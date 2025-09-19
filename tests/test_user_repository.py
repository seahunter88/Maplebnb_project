from lib.user_repository import UserRepository
from lib.user import User

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

'''
when we call @find, we read a user from the database
'''

def test_find_user_reads_user_from_database(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = UserRepository(db_connection)
    results = repo.find('Sarahmonster9000', 'Iloveponies!')
    assert results == User(1, 'Sarahmonster9000', 'Iloveponies!')

'''
when we create a user, if the username is already in the database then it will show an error saying that the username is already in use
'''

def test_create_user_shows_error_when_username_is_not_unique(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = UserRepository(db_connection)
    user_1 = User(1, 'Username123', 'Password!', 'Password!')
    user_2 = User(2, 'Username123', 'Password123!', 'Password123!')
    repo.create(user_1)
    result = repo.create(user_2)
    assert result == "Username is already in use."

'''
@read_one_user returns a user object given the correct id
'''

def test_read_one_user_returns_correct_user(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = UserRepository(db_connection)
    assert repo.read_one_user(1) == User(1, 'Sarahmonster9000', 'Iloveponies!')
    

'''
@read_one_user returns a user object given the correct id
'''

def test_read_one_user_returns_correct_user_2(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = UserRepository(db_connection)
    assert repo.read_one_user(2) == User(2, 'HunoristheGOAT', 'Pokemon$')
    
'''
@get_user_id returns an id from a given User object
'''

def test_get_user_id_returns_id(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = UserRepository(db_connection)
    user_1 = User(3, 'Username123', 'Password!', 'Password!')
    assert repo.get_user_id(user_1) == 3
    

