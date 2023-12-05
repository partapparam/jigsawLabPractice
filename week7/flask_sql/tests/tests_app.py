# enuring proper setup of our database requires a couple things
# First, we need to create a test DB just for running tests
# This way, we can add/remove data without messing with real DB
# Second, we create records just for the purpose of our test

# Pytest fixtures
import pytest 
import psycopg2
from app import players


conn = psycopg2.connect(database='flask', user='param', password='postgres')
cursor = conn.cursor()

@pytest.fixture()
def db_with_players():
    # setup db with player
    insert_into = 'INSERT INTO customers (first_name, last_name, category) VALUES (%s, %s, %s)'
    cursor.execute(insert_into, ('bob', 'smith', 'premium'))
    cursor.execute(insert_into, ('fred', 'samuel', 'standard'))
    cursor.commit()
    # yield to run the test
    yield
    # cleanup after the test
    cursor.execute('DELETE FROM customers;')
    cursor.commit()


def test_players(db_with_players):   
    assert players() == 1