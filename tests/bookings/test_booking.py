from lib.bookings.booking import Booking

'''
When we construct a booking, it has an id, booking_date, booking_user_id and space_id,
'''

def test_booking_constructs_with_properties():
    booking = Booking(1, '2025-09-17', 1, 1)
    assert booking.id == 1
    assert booking.booking_date == '2025-09-17'
    assert booking.space_id == 1
    assert booking.booking_user_id == 1
    

'''
booking objects are treated equally if they have equal values
'''

def test_equality():
    booking_1 = Booking(1, '2025-09-17', 1, 1)
    booking_2 = Booking(1, '2025-09-17', 1, 1)
    assert booking_1 == booking_2

'''
booking objects are formatted as a nice string
'''

def test_booking_formats_nicely_as_a_string():
    booking_1 = Booking(1, '2025-09-17', 1, 1)
    assert str(booking_1) == 'Booking(1, 2025-09-17, 1, 1)'
    
'''
@check_booking_date_format returns true if booking date format is correct
'''

def test_check_booking_date_returns_true():
    booking_1 = Booking(1, '2025-09-17', 1, 1)
    assert booking_1.check_booking_date_format('%Y-%m-%d') == True

'''
@check_booking_date_format returns false if booking date format is incorrect
'''

def test_check_booking_date_returns_false():
    booking_1 = Booking(1, '2025-07', 1, 1)
    assert booking_1.check_booking_date_format('%Y-%m-%d') == False
    
'''
@check_booking_date_format returns false if booking date format is incorrect
'''

def test_check_booking_date_returns_false_2():
    booking_1 = Booking(1, 'hello', 1, 1)
    assert booking_1.check_booking_date_format('%Y-%m-%d') == False
    

'''
@is_valid returns false if booking date format is incorrect
'''

def test_is_valid_returns_false():
    booking_1 = Booking(1, '2025-07', 1, 1)
    assert booking_1.is_valid() == False
    
'''
@is_valid returns true if booking date format is correct
'''

def test_is_valid_returns_true():
    booking_1 = Booking(1, '2025-07-10', 1, 1)
    assert booking_1.is_valid() == True
    
'''
@generate_errors returns string if booked date is not in the right format
'''

def test_generate_errors_return_string_for_invalid_booking_date():
    booking_1 = Booking(1, '2025-0710', 1, 1)
    assert booking_1.generate_errors() == 'The booking date must be in the format YYYY-MM-DD'
    
'''
@generate_errors returns None if booked date is in the right format
'''

def test_generate_errors_return_none_for_valid_booking_date():
    booking_1 = Booking(1, '2025-07-10', 1, 1)
    assert booking_1.generate_errors() == None
    

    
    

    
    
