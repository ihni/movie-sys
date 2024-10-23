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
    