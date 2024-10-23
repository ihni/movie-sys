from models import Showtime

class ShowtimeService:
    def create_showtime(self, year, month_number, day, time):
        return Showtime(year, month_number, day, time)