import psycopg2 
from flask import Flask

conn = psycopg2.connect(database='flask', user='postgres', password='postgres')
