from lib.booking import Booking

class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        table = self._connection.execute("SELECT * FROM bookings")
        return [
            Booking(row["id"], row["booking_date"], row["space_id"], row["booking_user_id"])
            for row in table
            ]
        
    def create(self, booking):
        if self.check_booking_is_unique(booking):
            table = self._connection.execute("INSERT INTO bookings (booking_date, space_id, booking_user_id) VALUES (%s, %s, %s) RETURNING id", [booking.booking_date, booking.space_id, booking.booking_user_id])
            row = table[0]
            booking.id = row['id']
            return None
        return None

    
    def check_booking_is_unique(self, booking):
        table = self._connection.execute("SELECT * FROM bookings WHERE booking_date = %s AND space_id = %s", [booking.booking_date, booking.space_id])
        return table == []
    
    def generate_errors(self, booking):
        errors = []
        if not self.check_booking_is_unique(booking):
            errors.append("Unfortunately this space is being used for a Pokemon convention on that date, please try a different date.")
        if len(errors) > 0:
            return ", ".join(errors)
        return None
    
    
    def read_bookings_one_space(self, space_id):
        table = self._connection.execute("SELECT * FROM bookings WHERE space_id = %s", [space_id])
        return [
            Booking(row["id"], row["booking_date"], row["space_id"], row["booking_user_id"])
            for row in table
            ]

    def read_bookings_one_user(self, user_id):
        table = self._connection.execute("SELECT * FROM bookings WHERE booking_user_id = %s ORDER BY booking_date ASC", [user_id])
        return [
            Booking(row["id"], row["booking_date"], row["space_id"], row["booking_user_id"])
            for row in table
            ]
