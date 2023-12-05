import psycopg2 
from flask import Flask


conn = psycopg2.connect(database='flask', user='param', password='postgres')
cursor = conn.cursor()
sql_file = open('./db.sql', 'r')
cursor.execute(sql_file.read())

