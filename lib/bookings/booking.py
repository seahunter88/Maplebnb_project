from datetime import datetime

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
    
    def is_valid(self):
        return self.check_booking_date_format('%Y-%m-%d')

    def check_booking_date_format(self, date_format):
        try:
            datetime.strptime(self.booking_date, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def generate_errors(self):
        errors = []
        if not self.check_booking_date_format('%Y-%m-%d'):
            errors.append("The booking date must be in the format YYYY-MM-DD")
        if len(errors) > 0:
            return ", ".join(errors)
        return None
