import psycopg2
query = """DROP TABLE IF EXISTS players;

CREATE TABLE IF NOT EXISTS players (
  id serial PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  age INT,
  height VARCHAR(255),
  weight VARCHAR(255),
  shot VARCHAR(16),
  birth_place VARCHAR(255),
  birthdate VARCHAR(255),
  number INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);"""

conn = psycopg2.connect(database='flask', user='postgres', password='postgres')
cursor = conn.cursor()
cursor.execute(query)
conn.commit()
conn.close()

