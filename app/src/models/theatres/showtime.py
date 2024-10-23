from datetime import datetime, timedelta

class Showtime:
    def __init__(self, year, month_number, day, time):
        self.year = year
        self.month_number = month_number
        self.day = day
        self.time = time
        self.showtime = self.set_showtime()

    def to_24h_format(self):
        return self.showtime.strftime("%H:%M")
    
    def set_showtime(self):
        datetime_str = f"{self.year}-{self.month_number}-{self.day} {self.time}"
        return datetime.strptime(datetime_str, "%Y-%m-%d %I:%M %p")
    
    def __str__(self):
        return f"Showtime: {self.showtime.strftime('%Y-%m-%d %I:%M %p')}"