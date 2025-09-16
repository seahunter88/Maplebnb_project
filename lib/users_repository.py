from lib.users import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        table = self._connection.execute("SELECT * FROM users")
        return [
            User(row["id"], row["username"], row["password"])
            for row in table
            ]

