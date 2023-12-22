from api.models.course import Course
import pytest
from api.lib.db import save, test_conn, test_cursor, drop_all_tables, build_from_records

# define a pytest.fixture that will create a few courses and drop them
@pytest.fixture
def courses():
    drop_all_tables(test_conn, test_cursor)

    yield
    drop_all_tables(test_conn, test_cursor)


# test that a course instance can be created
def test_course_creation():
    name = 'science'
    obj = Course(course_name = name)
    assert obj.course_name == name

def test_save_course(courses):
    obj = Course(course_name = 'Math')
    record = save(obj, test_conn)
    assert record.course_name == obj.course_name
    assert record.id == 1