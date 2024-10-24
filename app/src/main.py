from config import *
from models import Theatre
from services import UserService
from services import ReservationService
from services import MovieService
from services import ShowtimeService
from utilities import DisplayService

user_service = UserService()
reservation_service = ReservationService()
movie_service = MovieService()
showtime_service = ShowtimeService()

'''
Creating Preset Data
'''

theatre1 = Theatre(
    location = ALL_THEATRE_LOCATIONS[0],
    total_rows = MAX_ROWS,
    total_columns = MAX_COLUMNS-2
)

coraline = movie_service.create_movie(title="Coraline", length=115)
spirited_away = movie_service.create_movie(title = "Spirited Away", length = 125)
chipmunks = movie_service.create_movie(title = "Alvin and the Chipmunks", length = 92)
pirates_carribean = movie_service.create_movie(title = "Pirates of the Caribbean", length = 143)

coraline_showtime1 = showtime_service.create_showtime(
    movie = coraline,
    theatre = theatre1,
    year = 2024,
    month_number = 10,
    day = 25,
    time = "10:00 AM"
)
coraline_showtime2 = showtime_service.create_showtime(
    movie = coraline,
    theatre = theatre1,
    year = 2024,
    month_number = 10,
    day = 25,
    time = "1:00 PM"
)
showtime2 = showtime_service.create_showtime(
    movie = spirited_away,
    theatre = theatre1,
    year = 2024,
    month_number = 10,
    day = 25,
    time = "5:00 PM"
)
showtime3 = showtime_service.create_showtime(
    movie = chipmunks,
    theatre = theatre1,
    year = 2024,
    month_number = 10,
    day = 25,
    time = "8:30 PM"
)
showtime4 = showtime_service.create_showtime(
    movie = pirates_carribean,
    theatre = theatre1,
    year = 2024,
    month_number = 10,
    day = 25,
    time = "11:30 PM"
)

theatre1.add_movie(coraline)
theatre1.add_movie(spirited_away)
theatre1.add_movie(chipmunks)
theatre1.add_movie(pirates_carribean)

'''Adding Users and Reserving Seats in different Showtimes'''

user1 = user_service.create_user(email = "test@gmail.com")
user2 = user_service.create_user(email = "gmail@yahoo.com")
reservation_service.create_reservation(coraline, coraline_showtime1, "A4", user1)
reservation_service.create_reservation(coraline, coraline_showtime2, "A1", user1)
reservation_service.create_reservation(coraline, coraline_showtime1, "B2", user2)
reservation_service.create_reservation(coraline, coraline_showtime2, "D6", user2)

DisplayService.display_seats_with_cli_color(coraline_showtime1)
print()
DisplayService.display_seats_with_cli_color(coraline_showtime2)
alphabetical_movie_list = movie_service.sort_by_alphabetical_order()
print(f"\nAll movies in this theatre:\n")
for movie in alphabetical_movie_list:
    print(movie)