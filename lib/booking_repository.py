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
        table = self._connection.execute("INSERT INTO bookings (booking_date, space_id, booking_user_id) VALUES (%s, %s, %s) RETURNING id", [booking.booking_date, booking.space_id, booking.booking_user_id])
        row = table[0]
        booking.id = row['id']
        return None


