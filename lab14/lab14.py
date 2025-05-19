from icecream import ic
import sqlite3
import os

try: os.remove('lab14.db')
except: pass
con = sqlite3.connect("lab14.db")
cur = con.cursor()

cur.execute("""CREATE TABLE Items
(
    name TEXT PRIMARY KEY,
    description TEXT,
    price INTEGER,
    have INTEGER
)""")
cur.execute("""CREATE TABLE Orders
(
    id INTEGER,
    date DATE,
    status TEXT,
    product,
    num INTEGER,
    client INTEGER,
    PRIMARY KEY (id,product,num),
    FOREIGN KEY (client) REFERENCES Clients(name)
)""")
cur.execute("""CREATE TABLE Clients
(
    name PRIMARY KEY,
    address,
    contact_info
)""")

il = [
    ("Морковь", "Съедобная, может быть вкусная", 50, 10),
    ("Кортофель", "Съедобный, можно есть, может быть вкусный", 20, 10),
    ("Процессор", "Который под столом, нельзя есть", 20, 2000),
    ("Внешняя видеокарта", "Утолщение на проводе видеосигнала (на т.н. картиночном проводе), есть никто не решился", 15, 1000),
    ("V2_1", "Странное неформализованное устаревшее подобие логики", 9999**999, 1),
]

ol = [
    (1, "01-01-72", "OK", "Морковь", 2, 1),
    (1, "01-01-72", "OK", "Кортофель", 3, 1),
    (2, "16-05-25", "НЕOK", "V2_1", 1, 2),
    (3, "27-18-28", "OK", "Процессор", 64, 3),
    (3, "27-18-28", "OK", "Внешняя видеокарта", 512, 3),
    (4, "42-99-54", "OK", "Внешняя видеокарта", 3584, 3),
]

cl = [
    ('Зубенко Михаил Петрович', 'шумиловский городок, улица Мафиозника, дом 54', 'звать по кличке'),
    ('Подозрительный тип', 'полиморфная F омега', 'не стоит выводить (в том числе из себя)'),
    ('Компьюктерный гений (хацкер)', 'возле мощного процессора', 'не пытаться контактировать'),
]

for i in il: cur.execute(f'INSERT INTO Items VALUES {i}')
for i in ol: cur.execute(f'INSERT INTO Orders VALUES {i}')
for i in cl: cur.execute(f'INSERT INTO Clients VALUES {i}')

cur.execute('SELECT * FROM Items'); ic('Items', cur.fetchall())
cur.execute('SELECT * FROM Orders'); ic('Orders', cur.fetchall())
cur.execute('SELECT * FROM Clients'); ic('Clients', cur.fetchall())

cur.execute('SELECT * FROM Orders where client is 3'); ic('Client 3 orders:', cur.fetchall())