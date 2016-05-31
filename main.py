#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version 1.0
import sqlite3, os, sys, time
#create DB
if not os.path.exists("database"):
    print("creating database...")
    os.mkdir("database")
    connection = sqlite3.connect("database/raspido.db")
    cursor = connection.cursor()
    sql = "CREATE TABLE streams("\
        "id INTEGER PRIMARY KEY,"\
        "url TEXT,"\
        "shortname TEXT)"
    cursor.execute(sql)
    connection.close()
    print("done")
#functions:
def addstream(url, shortname):
    connection = sqlite3.connect("database/raspido.db")
    cursor = connection.cursor()
    x = 0
    for i in range(1,100):
        try:
            cursor.execute("""INSERT INTO streams(id, url, shortname)
                              VALUES(?,?,?)""", (i, url, shortname))
            connection.commit()
        except:
            x = x + 1 # nur, damit etwas passiert
        else:
            break
    connection.close()
    result = i
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
            save_stdout = sys.stdout
            fh = open("bridge.txt","w")
            sys.stdout = fh
            print("okay")
            sys.stdout = save_stdout
            fh.close()
        else:
            save_stdout = sys.stdout
            fh = open("bridge.txt","w")
            sys.stdout = fh
            print("full")
            sys.stdout = save_stdout
            fh.close()
    else:
        save_stdout = sys.stdout
        fh = open("bridge.txt","w")
        sys.stdout = fh
        print("parameter error")
        sys.stdout = save_stdout
        fh.close()
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
