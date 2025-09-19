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
        if not self.check_username_is_unique(user.username):
            raise Exception("Username is already in use.")

        if not user.password:
            raise Exception("Password cannot be blank.")

        hashed_password = hashlib.sha256(user.password.encode("utf-8")).hexdigest()
        table = self._connection.execute("INSERT INTO users (username, password) VALUES (%s, %s) RETURNING id", [user.username, hashed_password])
        row = table[0]
        user.id = row['id']
        return None

    def find(self, username, password):
        hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
        table = self._connection.execute("SELECT id, username, password FROM users WHERE (username, password) = (%s, %s)", [username, hashed_password])

        if not table:
            return None
        row = table[0]
        if row is None:
            return None

        return User(row['id'], row['username'], row['password'])
    
    def read_one_user(self, user_id):
        rows = self._connection.execute('SELECT * FROM users where id = %s', [user_id])
        row = rows[0]
        return User(row['id'], row['username'], row['password'])
    
    def get_user_id(self, user):
        return user.id

    def check_username_is_unique(self, username):
        table = self._connection.execute("SELECT * FROM users WHERE username = %s", [username])
        return table == []



