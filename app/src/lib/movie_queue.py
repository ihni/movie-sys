class MovieQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, movie):
        if not self.queue:
            self.queue.append(movie)
            return

        earliest_showtime = None
        for showtime in movie.showtimes:
            if earliest_showtime is None or showtime.showtime < earliest_showtime.showtime:
                earliest_showtime = showtime

        for idx, current_movie in enumerate(self.queue):
            current_earliest_showtime = None
            for showtime in current_movie.showtimes:
                if current_earliest_showtime is None or showtime.showtime < current_earliest_showtime.showtime:
                    current_earliest_showtime = showtime

            if earliest_showtime.showtime < current_earliest_showtime.showtime:
                self.queue.insert(idx, movie)
                return
        self.queue.append(movie)

    def dequeue(self):
        if self.is_empty():
            return False
        movie = self.queue.pop(0)
        return movie

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def rotate(self):
        self.enqueue(self.dequeue())

    def is_empty(self):
        return True if not self.queue else False
    
    def size(self):
        return len(self.queue)
    
    def __str__(self):
        display_str = []
        for movie in self.queue:
            display_str.append(f"- {movie.title} (Showtime: {movie.showtime})")

        display_str = "\n".join(display_str)
        return f"Movie Queue:\n{display_str}"