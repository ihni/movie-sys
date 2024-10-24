from config import *
from models import Theatre
from services import UserService
from services import ReservationService
from services import MovieService


user_service = UserService()
reservation_service = ReservationService()
movie_service = MovieService()

'''TEST DATA'''
coraline = movie_service.create_movie(
    title = "Coraline",
    year = "2009",
    month_number = 2,
    day = 6,
    time = "12:00 PM",
    length = 115
)

spirited_away = movie_service.create_movie(
    title = "Spirited Away",
    year = "2001",
    month_number = 7,
    day = 20,
    time = "3:30 PM",
    length = 125
)

chipmunks = movie_service.create_movie(
    title = "Alvin and the Chipmunks",
    year = "2007",
    month_number = 12,
    day = 14,
    time = "6:30 PM",
    length = 92
)

pirates_carribean = movie_service.create_movie(
    title = "Pirates of the Caribbean",
    year = "2003",
    month_number = 7,
    day = 9,
    time = "10:00 PM",
    length = 143
)

theatre = Theatre(
    location = ALL_THEATRE_LOCATIONS[0],
    total_rows = MAX_ROWS,
    total_columns = MAX_COLUMNS-2
)

theatre.add_movie(coraline)
theatre.add_movie(spirited_away)
theatre.add_movie(chipmunks)
theatre.add_movie(pirates_carribean)

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
#print(theatre.avaible_seats_list())

sorted_list = movie_service.sort_by_alphabetical_order()
print(f"\nAll movies in this theatre:\n")
for movie in sorted_list:
    print(movie)