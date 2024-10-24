from datetime import datetime, timedelta
from .seat import Seat 

class Showtime:
    def __init__(self, movie, theatre, year, month_number, day, time):
        self.movie = movie # reference to movie object
        self.theatre = theatre # reference to theatre instance
        self.year = year
        self.month_number = month_number
        self.day = day
        self.time = time
        self.showtime = self.set_showtime()
        self.seats = self.create_seat_copy()
        self.booked_seats = 0

    def create_seat_copy(self):
        copy_of_seats = []
        for row in self.theatre.seats:
            copied_row = []
            for seat in row:
                copied_seat = Seat(seat.row, seat.column)
                copied_row.append(copied_seat)
            copy_of_seats.append(copied_row)
        return copy_of_seats

    def check_seat_availability(self, seat_name):
        row, column = self.theatre.get_seat_position(seat_name)
        seat = self.seats[row][column]
        return seat.is_available

    def reserve_seat_by_name(self, seat_name):
        row, column = self.theatre.get_seat_position(seat_name)
        return self.reserve_seat(row, column)

    def release_seat_by_name(self, seat_name):
        row, column = self.theatre.get_seat_position(seat_name)
        return self.release_seat(row, column)

    def reserve_seat(self, row, column) -> bool:
        seat = self.seats[row][column]
        if seat.is_available:
            seat.is_available = False
            self.booked_seats += 1
            return True
        return False

    def release_seat(self, row, column) -> bool:
        seat = self.seats[row][column]
        if not seat.is_available:
            seat.is_available = True
            self.booked_seats -= 1
            return True
        return False
    
    def available_seats(self) -> int:
        return sum(seat.is_available for row in self.seats for seat in row)

    def available_seats_list(self) -> list:
        return [seat.name for row in self.seats for seat in row if seat.is_available]

    def to_24h_format(self):
        return self.showtime.strftime("%H:%M")
    
    def set_showtime(self):
        datetime_str = f"{self.year}-{self.month_number}-{self.day} {self.time}"
        return datetime.strptime(datetime_str, "%Y-%m-%d %I:%M %p")
    
    def __str__(self):
        return f"Showtime: {self.showtime.strftime('%Y-%m-%d %I:%M %p')}"