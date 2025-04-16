#------------------------------------------------------------
# This file creates a shared DB connection resource
#------------------------------------------------------------
from flaskext.mysql import MySQL
from pymysql import cursors


# the parameter instructs the connection to return data 
# as a dictionary object. 
# as a dictionary object.
db = MySQL(cursorclass=cursors.DictCursor)

import mysql.connector

def db_connection():
    return mysql.connector.connect(
        host='db',
        user='root',
        password='password123',
        database='projectdb'
    )