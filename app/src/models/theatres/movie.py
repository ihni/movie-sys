class Movie:
    def __init__(self, title, theatre, showtime):
        self.title = title
        self.theatre = theatre
        self.showtime = showtime

    def __str__(self):
        return f"{self.title} at {self.theatre.name} - Showtime: {self.showtime}"