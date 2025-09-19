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
    
    # def is_valid(self):
    #     return self.check_username_length() \
    #         and self.check_password_length() \
    #         and self.special_chars()

    # def check_booking_date_format(self):
    #     return len(self.username) >= 4 and len(self.username) <= 16


    

    def generate_errors(self):
        errors = []
        if not self.check_username_length():
            errors.append("username must be 4-16 characters in length")
        if not self.check_password_length() or not self.special_chars():
            errors.append("password must be 8-16 characters in length and contain a special character")
        if not self.check_passwords_match():
            errors.append("passwords do not match")
        if len(errors) > 0:
            return ", ".join(errors)
        return None

    
