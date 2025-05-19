from icecream import ic
import sqlite3
import os
import requests
from bs4 import BeautifulSoup
import re


class T:
    status_code = '(local file)',
    text = open('Список прилунений — Википедия.html').read()
page = T()
# page = requests.get('https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%BF%D1%80%D0%B8%D0%BB%D1%83%D0%BD%D0%B5%D0%BD%D0%B8%D0%B9#%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%BC%D1%8F%D0%B3%D0%BA%D0%B8%D1%85_%D0%BF%D0%BE%D1%81%D0%B0%D0%B4%D0%BE%D0%BA')

ic(page.status_code)

soup = BeautifulSoup(page.text, "html.parser")
soup.select('.mw-file-description')
for i in soup.find_all(class_='reference'): i.decompose()
# print(soup.prettify())
# exit(0)
# exit(0)

try: os.remove('lab15.db')
except: pass
con = sqlite3.connect("lab15.db")
cur = con.cursor()
# Наименование
# Страна
# Дата прилунения
# Место прилунения
# Описание миссии
cur.execute('''CREATE TABLE Raw (
    name TEXT,
    country TEXT,
    date TEXT,
    place TEXT,
    description TEXT
)''')

fields = ['name', 'country', 'date', 'place', 'description']

def it():
    t = soup.select('table.wikitable')
    for i in t:
        for j in i.text.split('\n'):
            j = j.strip()
            if j == '': continue
            yield j
c = 0
n = 0
t = [None] * len(fields)
tr = str.maketrans('', '', '«»')
for j in it():    
        if c > 2: break
        elif j == 'Описание миссии': c += 1
        elif c == 2:
            if j == 'Изображение': break
            t[n] = j.translate(tr)
            n = n+1
            if n == len(fields):
                cur.execute(fr'INSERT INTO Raw VALUES {tuple(t)}')
                n = 0

cur.execute('SELECT * FROM Raw'); ic(cur.fetchall())

# TODO: multiple tables (see the task)