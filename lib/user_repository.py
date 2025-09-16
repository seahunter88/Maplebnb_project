from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        table = self._connection.execute("SELECT * FROM users")
        return [
            User(row["id"], row["username"], row["password"])
            for row in table
            ]
        
    def create(self, user):
        table = self._connection.execute("INSERT INTO users (username, password) VALUES (%s, %s)", [user.username, user.password])
        return user

