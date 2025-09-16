class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f'User({self.id}, {self.username}, {self.password})'

    def is_valid(self):
        if self.username == None or self.username == "":
            return False
        if self.password == None or self.password == "":
            return False
        if self.check_length() == False:
            return False
        if self.special_chars() == False:
            return False
        return True
    
    def special_chars(self):
        special_chars = '!@$%&'
        return any(char in self.password for char in special_chars)
    
    def check_length(self):
        if len(self.password) < 8:
            return False
        else:
            return True

    def generate_errors(self):
        errors = []
        if self.username == None or self.username == "":
            errors.append("Username cannot be blank")
        if self.password == None or self.password == "":
            errors.append("Password cannot be blank")
        # if self.check_length() == False:
        #     errors.append("Password must be at least 8 characters long")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)