import api 
from settings import TEST_DB_NAME, DB_USER, PASSWORD
# TODO change back to DB_NAME
import psycopg2

conn = psycopg2.connect(database=TEST_DB_NAME, user=DB_USER)

# app = api.create_app(DB_NAME, DB_USER, PASSWORD)

# if __name__ == '__main__':
#     app.run(debug=True)

s = api.models.Student(id=14, student_name='param')
r = api.db.save(obj=s, conn=conn )
print(r.__dict__)