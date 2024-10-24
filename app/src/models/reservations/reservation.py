class Reservation:
    def __init__(self, movie, showtime, seat_name, user, theatre):
        self.movie = movie # Instance of a movie
        self.showtime = showtime # Instance of a showtime
        self.seat_name = seat_name
        self.user = user
        self.theatre = theatre