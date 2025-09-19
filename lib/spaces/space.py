class Space():
    def __init__(self, id, title, price, description, user_id):
        self.id = id
        self.title = title
        self.price = price
        self.description = description
        self.user_id = user_id

    def __eq__(self,other):
        return self.__dict__ == other.__dict__  
    
    def __repr__(self):
        return f"Space({self.id}, {self.title}, {self.price}, {self.description}, {self.user_id})"
    
    def is_valid(self):
        return self.check_title() \
            and self.check_price() \
            and self.check_description()

    def check_title(self):
        return len(self.title) >= 4 and len(self.title) <= 100
    
    def check_price(self):
        return isinstance(self.price, int) and self.price >= 20
    
    def check_description(self):
        return isinstance(self.description, str) and len(self.description.split()) >= 3
    
    def generate_errors(self):
        errors = []
        if not self.check_title():
            errors.append("title must be 4-20 characters in length")
        if not self.check_price():
            errors.append("price must be at least 20")
        if not self.check_description():
            errors.append("a description must be at least 3 words in length")
        if len(errors) > 0:
            return errors
        return None