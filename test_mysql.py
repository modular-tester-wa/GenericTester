import mysql.connector
from threading import Timer
import datetime
import socket
import sys


def check_lock_open_table():
    # cnx = mysql.connector.connect(user='wa', password='StateCuba', host='uk.sql05.yourwebservers.com', port=13307, database='wa')
    cnx = mysql.connector.connect(user='watestda_test',
                                  password='Watestda_test-Password-8299',
                                  host='185.197.130.31',
                                  port=3306,
                                  database='watestda_test')
    cursor = cnx.cursor(buffered=True, named_tuple=True)
    mysn = "BQ2231"
    myLock = "1"

    remoteSN = "BQ2237"
    remoteLock = "1"

    snTerminal = ""
    idLock = ""

    query = ("SELECT * from data")
    cursor.execute(query)

    print(cursor.column_names)
    # print(cursor.rowcount)

    for (row) in cursor:
        print(row)

    cursor.close()
    cnx.close()


check_lock_open_table()

# WA Site Ground hosting
# testdata@westernautomation.com
# 0fKCBz32Um8F

# FTP
# tester_01
# Tester_01-password
# Home folder /home/watestda/public_html/tester_01

# MySql
# Domain:
# Primary Domain: watestdata.com
# Database: watestda_test
# User: watestda_test
# Password: Watestda_test-Password-8299


# port 3306