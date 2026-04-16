from datetime import datetime, timedelta

class Date:
    def __init__(self, day, month, year):
        self.date = datetime(year, month, day)

    def __sub__(self, other):
        return abs((self.date - other.date).days)

    def __add__(self, days):
        new_date = self.date + timedelta(days=days)
        return Date(new_date.day, new_date.month, new_date.year)

    def __str__(self):
        return self.date.strftime("%d-%m-%Y")