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