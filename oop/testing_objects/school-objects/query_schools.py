import pandas as pd
from school import *

def query_api():
    url = "https://raw.githubusercontent.com/jigsawlabs-student/decision-trees-intro/master/3-practical-ds-4/nyc_hs_sat.csv"
    df = pd.read_csv(url)
    return df.to_dict('records')

def get_school(school, keys):
    return {k:v for k, v in school.items() if k in keys}

def build_instances(school_dicts):
    selected_attrs = ['dbn', 'name', 'boro', 'writing_score', 'math_avg', 
        'reading_avg', 'total_students', 'attendance_rate']
    selected_schools = [get_school(school, selected_attrs) for school in school_dicts]
    schools = [School(**selected_school) for selected_school in selected_schools]
    return schools


def largest_total_score_school(schools):
    # return sorted(schools, key=lambda school: school.math_avg + school.reading_avg + school.writing_score)[-1]

    # return sorted(schools, key=lambda school: school.total_score())[-1]

    # we can also do this with max
    return max(schools, key=lambda school: school.total_score())

def average_total_score_of(schools):
    total_score_for_school = [school.total_score() for school in schools]
    number_of_schools = len(total_score_for_school)
    return int(sum(total_score_for_school)/number_of_schools)

def largest_average_student_attendance(schools):
    return max(schools, key=lambda school: school.avg_student_attendance())