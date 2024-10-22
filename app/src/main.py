from config import *
from models import Movie
from models import Theatre

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

theatre.display_seats()