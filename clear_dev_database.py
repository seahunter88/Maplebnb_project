from lib.database_connection import DatabaseConnection

# Run this file to clear your database 


connection = DatabaseConnection(test_mode=False)
connection.connect()
connection.execute('DELETE FROM users;')
connection.execute('DELETE FROM spaces;')
connection.execute('DELETE FROM bookings;')

