import api 
from settings import DB_NAME, DB_USER, PASSWORD

app = api.create_app(DB_NAME, DB_USER, PASSWORD)

# if __name__ == '__main__':
#     app.run(debug=True)

stu = api.models.Student(id=1, student_name='Parma')
api.db.build_from_record(obj=api.models.Student, record=stu.__dict__ )