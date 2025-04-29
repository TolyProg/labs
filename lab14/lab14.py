from icecream import ic
import sqlite3
import os

os.remove('tutorial.db')
con = sqlite3.connect("tutorial.db")
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
    product FOREIGN KEY,
    num INTEGER,
    client INTEGER
    PRIMARY KEY (id,product,num)
    FOREIGN KEY (client) REFERENCES Clients
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
    ("Внешняя видеокарта", "Утолщение на проводе", 15, 1000),
    ("V2_1", "Странное подобие логики", 3_000_000, 1),
]

ol = [
    (1, "01-01-72", "OK", "Морковь", 3, 1)
]

for i in il: cur.execute(f'INSERT INTO Items VALUES {i}')
for i in ol: cur.execute(f'INSERT INTO Orders VALUES {i}')

ic(cur.execute('SELECT * FROM Items'), cur.fetchall())

ic(cur.execute('SELECT * FROM Orders'), cur.fetchall())
