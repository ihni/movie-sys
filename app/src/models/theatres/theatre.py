from .seat import Seat
from lib import MovieQueue

class Theatre:
    def __init__(self, location, total_rows, total_columns):
        self.location = location
        self.total_rows = total_rows
        self.total_columns = total_columns

        self.movies = []
        self.movie_queue = MovieQueue()
        self.seats = self.generate_seats()
    
    def add_movie(self, movie):
        self.movies.append(movie)
        self.movie_queue.enqueue(movie)
    
    def generate_seats(self):
        seat_matrix = []
        for row in range(self.total_rows):
            row_seats = []
            for column in range(self.total_columns):
                seat = Seat(row, column)
                row_seats.append(seat)
            seat_matrix.append(row_seats)
        return seat_matrix

    def get_seat_position(self, seat_name):
        row_part = ''.join(filter(str.isalpha, seat_name))
        column_part = ''.join(filter(str.isdigit, seat_name))
        column = int(column_part) - 1

        row = 0
        for index, char in enumerate(reversed(row_part)):
            row += (ord(char) - ord('A')) * (26 ** index)
        return row, column

    def __str__(self):
        return f"{self.movies} playing at theatre {self.location}"