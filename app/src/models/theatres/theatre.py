from .seat import Seat

class Theatre:
    def __init__(self, movie, location, total_rows, total_columns):
        self.movie = movie
        self.location = location
        self.total_rows = total_rows
        self.total_columns = total_columns
        self.seats = self.generate_seats()
        self.booked_seats = 0
    
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

    def display_seats(self):
        for row in self.seats:
            for seat in row:
                print(seat.name, end=" ")
            print()

    def get_seat_position(self, seat_name):
        row_part = ''.join(filter(str.isalpha, seat_name))
        column_part = ''.join(filter(str.isdigit, seat_name))
        column = int(column_part) - 1

        row = 0
        for index, char in enumerate(reversed(row_part)):
            row += (ord(char) - ord('A')) * (26 ** index)
        return row, column

    def reserve_seat_by_name(self, seat_name):
        row, column = self.get_seat_position(seat_name)
        return self.reserve_seat(row, column)
    
    def reserve_seat(self, row, column) -> bool:
        seat = self.seats[row][column]
        if seat.is_avaible:
            seat.is_avaible = False
            self.booked_seats += 1
            return True
        else:
            return False
        
    def release_seat_by_name(self, seat_name):
        row, column = self.get_seat_position(seat_name)
        return self.release_seat(row, column)
    
    def release_seat(self, row, column) -> bool:
        seat = self.seats[row][column]
        if seat.is_avaible:
            return False
        seat.is_avaible = True
        self.booked_seats -= 1
        return True

    def __str__(self):
        return f"{self.movie} playing at theatre {self.location} with {self.available_seats()} seats left."