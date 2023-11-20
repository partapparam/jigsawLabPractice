# create the plane class here
import datetime
class Plane:
    def __init__(self, seats_per_row, number_of_rows, year):
      self.seats_per_row = seats_per_row
      self.number_of_rows = number_of_rows
      self.year = year

    def total_seats(self):
       return self.seats_per_row * self.number_of_rows
    
    def age(self):
       now = datetime.datetime.now()
       return now.year - self.year