import mysql.connector

def koneksi_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db_login"
    )
