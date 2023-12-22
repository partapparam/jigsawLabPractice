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

# test_conn = psycopg2(TEST_DB_NAME, TEST_DB_USER, 'password')
# test_cursor = test_conn.cursor()

# conn = psycopg2(DB_NAME, DB_USER, 'password')

def get_db():
    # check to see if db exists in the 'g' context
    if 'db' not in g:
        # if not, we create it with the current app, the requesting app's context
        g.db = psycopg2(dbname=current_app.config['DB_NAME'], user = current_app.config['DB_USER'], password = current_app['PASSWORD'])
    return g.db 

def close_db():
    db = g.pop('db', None)
    if db is not None:
        db.close()

def save(obj, conn):
    # save query requires: table, column names and values
    # obj.
    table_name = obj.__table__
    columns = keys(obj)
    # get values
    value_list = values(obj)
    # create a values insert list (%s) * len of values
    values_string = ', '.join(len(value_list) * ['%s'])
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({values_string})"
    cursor = conn.cursor()
    cursor.execute(query, tuple(value_list))
    conn.commit()
    # return the added value from the table
    get_query = f"SELECT * FROM {table_name} ORDER BY id DESC LIMIT 1"
    cursor.execute(get_query, table_name)
    record = cursor.fetchone()
    return build_from_record(type(obj), record)

def keys(obj):
    key_list = obj.__dict__.keys()
    return ', '.join(key_list)

def values(obj):
    return obj.__dict__.values()

def build_from_record(Class, record):
    # check for missing record, it nothing that return None
    if not record: return None
    # get Class columns
    cols = Class.columns
    # create a new Class object
    obj = Class()
    # zip together cols and record
    attr = dict(zip(cols, record))
    # set attr to object dict
    obj.__dict__ = attr
    return obj

def build_from_records(obj, records):
    return [build_from_record(record) for record in records] 

def find_all(obj, conn):
    query = """SELECT * FROM %s"""
    cursor = conn.cursor()
    cursor.execute(query, (obj.__table__))
    records = cursor.fetchall()
    return records

def find_by_id(id, conn):
    