from datetime import datetime, timedelta

class Movie:
    def __init__(self, title, showtime, length):
        self.title = title
        self.showtime = showtime # showtime obj
        self.length = length    # in minutes
        self.endtime = self.set_end_time()

    def set_end_time(self):
        return self.showtime.showtime + timedelta(
            minutes = self.length
        )

    def __str__(self):
        return f"{self.title} - Showtime: {self.showtime.showtime.strftime('%Y-%m-%d %I:%M %p')} (Length: {self.length} min)"