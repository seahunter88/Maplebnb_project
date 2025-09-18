from lib.user import User
import hashlib

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
        if self.check_username_is_unique(user.username):
            table = self._connection.execute("INSERT INTO users (username, password) VALUES (%s, %s) RETURNING id", [user.username, user.password])
            row = table[0]
            user.id = row['id']
            return None
        return "Username is already in use."

    def find(self, username, password):
        hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
        table = self._connection.execute("SELECT id, username, password FROM users WHERE (username, password) = (%s, %s)", [username, hashed_password])

        if not table:
            return None
        row = table[0]
        if row is None:
            return None

        return User(row['id'], row['username'], row['password'])

    def check_username_is_unique(self, username):
        table = self._connection.execute("SELECT * FROM users WHERE username = %s", [username])
        return table == []



