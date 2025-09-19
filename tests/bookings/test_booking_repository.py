from lib.bookings.booking_repository import BookingRepository
from lib.bookings.booking import Booking
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

'''
when we call @read_bookings_one_space with a space_id
it returns all the bookings associated with that space_id.
'''

def test_read_bookings_one_space_returns_correct_bookings_1(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = BookingRepository(db_connection)
    results = repo.read_bookings_one_space(1)
    assert results == [
        Booking(1, date(2025, 9, 17), 1, 1)
    ]
    
'''
when we call @read_bookings_one_space with a space_id
it returns all the bookings associated with that space_id.
'''

def test_read_bookings_one_space_returns_correct_bookings_2(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = BookingRepository(db_connection)
    results = repo.read_bookings_one_space(2)
    assert results == [
        Booking(2, date(2025, 8, 17), 2, 2)
    ]
    
'''
when we create a new booking and
when we call @read_bookings_one_space with a space_id
it returns all the bookings associated with that space_id.
'''

def test_create_booking_then_read_bookings_one_space(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = BookingRepository(db_connection)
    booking = Booking(3, '2025-10-15', 1, 2)
    repo.create(booking)
    results = repo.read_bookings_one_space(1)
    assert results == [
        Booking(1, date(2025, 9, 17), 1, 1),
        Booking(3, date(2025, 10, 15), 1, 2)
    ]

'''
when we call @read_bookings_one_user with a user_id
it returns all the bookings associated with that user_id.
'''

def test_read_bookings_one_user_returns_correct_bookings_1(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = BookingRepository(db_connection)
    results = repo.read_bookings_one_user(1)
    assert results == [
        Booking(1, date(2025, 9, 17), 1, 1)
    ]

'''
when we call @read_bookings_one_user with a user_id
it returns all the bookings associated with that user_id.
'''

def test_read_bookings_one_user_returns_correct_bookings_2(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = BookingRepository(db_connection)
    results = repo.read_bookings_one_user(2)
    assert results == [
        Booking(2, date(2025, 8, 17), 2, 2)
    ]

'''
when we create a new booking and
when we call @read_bookings_one_user with a user_id
it returns all the bookings associated with that user_id.
'''

def test_create_booking_then_read_bookings_one_user(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = BookingRepository(db_connection)
    booking = Booking(3, '2025-10-15', 1, 2)
    repo.create(booking)
    results = repo.read_bookings_one_user(2)
    assert results == [
        Booking(2, date(2025, 8, 17), 2, 2),
        Booking(3, date(2025, 10, 15), 1, 2)
    ]

'''
when we create a new booking with an earlier date and
when we call @read_bookings_one_user with a user_id
it returns all the bookings associated with that user_id
ORDERED by date, ascending order.
'''

def test_read_bookings_one_user_orders_by_date(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = BookingRepository(db_connection)
    booking = Booking(3, '2025-01-15', 1, 2)
    repo.create(booking)
    results = repo.read_bookings_one_user(2)
    assert results == [
        Booking(3, date(2025, 1, 15), 1, 2),
        Booking(2, date(2025, 8, 17), 2, 2)
    ]

    
'''
when we create a new booking that is not a duplicate,
check_bookings_unique returns true
'''

def test_check_bookings_unique_returns_true_for_unique_bookings(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = BookingRepository(db_connection)
    booking_1 = Booking(3, '2025-10-15', 1, 2)
    assert repo.check_booking_is_unique(booking_1) == True
    
'''
when we create a new booking that is not a duplicate,
check_bookings_unique returns true
'''

def test_check_bookings_unique_returns_true_for_unique_bookings_2(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = BookingRepository(db_connection)
    booking_1 = Booking(3, '2025-10-15', 2, 2)
    assert repo.check_booking_is_unique(booking_1) == True
    
'''
when we create a new booking that is not a duplicate,
check_bookings_unique returns true
'''

def test_check_bookings_unique_returns_true_for_unique_bookings_3(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = BookingRepository(db_connection)
    booking_1 = Booking(3, '2025-08-17', 1, 2)
    assert repo.check_booking_is_unique(booking_1) == True
    
'''
when we create a new booking that IS a duplicate,
check_bookings_unique returns false
'''

def test_check_bookings_unique_returns_false_for_unique_bookings(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = BookingRepository(db_connection)
    booking_1 = Booking(3, '2025-08-17', 2, 2)
    assert repo.check_booking_is_unique(booking_1) == False
    
'''
when we create a new booking that IS a duplicate,
with a different user_id
check_bookings_unique returns false
'''

def test_check_bookings_unique_returns_false_for_unique_bookings_2(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = BookingRepository(db_connection)
    booking_1 = Booking(3, '2025-08-17', 2, 1)
    assert repo.check_booking_is_unique(booking_1) == False
    
'''
when we create a new booking that IS a duplicate,
and use the @create method
check_bookings_unique will return false
create does not add to database
we cannot see the new booking from the @all method
'''

def test_create_bookings_uses_check_booking_unique(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = BookingRepository(db_connection)
    booking_1 = Booking(3, '2025-09-17', 1, 1)
    assert repo.check_booking_is_unique(booking_1) == False
    assert repo.all() == [
        Booking(1, date(2025, 9, 17), 1, 1),
        Booking(2, date(2025, 8, 17), 2, 2)
    ]
    
    
'''
if a booking is a duplicate, we get a string from generate_errors()
'''

def test_generate_errors_returns_string(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = BookingRepository(db_connection)
    booking_1 = Booking(1, '2025-09-17', 1, 1)
    assert repo.check_booking_is_unique(booking_1) == False
    assert repo.generate_errors(booking_1) == "Unfortunately this space is being used for a Pokemon convention on that date, please try a different date."
    
'''
if a booking is NOT a duplicate, we do not get a string from generate_errors()
'''

def test_generate_errors_does_not_return_string(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = BookingRepository(db_connection)
    booking_1 = Booking(1, '2025-09-19', 1, 1)
    assert repo.check_booking_is_unique(booking_1) == True
    assert repo.generate_errors(booking_1) == None
    
'''
if a user_id exists in the db then @check_user_id_exists returns True
'''

def test_check_user_id_returns_true_for_existing_user(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = BookingRepository(db_connection)
    booking_1 = Booking(1, '2025-09-19', 1, 1)
    assert repo.check_user_id_exists(booking_1) == True
    
'''
if a user_id does NOT exist in the db then @check_user_id_exists returns False
'''

def test_check_user_id_returns_false_for_nonexisting_user(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = BookingRepository(db_connection)
    booking_1 = Booking(1, '2025-09-19', 1, 8)
    assert repo.check_user_id_exists(booking_1) == False
    
'''
if a user tries to make a booking (with a unique date) 
with a user id that does not exist
we get an error message specific to the user not existing
'''

def test_generate_errors_returns_string_for_invalid_user_id(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = BookingRepository(db_connection)
    booking_1 = Booking(1, '2025-09-20', 1, 8)
    assert repo.check_user_id_exists(booking_1) == False
    assert repo.generate_errors(booking_1) == "Are you sure this is your user ID? We cannot find it round the back."
    
'''
if a user tries to make a booking that is a duplicate
with a user id that does not exist
we get an error message specific to the user not existing AND the booking being a duplicate
'''

def test_generate_errors_returns_string_for_invalid_user_id_and_duplicate_booking(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = BookingRepository(db_connection)
    booking_1 = Booking(1, '2025-09-17', 1, 8)
    assert repo.check_user_id_exists(booking_1) == False
    assert repo.generate_errors(booking_1) == "Unfortunately this space is being used for a Pokemon convention on that date, please try a different date.<br>Are you sure this is your user ID? We cannot find it round the back."
    