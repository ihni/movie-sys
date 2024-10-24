from datetime import datetime, timedelta

class Movie:
    def __init__(self, title, length):
        self.title = title
        self.length = length    # in minutes
        self.showtimes = []

    def add_showtime(self, showtime):
        if showtime not in self.showtimes:
            self.showtimes.append(showtime)
        else:
            print(f"Showtime {showtime.showtime} already exists for {self.title}")
    
    def get_end_time(self, showtime):
        return showtime.showtime + timedelta(
            minutes = self.length
        )

    def __str__(self):
        showtime_str = ', '.join(
            showtime.showtime.strftime('%Y-%m-%d %I:%M %p') for showtime in self.showtimes
        )
        return f"{self.title} - Showtimes: {showtime_str} (Length: {self.length} min)"