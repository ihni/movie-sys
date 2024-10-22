from models import Reservation

class ReservationService:
    def __init__(self):
        self.reservations = []

    def create_reservation(self, movie, theatre, seat_name, user) -> object:
        if not theatre.reserve_seat_by_name(seat_name):
            raise Exception("Seat is not available")
        
        reservation = Reservation(movie = movie,
                                  theatre = theatre,
                                  seat_name = seat_name,
                                  user = user)
        self.reservations.append(reservation)
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