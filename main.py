#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version 1.0
import sqlite3, os, sys#, logging
#create DB
#logging.basicConfig(filename="raspido.log",level=logging.DEBUG)
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
#if parameter 1 = add
if sys.argv[1] == "add":
    try:
        url = sys.argv[2]
        shortname = sys.argv[3]
    except:
        error = True
#        logging.debug("Error 01: Parameter nicht vorhanden!")
    if error != True:
        erg = addstream(url, shortname)
        if erg < 100:
#            logging.info("Info: url added to stream.")
            save_stdout = sys.stdout
            fh = open("bridge.txt","w")
            sys.stdout = fh
            print("okay")
            sys.stdout = save_stdout
            fh.close()
        else:
#            logging.debug("Error 02: Command not feasible. Database contains more than 100 channels.")
#functions
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
    return result
