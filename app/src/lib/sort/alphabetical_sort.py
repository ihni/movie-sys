'''
returns a list of movie names that are sorted alphabetically
- input is an unsorted list of movie names and must return a list
that is sorted alphabetically.
'''

# need a  comparison-based sorting algorithm.
# best for large database so once more and more movies are added to catalogue, it would be more useful
# simply brute forcing/naive approach would take forever or n^2

class AlphabeticalMovieNameSorter:
    def sort(self, unsorted_movies):
        sorted_movies = []
        return sorted_movies