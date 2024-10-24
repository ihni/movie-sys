from models import Showtime

class ShowtimeService:
    def __init__(self):
        self.showtimes = []

    def create_showtime(self, movie, theatre, year, month_number, day, time):
        showtime = Showtime(movie, theatre, year, month_number, day, time)
        movie.add_showtime(showtime)
        self.showtimes.append(showtime)
        return showtime
    
    def get_showtimes_by_movies(self, movie) -> list:
        showtimes_by_movies = []
        for showtime in self.showtimes:
            if showtime.movie == movie:
                showtimes_by_movies.append(showtime)
        return showtimes_by_movies
    
    def get_showtimes_by_theatre(self, theatre) -> list:
        showtimes_by_theatre = []
        for showtime in self.showtimes:
            if showtime.theatre == theatre:
                showtimes_by_theatre.append(showtime)
        return showtimes_by_theatre
    
    def check_seat_availability(self, showtime, seat_name) -> bool:
        row, column = showtime.get_seat_position(seat_name)
        return showtime.seats[row][column].is_available
    
    def release_seat(self, showtime, seat_name) -> bool:
        return showtime.release_seat_by_name(seat_name)