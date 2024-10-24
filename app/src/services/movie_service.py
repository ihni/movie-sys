from models import Movie
from lib import MergeSort
from .showtime_service import ShowtimeService

class MovieService:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)
    
    def remove_movie(self, movie):
        self.movies.remove(movie)

    def sort_by_alphabetical_order(self) -> list:
        '''
        returns a list of sorted movie objects based on the title
        time complexity is O(n*logn)
        creates a list of sorted titles and then a dictionary with key titles and value movie objects
        third list contains the sorted movie objects where i match the sorted titles as the key in the dictionary and store the objects
        '''
        sorter = MergeSort()
        unsorted_titles = [movie.title for movie in self.movies]
        sorted_titles = sorter.merge_sort(unsorted_titles)
        title_to_movie = {movie.title:movie for movie in self.movies}

        sorted_movie_objects = []
        for title in sorted_titles:
            sorted_movie_objects.append(title_to_movie[title])

        return sorted_movie_objects

    
    def sort_by_showtime(self) -> list:
        '''returns a list of movies based on the newest showtime'''
        pass

    def is_in_catalogue_by_title(self, searched_movie_title) -> bool:
        for movie in self.movies:
            if movie.title == searched_movie_title:
                return True
        return False
    
    def create_movie(self, title, year, month_number, day, time, length) -> object:
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