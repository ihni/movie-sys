from models import Theatre

class TheatreService:
    def __init__(self):
        self.theatres = []

    def add_theatre(self, theatre):
        self.theatres.append(theatre)

    def delete_theatre(self, theatre):
        if theatre in self.theatres:
            self.theatres.remove(theatre)
            return True
        return False
    
    def create_theatre(self, location, total_rows, total_columns) -> object:
        theatre = Theatre(location, total_rows, total_columns)
        self.add_theatre(theatre)
        return theatre
    
    def add_movie_to_theatre(self, theatre, movie):
        if movie not in theatre.movies:
            theatre.add_movie(movie)
    
    def get_movies_by_theatre(self, theatre) -> list:
        '''Returns a list of movies showing in the theatre.'''
        for theatre_in_list in self.theatres:
            if theatre_in_list == theatre:
                return theatre_in_list.movies
        return []