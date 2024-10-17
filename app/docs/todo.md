# Movie Ticket Booking System

## Final Project
- Final Exam -> (Laboratory)
- 10-minute explanation
- Explain the data structure and algorithms used
- **Documentation**: Create a user manual in README.md
- document any changes and WHY in documentation.md for presentation showcase & summar
- **Version Control**: Set up a Git repository

## Project Breakdown
- **Core Components**:
  - **Ticket**: Central to the program
  - **Reservation System**: Handles all tickets
  - **Movies**: Users can select from a catalogue of movies
  - **Seating System**: Manages seating arrangements
  - **Theatre System**: Provides location and management of theatres
- **Data Storage**:
  - All information stored in separate Excel files
  - Use pandas for handling dataframes and Excel operations
  - In the future, expect modules to be handled by tkinter -> GUI approach

## Data Models

### Movie
- Attributes:
  - name
  - length (in minutes)
  - rating (e.g., PG, R) or (e.g., out of 10, or 5 stars)
  - showtimes (list of (date, time))

### Ticket
- Attributes:
  - name
  - email
  - seat
  - theatre location
  - movie (reference to Movie object)
  - date + time of movie reservation

### Reservation
- Attributes:
  - user (reference to User object)
  - tickets (list of Ticket objects)

## Reservation System
- **Functions**:
  - Authenticate based on name and email
  - Create tickets
  - Prevent ticket creation if no seats are left
  - Check for duplicate tickets and raise errors before creation
  - **Reservation History**: Allow users to view past reservations
  - **Cancellation System**: Enable users to cancel their reservations

## Theatre System
- **Functions**:
  - Manage systems for each theatre
  - Provide location and details of movies showcased
  - Add scalability for more flexibility when adding custom seats
  - **Seating Map**: Visual representation of available and reserved seats

## Catalogue of Movies
- **Functions**:
  - Display all movies alphabetically
  - Display movies by genre
  - **Search Functionality**: Allow searching by title, genre, or rating
  - **Movie Details**: Provide information

## Admin Utilities
- **Functions**:
  - Admin authentication system for managing movies
  - Add/remove movies from the catalogue
  - **Logging Changes**: Maintain a log of admin actions

## Data Management
- **Data Files**:
  - Separate Excel files for Users, Movies, and Reservations
- **Backup System**: Plan for regular backups of Excel files
- **Data Validation**: Implement validation for data read/write operations

```
movie_ticket_booking_system/
│
├── src/                            # Source code in directory
│   ├── __init__.py                 # Package initialization
│   ├── main.py                     # Entry point
│   ├── models/                     # Classes => pure representation of data, no functions please
│   │   ├── __init__.py             # Package initialization
│   │   ├── user.py                 # User model
│   │   ├── movie.py                # Movie model
│   │   ├── ticket.py               # Ticket model
│   │   └── reservation.py          # Reservation model
│   │
│   ├── services/                  # Core functionality of the program, interacts with models to give functionality
│   │   ├── __init__.py            # Package initialization
│   │   ├── user_service.py        # User-related services
│   │   ├── movie_service.py       # Movie-related services
│   │   └── booking_service.py     # Booking-related services
│   │
│   ├── controllers/               # Controllers for managing flow of program
│   │   ├── __init__.py            # Package initialization
│   │   ├── user_controller.py      # User management logic
│   │   ├── movie_controller.py     # Movie catalog management
│   │   └── booking_controller.py   # Ticket booking management
│   │
│   ├── utils/                     # Utility functions and helpers
│   │   ├── __init__.py            # Package initialization
│   │   ├── utilities.py              # General helper functions
│   │   └── excel_handler.py        # Module for handling Excel operations
│   │
│   ├── lib/                       # library for packages that are imported
│   │   └── __init__.py            # Package initialization
│   │
│   └── config.py                  # Configuration settings
│
├── data/                          # Data storage and backups
│   ├── users.xlsx                 # Excel file for user data
│   ├── movies.xlsx                # Excel file for movie data
│   ├── ..... . xlsx               # add one possibly for the seat plan of each theatre 
│   └── reservations.xlsx           # Excel file for reservation data(logs of ALL previous/current reservations)
│
├── backups/                       # Backup directory for Excel files
│   └── ...                        # Backup files will be stored here
│
├── docs/                          # Documentation directory
│   ├── README.md                  # Project overview and user manual
│   └── documentation.md           # Documentation of changes and processes
│
└── .gitignore                     # Git ignore file for untracked files
```

## Implement Data Structures and Algorithms
- **Data Structures**
  - Stacks for user reservations
  - stacks can push a reservation and undo most recent reservation
  - Hashmaps for storing UID or user information
- **Algorithms**
  - Binary search for searching through Movie titles(sorted list)
  - Sort Movies in a list using Merge Sort
    - Reasoning:
      - Scalability: Best for when Datasets get large
      - Time Complexity: O(n log n)
      - Space Complexity: O(n) because of additional memory needed for mergin
      - Con: requires a lot of memory if datasets are big