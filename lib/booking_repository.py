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
        if self.check_booking_is_unique()
        table = self._connection.execute("INSERT INTO bookings (booking_date, space_id, booking_user_id) VALUES (%s, %s, %s) RETURNING id", [booking.booking_date, booking.space_id, booking.booking_user_id])
        row = table[0]
        booking.id = row['id']
        return None
    
    def check_booking_is_unique(self, booking):
        table = self._connection.execute("SELECT * FROM bookings WHERE booking_date = %s AND space_id = %s", [booking.booking_date, booking.space_id])
        return table == []
    
    # def create(self, user):
    #     if self.check_username_is_unique(user.username):
    #         table = self._connection.execute("INSERT INTO users (username, password) VALUES (%s, %s) RETURNING id", [user.username, user.password])
    #         row = table[0]
    #         user.id = row['id']
    #         return None
    #     return "Username is already in use."
    
    # def check_username_is_unique(self, username):
    #     table = self._connection.execute("SELECT * FROM users WHERE username = %s", [username])
    #     return table == []
    
    def read_bookings_one_space(self, space_id):
        table = self._connection.execute("SELECT * FROM bookings WHERE space_id = %s", [space_id])
        return [
            Booking(row["id"], row["booking_date"], row["space_id"], row["booking_user_id"])
            for row in table
            ]

    def read_bookings_one_user(self, user_id):
        table = self._connection.execute("SELECT * FROM bookings WHERE booking_user_id = %s", [user_id])
        return [
            Booking(row["id"], row["booking_date"], row["space_id"], row["booking_user_id"])
            for row in table
            ]
