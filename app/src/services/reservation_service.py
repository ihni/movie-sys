from models import Reservation

class ReservationService:
    def __init__(self):
        self.reservations = []

    def is_movie_in_theatre(self, movie, theatre) -> bool:
        '''checks if movie obj in a theatre's list'''
        return movie in theatre.movies

    def is_seat_reserved(self, theatre, seat_name) -> bool:
        '''checks if the seat is reserved in the theatre
            if not, create a reservation and return True'''
        return theatre.reserve_seat_by_name(seat_name)

    def create_reservation(self, movie, theatre, seat_name, user) -> object:
        if not self.is_movie_in_theatre(movie, theatre):
            raise ValueError("Movie is not being shown in this theatre.")
        if not self.is_seat_reserved(theatre, seat_name):
            raise Exception("Seat is not available")
        
        reservation = Reservation(movie = movie,
                                  theatre = theatre,
                                  seat_name = seat_name,
                                  user = user)
        self.reservations.append(reservation)
        user.add_reservation(reservation)
        return reservation
    
    def cancel_reservation(self, remove_reservation) -> bool:
        for reservation in self.reservations:
            if reservation == remove_reservation:
                theatre = remove_reservation.theatre
                theatre.release_seat_by_name(remove_reservation.seat_name)
                self.reservation.remove(remove_reservation)
                return True
        return False
    
    def find_reservation_by_email(self, email) -> object:
        for reservation in self.reservations:
            if reservation.user.email == email:
                return reservation
        return None
    
    
    def list_reservations(self) -> list:
        return self.reservations
    
    def number_of_reservations(self) -> int:
        return len(self.reservations)