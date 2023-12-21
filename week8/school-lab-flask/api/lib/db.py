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

from settings import TEST_DB_NAME, TEST_DB_USER
from flask import g
import psycopg2

test_conn = psycopg2(TEST_DB_NAME, TEST_DB_USER, 'password')
test_cursor = test_conn.cursor()

def get_db(database, user):
    if not g.db:
        g.db = psycopg2(database, user, 'password')
    return g.db 

