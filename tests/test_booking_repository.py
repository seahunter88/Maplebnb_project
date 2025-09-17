from lib.booking_repository import BookingRepository
from lib.booking import Booking
from datetime import date


'''
we can instantiate the booking repository
'''

def test_instantiates(db_connection):
    repo = BookingRepository(db_connection)
    assert isinstance(repo, BookingRepository)


'''
when we call @all, returns a list of all bookings
'''

def test_all_returns_all_bookings(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = BookingRepository(db_connection)
    results = repo.all()
    assert results == [
        Booking(1, date(2025, 9, 17), 1, 1),
        Booking(2, date(2025, 8, 17), 2, 2)
    ]

'''
when we call @create, we can add a booking to the database
when we instantiate a booking, the date must be a string with the format 'YYYY-MM-DD' but
in the tests, the date must be in the format date(YYYY, MM (with no leading zeroes), DD)
'''

def test_create_booking_adds_booking_to_database(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = BookingRepository(db_connection)
    booking = Booking(3, '2025-10-15', 1, 2)
    repo.create(booking)
    results = repo.all()
    assert results == [
        Booking(1, date(2025, 9, 17), 1, 1),
        Booking(2, date(2025, 8, 17), 2, 2),
        Booking(3, date(2025, 10, 15), 1, 2)
    ]


