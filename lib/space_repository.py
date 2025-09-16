from lib.space import Space

class SpaceRepository():
    def __init__(self, connection):
        self._connection = connection

    def read_all_spaces(self):
        rows = self._connection.execute('SELECT * FROM spaces')
        return [
            Space(row['id'], row['title'], row['price'], row['description'], row['user_id'])
            for row in rows
        ]
    
    def read_one_space(self, space_id):
        rows = self._connection.execute('SELECT * FROM spaces where id = %s', [space_id])
        row = rows[0]
        return Space(row['id'], row['title'], row['price'], row['description'], row['user_id'])
