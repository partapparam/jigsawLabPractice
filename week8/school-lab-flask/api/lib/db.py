# ORM function
# save an object instance
# find_all
# find_by_id
# find by name
# build from record
# build from records
# drop all table
# drop table
#drop record
# get db

from settings import TEST_DB_NAME, TEST_DB_USER, DB_NAME, DB_USER
from flask import g
from flask import current_app
import psycopg2

test_conn = psycopg2(TEST_DB_NAME, TEST_DB_USER, 'password')
test_cursor = test_conn.cursor()

conn = psycopg2(DB_NAME, DB_USER, 'password')

def get_db(database, user):
    # check to see if db exists in the 'g' context
    if 'db' not in g:
        # if not, we create it with the current app, the requesting app's context
        g.db = psycopg2(dbname=current_app.config['DB_NAME'], user = current_app.config['DB_USER'], password = current_app['PASSWORD'])
    return g.db 

def save(obj, conn):
    # save query requires: table, column names and values
    # obj.
    table_name = obj.__table__
    columns = keys(obj.__dict__)
    values = values(obj.__dict__)
    query = """INSERT INTO %s (%s) VALUES (%s)"""
    cursor = conn.cursor()
    cursor.execute(query, (table_name, columns, values,))
    conn.commit()
    get_query = """SELECT * FROM %s ORDER BY id LIMIT 1"""
    cursor.execute(get_query, (table_name,))
    saved = cursor.fetchone()
    return saved

def keys(obj):
    key_list = obj.keys()
    return ', '.join(key_list)

def values(obj):
    value_list = obj.values()
    return ', '.join(value_list)


