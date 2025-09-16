from lib.users_repository import UserRepository
from lib.users import User

'''
we can instantiate the user repository
'''

def test_instantiates(db_connection):
    repo = UserRepository(db_connection)
    assert isinstance(repo, UserRepository)


'''
when we call @all, returns a list of all users
'''

def test_all_returns_all_users(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = UserRepository(db_connection)
    results = repo.all()
    assert results == [
        User(1, 'Sarahmonster9000', 'Iloveponies!'),
        User(2, 'HunoristheGOAT', 'Pokemon$')
    ]

'''
when we call @create, we can add a user to the database
'''

def test_create_user_adds_user_to_database(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = UserRepository(db_connection)
    user = User(3, 'Username', 'Password!')
    repo.create(user)
    results = repo.all()
    assert results == [
        User(1, 'Sarahmonster9000', 'Iloveponies!'),
        User(2, 'HunoristheGOAT', 'Pokemon$'),
        User(3, 'Username', 'Password!')
    ]

