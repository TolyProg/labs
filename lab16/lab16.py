from selenium import webdriver
from selenium.webdriver.common.by import By
from icecream import ic
import os
from pypika import Table, Query, Database, Column, Order
from pypika.functions import Count, Avg
import sqlite3

driver = webdriver.Chrome()

# driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.get(f"file://{os.getcwd()}/IOCCC.html")
driver.implicitly_wait(0.1) # доки говорят, что это не самый лучший способ

content = driver.find_element(by=By.ID, value='content')
t = content.text.split('\n')[1:-1]
t.append('END')

entries = []

entry = []
gotDigit = False
for l in t:
    if ' is for ' in l: continue

    if l == 'END' or (gotDigit and not l[0].isdigit()):
        entries.append(entry)
        entry = []
    gotDigit = l[0].isdigit()
    entry.append(l)

try: os.remove('lab16.db')
except: pass
con = sqlite3.connect('lab16.db')
cur = con.cursor()

q = Query \
    .create_table('Persons') \
    .columns(
        Column('author_name', 'TEXT', nullable=False),
        Column('author_location', 'TEXT', nullable=True),
        Column('url', 'TEXT', nullable=True),
        Column('github', 'TEXT', nullable=True)) \
    .primary_key('author_name', 'author_location')
cur.execute(q.get_sql())
persons = Table('Persons')

q = Query \
    .create_table('Projects') \
    .columns(
        Column('author_name', 'TEXT', nullable=False),
        Column('author_location', 'TEXT', nullable=False),
        Column('year', 'INT', nullable=False),
        Column('name', 'TEXT', nullable=False),
        Column('description', 'TEXT', nullable=False)) \
    .foreign_key(['author_name', 'author_location'], \
        persons, ['author_name', 'author_location'])
cur.execute(q.get_sql())
projects = Table('Projects')

def parse_project(author_name, author_location, text):
    year = text[0:4]
    t = text[5:].split('-')
    name = t[0].strip()
    desc = t[1].strip()
    q = projects.insert(author_name, author_location, year, name, desc)
    cur.execute(q.get_sql())

for e in entries:
    name = e[0]
    location = url = github = None
    for t in e[1:]:
        if 'Location: ' in t:
            location = t.replace('Location: ', '')
        elif 'URL: ' in t:
            url = t.replace('URL: ', '')
        elif 'GitHub: ' in t:
            github = t.replace('GitHub: ', '')
        elif t[0] == '1' or t[0] == '2':
            parse_project(name, location, t)
    q = persons.insert(name, location, url, github)
    cur.execute(q.get_sql())

n = 1
def run(q):
    global n
    q = q.get_sql()
    ic(f'Query {n}:', q)
    cur.execute(q)
    ic(cur.fetchall())
    n += 1

# 2 запроса с JOIN

run(Query \
    .from_(projects) \
    .select('*') \
    .join(persons) \
    .on_field('author_name', 'author_location'))

run(Query \
    .from_(persons) \
    .select('*') \
    .join(projects) \
    .on_field('author_name', 'author_location'))

# 3 запроса с расчётом статистики/группировкой/агрегирующими функциями

# сколько проектов у автора
run(Query \
    .from_(persons) \
    .select(
        persons.author_name,
        persons.author_location,
        Count('*')) \
    .groupby(persons.author_name, persons.author_location) \
    .join(projects) \
    .on_field('author_name', 'author_location'))

# сколько проектов из стран + сортировка
run(Query \
    .from_(persons) \
    .select(
        persons.author_location,
        Count('*')) \
    .groupby(persons.author_location) \
    .orderby(Count('*'), order=Order.desc) \
    .join(projects) \
    .on_field('author_name', 'author_location'))

# сколько проектов на человека в среднем по странам
t = Query \
    .from_(persons) \
    .select(
        persons.author_location.as_('location'),
        Count(projects.name).as_('cnt')) \
    .groupby(persons.author_name, persons.author_location) \
    .join(projects) \
    .on_field('author_name', 'author_location')
run(Query \
    .from_(t) \
    .select(
        'location',
        Avg(t.cnt)) \
    .groupby('location'))

driver.quit()
con.commit()
con.close()