from models import Movie
from .showtime_service import ShowtimeService

class MovieService:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)
    
    def remove_movie(self, movie):
        self.movies.remove(movie)

    def is_in_catalogue_by_title(self, searched_movie_title):
        for movie in self.movies:
            if movie.title == searched_movie_title:
                return True
        return False
    
    def create_movie(self, title, year, month_number, day, time, length):
        if self.is_in_catalogue_by_title(title):
            return False
        
        showtime_service = ShowtimeService()
        showtime = showtime_service.create_showtime(
            year = year,
            month_number = month_number,
            day = day,
            time = time
        )
        movie = Movie(title = title,
                      showtime = showtime,
                      length = length
        )
        self.add_movie(movie)
        return movie
    
    def lists_movies(self):
        return self.movies