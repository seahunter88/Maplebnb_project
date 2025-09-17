from lib.space_repository import SpaceRepository
from lib.space import Space

'''
Testing read_all_spaces method returns all Spaces from the DB
'''
def test_read_all_spaces(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = SpaceRepository(db_connection)
    spaces = repo.read_all_spaces()
    assert spaces == [
        Space(1, 'House_1', 100, 'a nice house', 1),
        Space(2, 'House_2', 150, 'a nicer house', 1)
    ]

"""
Testing read_one_space method returns specified space
"""
def test_read_one_space(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = SpaceRepository(db_connection)
    space = repo.read_one_space(1)
    assert space == Space(1, 'House_1', 100, 'a nice house', 1)

"""
We can create a space with a Title, Price, Description, and a owner/user_id
"""
def test_create_space(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = SpaceRepository(db_connection)
    new_space = Space(None, "House_3", 50, "a not so nice house", 2)
    repo.create_space(new_space)
    space = repo.read_one_space(3)
    assert space == Space(3, 'House_3', 50, 'a not so nice house', 2)