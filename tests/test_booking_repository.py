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

# '''
# when we call @create, we can add a booking to the database
# '''

# def test_create_booking_adds_booking_to_database(db_connection):
#     db_connection.seed('seeds/maplebnb.sql')
#     repo = BookingRepository(db_connection)
#     booking = booking(3, 'bookingname', 'Password!')
#     repo.create(booking)
#     results = repo.all()
#     assert results == [
#         booking(1, 'Sarahmonster9000', 'Iloveponies!'),
#         booking(2, 'HunoristheGOAT', 'Pokemon$'),
#         booking(3, 'bookingname', 'Password!')
#     ]


