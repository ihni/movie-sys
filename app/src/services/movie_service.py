from models import Movie
from lib import MergeSort

class MovieService:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)
    
    def remove_movie(self, movie):
        self.movies.remove(movie)

    def search_movie_by_partial_title(self, partial_title) -> list:
        '''
        returns a list of all movies where partial title is inside movie title
        '''
        matching_movies = []
        for movie in self.movies:
            if partial_title.lower() in movie.title.lower():
                matching_movies.append(movie)
        return matching_movies

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
    
    def create_movie(self, title, length) -> object:
        if self.is_in_catalogue_by_title(title):
            return False
        
        movie = Movie(title=title, length=length)
        self.add_movie(movie)
        return movie
    
    def lists_movies(self):
        return self.movies