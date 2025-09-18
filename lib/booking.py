class Booking:
    def __init__(self, id, booking_date, space_id, booking_user_id):
        self.id = id
        self.booking_date = booking_date
        self.space_id = space_id
        self.booking_user_id = booking_user_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f'Booking({self.id}, {self.booking_date}, {self.space_id}, {self.booking_user_id})'