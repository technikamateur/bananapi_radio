#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version 1.0
import sqlite3, os, sys
#create DB
if not os.path.exists("database"):
    os.mkdir("database")
    connection = sqlite3.connect("database/raspido.db")
    cursor = connection.cursor()
    sql = "CREATE TABLE streams("\
        "id INTEGER PRIMARY KEY,"\
        "url TEXT,"\
        "shortname TEXT)"
    cursor.execute(sql)
    connection.close()
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
