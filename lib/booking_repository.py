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
        
    # def create(self, booking):
    #     table = self._connection.execute("INSERT INTO bookings (bookingname, password) VALUES (%s, %s) RETURNING id", [booking.bookingname, booking.password])
    #     row = table[0]
    #     booking.id = row['id']
    #     return None


