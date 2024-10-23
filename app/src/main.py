from config import *
from models import Movie
from models import Theatre
from models import User
from services import UserService
from services import ReservationService

movie = Movie(
    title = "Coraline",
    theatre = "1",
    showtime = "1:00pm"
)

theatre = Theatre(
    movie = movie,
    location = ALL_THEATRE_LOCATIONS[0],
    total_rows = MAX_ROWS-1,
    total_columns = MAX_COLUMNS-2
)

user_service = UserService()
reservation_service = ReservationService()

user_1 = user_service.create_user(
    email = "test@gmail.com"
)
reservation = reservation_service.create_reservation(
    movie = movie,
    theatre = theatre,
    seat_name = "A1",
    user = user_1
)


#theatre.display_seats()
theatre.display_seats_with_cli_color()
print(theatre.avaible_seats_list())