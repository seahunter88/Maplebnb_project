from lib.booking import Booking

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
    
