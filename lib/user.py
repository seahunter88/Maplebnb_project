class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f'User({self.id}, {self.username}, {self.password})'

# @is_valid returns false if any of the other methods return false
# if all the methods are true then is_valid returns true
    def is_valid(self):
        return self.check_username_length() \
            and self.check_password_length() \
            and self.special_chars()
    
    def check_username_length(self):
        return len(self.username) >= 4 and len(self.username) <= 16
    
    def check_password_length(self):
        return len(self.password) >= 8 and len(self.password) <= 16
    
    def special_chars(self):
        special_chars = '!@$%&'
        return any(char in self.password for char in special_chars)
    
    def generate_errors(self):
        errors = []
        if self.username == None or self.username == "":
            errors.append("username cannot be blank")
        if self.password == None or self.password == "" or not self.check_password_length() or not self.special_chars():
            errors.append("password must be at least 8 characters long and have a special character")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)