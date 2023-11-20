class School:
    def __init__(self, name, reading_avg, math_avg, writing_score, boro, total_students, attendance_rate, dbn):
        self.name = name
        self.dbn = dbn
        self.reading_avg = reading_avg
        self.math_avg = math_avg
        self.boro = boro 
        self.writing_score = writing_score 
        self.total_students = total_students 
        self.attendance_rate = attendance_rate
    
    city = 'New York City'

    
    def total_score(self):
        return self.math_avg + self.reading_avg + self.writing_score
    
    def avg_student_attendance(self):
        return self.attendance_rate * self.total_students
    
    def max_score(self):
        return max(self.math_avg, self.reading_avg, self.writing_score)
        