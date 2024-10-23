from config import *
from models import Theatre
from services import UserService
from services import ReservationService
from services import MovieService


user_service = UserService()
reservation_service = ReservationService()
movie_service = MovieService()

'''
TEST DATA
'''

coraline = movie_service.create_movie(
    title = "Coraline",
    year = "2009",
    month_number = 2,
    day = 6,
    time = "12:00 PM",
    length = 115
)

theatre = Theatre(
    location = ALL_THEATRE_LOCATIONS[0],
    total_rows = MAX_ROWS,
    total_columns = MAX_COLUMNS-2
)

theatre.add_movie(coraline)

user_1 = user_service.create_user(
    email = "test@gmail.com"
)
user_2 = user_service.create_user(
    email = "fake@gmail.com"
)

reservation_service.create_reservation(
    movie = coraline,
    theatre = theatre,
    seat_name = "A1",
    user = user_1
)

reservation_service.create_reservation(
    movie = coraline,
    theatre = theatre,
    seat_name = "A3",
    user = user_2
)

#theatre.display_seats()
theatre.display_seats_with_cli_color()
print(theatre.avaible_seats_list())
print(coraline)