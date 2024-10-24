from models import Reservation
from datetime import datetime

class ReservationService:
    def __init__(self):
        self.reservations = []

    def add_reservation(self, reservation) -> None:
        self.reservations.append(reservation)

    def is_movie_in_showtime(self, movie, showtime) -> bool:
        return movie == showtime.movie

    def is_seat_available(self, showtime, seat_name) -> bool:
        return showtime.check_seat_availability(seat_name)

    def is_showing_now_or_later(self, showtime) -> bool:
        current_time = datetime.now()
        return showtime.showtime > current_time

    def create_reservation(self, movie, showtime, seat_name, user) -> object:
        if not self.is_movie_in_showtime(movie, showtime):
            raise ValueError("Movie is not being shown in this showtime.")
        
        if not self.is_showing_now_or_later(showtime):
            raise Exception("Cannot reserve; the movie is no longer showing.")

        if not self.is_seat_available(showtime, seat_name):
            raise Exception("Seat is not available")
        
        showtime.reserve_seat_by_name(seat_name)

        reservation = Reservation(
            movie = movie,
            showtime = showtime,               
            theatre = showtime.theatre,
            seat_name = seat_name,
            user = user
        )
        self.add_reservation(reservation)
        user.add_user_reservation(reservation)
        return reservation
    
    def cancel_reservation(self, remove_reservation) -> bool:
        for reservation in self.reservations:
            if reservation == remove_reservation:
                showtime = remove_reservation.theatre
                showtime.release_seat_by_name(remove_reservation.seat_name)
                self.reservations.remove(remove_reservation)
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