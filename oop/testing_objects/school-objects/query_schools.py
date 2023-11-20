import pandas as pd

def query_api():
    url = "https://raw.githubusercontent.com/jigsawlabs-student/decision-trees-intro/master/3-practical-ds-4/nyc_hs_sat.csv"
    df = pd.read_csv(url)
    return df.to_dict('records')


def build_instances(school_dicts):
    selected_attrs = ['dbn', 'name', 'boro', 'writing_score', 'math_avg', 
        'reading_avg', 'total_students', 'attendance_rate']
    edited_schools = [{}]


def largest_total_score_school(schools):
    pass

def average_total_score_of(schools):
    pass

def largest_average_student_attendance(schools):
    pass