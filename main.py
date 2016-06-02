#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
raspido Copyright (C) 2016 by Daniel Körsten aka TechnikAmateur
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import sqlite3, os, sys, time
#create DB if not exists
if not os.path.exists("database"):
    print("creating database...")
    os.mkdir("database")
    connection = sqlite3.connect("database/raspido.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS streams(
                      id INTEGER PRIMARY KEY,
                      url TEXT,
                      shortname TEXT);""")
    connection.close()
    print("done!")
#functions:
def addstream(url, shortname):
    connection = sqlite3.connect("database/raspido.db")
    cursor = connection.cursor()
    for i in range(1,100):
        try:
            cursor.execute("""INSERT INTO streams(id, url, shortname)
                              VALUES(?,?,?)""", (i, url, shortname))
            connection.commit()
        except:
            pass
        else:
            break
    connection.close()
    result = i

def removestream(aname):
    aname = str(aname)
    if "http" not in aname:
        connection = sqlite3.connect("database/raspido.db")
        cursor = connection.cursor()
        connection.close()
    result =
#if parameter 1 = add:
if sys.argv[1] == "add":
    try:
        url = sys.argv[2]
        shortname = sys.argv[3]
    except:
        error = True
    if error != True:
        erg = addstream(url, shortname)
        if erg < 100:
            print("Operation successfully performed.")
        else:
            print("Command not feasible. Database is full!")
"""
Please kepp in mind ;)
save_stdout = sys.stdout
fh = open("bridge.txt","w")
sys.stdout = fh
print("full")
sys.stdout = save_stdout
fh.close()
"""
    else:
        print("Command not feasible. You gave me the wrong parameters!")
#if parameter 1 = listall
if sys.argv[1] == "listall":
    print("Collecting data from default database.")
    print(" ")
    time.sleep(2)
    try:
        connection = sqlite3.connect("database/raspido.db")
        cursor = connection.cursor()
        sql = "SELECT * FROM defaultstream"
        cursor.execute(sql)
        for dsatz in cursor:
            print(dsatz[0], dsatz[1], dsatz[2])
        connection.close()
    except:
        print("Error: default database not found!")
    print(" ")
    input("Press any key to list user database...")
    print(" ")
    print("Collecting data from user database.")
    print(" ")
    time.sleep(2)
    try:
        connection = sqlite3.connect("database/raspido.db")
        cursor = connection.cursor()
        sql = "SELECT * FROM streams"
        cursor.execute(sql)
        for dsatz in cursor:
            print(dsatz[0], dsatz[1], dsatz[2])
        connection.close()
    except:
        print("Error: user database not found!")
    print(" ")
    print("done!")
