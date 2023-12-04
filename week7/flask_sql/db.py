conn = psycopg2.connect(database='flask', user='postgres', password='postgres')

create_table = """CREATE TABLE IF NOT EXISTS players (
id SERIAL PRIMARY KEY,
name VARCHAR,
age INT,
ht 
)"""