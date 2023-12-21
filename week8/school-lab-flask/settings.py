import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
TEST_DB_NAME = os.getenv('TEST_DB_NAME')
TEST_DB_USER = os.getenv('TEST_DB_USER')
PASSWORD = os.getenv('PASSWORD')