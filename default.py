#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3, os
if not os.path.exists("database"):
    os.mkdir("database")
    connection = sqlite3.connect("database/raspido.db")
    cursor = connection.cursor()
    sql = "CREATE TABLE defaultstream("\
        "id INTEGER PRIMARY KEY,"\
        "url TEXT,"\
        "shortname TEXT)"
    cursor.execute(sql)
    connection.close()
url = input("URL:")
shortname = input("shortname:")
print(url)
print(shortname)
eingabe = input('continue? Enter "YES"')
if eingabe != "YES":
    exit()
connection = sqlite3.connect("database/raspido.db")
cursor = connection.cursor()
x = 0
for i in range(1,1000):
    try:
        cursor.execute("""INSERT INTO defaultstream(id, url, shortname)
                          VALUES(?,?,?)""", (i, url, shortname))
        connection.commit()
    except:
        x = x + 1 # nur, damit etwas passiert
    else:
        break
connection.close()
connection = sqlite3.connect("database/raspido.db")
cursor = connection.cursor()
sql = "SELECT * FROM defaultstream"
cursor.execute(sql)
for dsatz in cursor:
    print(dsatz[0], dsatz[1], dsatz[2])
connection.close()
