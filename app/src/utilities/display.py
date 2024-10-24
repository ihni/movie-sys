class DisplayService:
    @staticmethod
    def display_seats(showtime):
        print(f"Seating arrangement for {showtime.movie.title} at theatre {showtime.theatre.location} at {showtime.showtime}:")
        for i, row in enumerate(showtime.seats):
            print(f"Row {i + 1}: ", end="")
            for seat in row:
                print(seat.name, end=" ")
            print()

    @staticmethod
    def display_seats_with_cli_color(showtime):
        print(f"Seating arrangement for {showtime.movie.title} at theatre {showtime.theatre.location} at {showtime.showtime}:")
        for row in showtime.seats:
            for seat in row:
                color = '\x1b[6;30;42m' if seat.is_available else '\x1b[38;5;9m'
                print(color + seat.name + '\x1b[0m', end="  ")
            print()

    @staticmethod
    def display_movies_in_alphabetical_order(sorted_list):
        print(f"All movies in this theatre:\n")
        for movie in sorted_list:
            print(movie)

    @staticmethod
    def display_user_reservations(list_user_reservations):
        for reservation in list_user_reservations:
            print(reservation)