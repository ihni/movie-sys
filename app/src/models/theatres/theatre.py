from .seat import Seat

class Theatre:
    def __init__(self, location, total_rows, total_columns):
        self.location = location
        self.total_rows = total_rows
        self.total_columns = total_columns
        self.movies = []
        self.seats = self.generate_seats()
    
    def add_movie(self, movie):
        self.movies.append(movie)

    def available_seats(self) -> int:
        return (self.total_rows * self.total_columns) - self.booked_seats
    
    def generate_seats(self):
        seat_matrix = []
        for row in range(self.total_rows):
            row_seats = []
            for column in range(self.total_columns):
                seat = Seat(row, column)
                row_seats.append(seat)
            seat_matrix.append(row_seats)
        return seat_matrix

    def available_seats_list(self) -> list:
        available_seats = []
        for row in self.seats:
            for seat in row:
                if seat.is_available:
                    available_seats.append(seat.name)
        return available_seats

    def display_seats(self):
        for row in self.seats:
            for seat in row:
                print(seat.name, end=" ")
            print()

    def display_seats_with_cli_color(self):
        for row in self.seats:
            for seat in row:
                if seat.is_available:
                    print('\x1b[6;30;42m' + seat.name + '\x1b[0m', end=" ")
                else:
                    print('\x1b[38;5;9m' + seat.name + '\x1b[0m', end=" ")
            print()

    def get_seat_position(self, seat_name):
        row_part = ''.join(filter(str.isalpha, seat_name))
        column_part = ''.join(filter(str.isdigit, seat_name))
        column = int(column_part) - 1

        row = 0
        for index, char in enumerate(reversed(row_part)):
            row += (ord(char) - ord('A')) * (26 ** index)
        return row, column

    def __str__(self):
        return f"{self.movie} playing at theatre {self.location} with {self.available_seats()} seats left."