# Krzysztof Garbala
# -*- coding: utf-8 -*-

import MySQLdb, csv, os
SQL = "INSERT INTO DVD (Name, Category, Country)
VALUES ('Cardinal', 'Stavanger', 'Norway');"
def writeCSV():
    try:
        db = MySQLdb.connect("localhost", "root", "niepowiem", "DVDCOLLECTION")
        c=db.cursor()
        c.execute(SQL)
        output= c.fetchall()
        c.close()
        db.close()
    except:
        input("blad [Enter..]")
        return