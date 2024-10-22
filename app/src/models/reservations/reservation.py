class Reservation:
    def __init__(self, movie, theatre, seat_name, user):
        self.movie = movie
        self.theatre = theatre # Instance of a Theatre, not a name
        self.seat_name = seat_name
        self.user = user
        self.location = theatre.location