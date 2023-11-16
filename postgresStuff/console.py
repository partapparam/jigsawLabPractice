import psycopg2
import pandas as pd

conn = psycopg2.connect(dbname="adventureworks", user="postgres")

cursor = conn.cursor()

pd.read_sql("select * from sales.Customer limit 5", conn)