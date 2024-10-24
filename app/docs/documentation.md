## 10/17/2024 - Foundational Work(pre-program)
- created todo.md
- created folders to store different parts of the program
- this is to easily manage and create modular programming for ease of use, updates, and scalability.
- Aidan

## 10/23/2024
- **created basic models**
    - users
    - reservations(acts as a ticket)
    - seat
    - movie
    - showtime(properly format the YYYY-MM-DD HH:MM AM/PM)
    - theatre(takes in seat and movie module)
- **created basic services**
    - user service(deals with creating users and validating them)
    - reservation services(handles the booking process, checking for availability of seats and cancellations)
    - movie service to create a movie with all information needed
- I used a 2d array/matrix for dealing with the seats of a theatre where each element in the matrix is a seat object
    - reasoning is because a matrix properly represents the rows and columns of a seat in a theatre
    - seat availability can also be represented using boolean or 0s and 1s, if seat is not available, it's a 0, if it is, it's a 1
    - because of the nature of matrixes being a 2d array, i can easily implement the seat naming because on its position in the matrix. the row and column gives off the name
- Aidan

## 10/24/2024
- Merge Sort Algorithm
    - chose merge sort for the reason of scalability
    - although the space complexity is O(N), i prefer it the most because of its speed
    - main implementation so far is alphabetically sorting movies using this algorithm
    - I don't want users to wait for a while just to see a catalogue of their movies organized in alphabetical order
- **WIP**
    - binary search for movie titles
    - sort by showtime
    - theatre service
        - adding movies to a theatre
        - creating theatres
        - changing movies in a theatre
        - deleting theatres
- **Issues**
    - I need to decouple the seating from the theatre or atleast only attach the reservation TO THAT SPECIFIC MOVIE SHOWTIME
    - reason is because if movie was to replay, the seating reservation won't be removed for the future showtime
    - seating in the theatres should be attached to that specific showtime - endtime, at the moment, it does not care about what showtime you're attached to as if you decide to book in the same theatre at the same seat for the same movie but in a later show time, the seat will still be unavaible even though it's a brand new movie.
    - reserving should only be attached for that showtime, future showtimes should not have their seats taken for other showtimes
- Aidan

## 10/25/2024
- **fixed previous issues**
    - decoupled seatings so that showtimes represent seperate screenings.
    - this is done through creating a seperate showtime service
        - showtimes now handle seat reservations
        - showtimes take a copy of a theatre's seating arrangement
        - seatings are now seperate for each showtime and for each theatre
        - seatings should not interfere anymore with the next showtime
- seperated out display functions into utilities folder; modularity
- many attributes from movie is now decoupled, movie now only holds title, length, and its showtimes
- added theatre service
- implemented a movie queue to prevent users from reserving tickets for movies that are already finished
    - queues work best in this case because it's most similar to a playlist where one movie plays after the other and the ones that are finished are dequeued
- moved more cli displays into utilities folder
- **WIP**
    - binary search for movie titles
    - sort by showtime
- Aidan