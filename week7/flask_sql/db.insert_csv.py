import psycopg2
import csv 

query = """INSERT INTO players 
(id, name, age, height, weight, shot, birth_place, birthdate, number)
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

conn = psycopg2.connect(database='flask', 
                        user='postgres', 
                        password='postgres')

cursor = conn.cursor()
with open('./players.csv', 'r') as f:
    reader = csv.reader(f)
    # skip the header row
    next(reader)
    for row in reader:
        cursor.execute(query, row)

conn.commit()
