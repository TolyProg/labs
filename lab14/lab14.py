import sqlite3

con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute("CREATE TABLE items(name, description, price, have)")
cur.execute("CREATE TABLE orders(date, status, linked)")
cur.execute("CREATE TABLE clients(name, address, contact_info)")

