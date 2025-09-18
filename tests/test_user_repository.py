from lib.user_repository import UserRepository
from lib.user import User
import hashlib

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
        User(1, 'Sarahmonster9000', '7aed73f28e36516d6b1af81271bccdc732b5abf3e17b5a56acda5a7a13f30dc3'),
        User(2, 'HunoristheGOAT', '39d4b14056843a7719d9612663b05e6d6bbe5db862fa944394bc4c205a8b0ab8')
    ]

'''
when we call @create, we can add a user to the database
'''

def test_create_user_adds_user_to_database(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = UserRepository(db_connection)
    raw_password = "Password!"
    hashed_password = hashlib.sha256('Password!'.encode("utf-8")).hexdigest()
    user = User(3, 'Username', raw_password)
    repo.create(user)
    results = repo.all()
    assert results == [
        User(1, 'Sarahmonster9000', '7aed73f28e36516d6b1af81271bccdc732b5abf3e17b5a56acda5a7a13f30dc3'),
        User(2, 'HunoristheGOAT', '39d4b14056843a7719d9612663b05e6d6bbe5db862fa944394bc4c205a8b0ab8'),
        User(3, 'Username', hashed_password)
    ]

'''
when we call @find, we read a user from the database
'''

def test_find_user_reads_user_from_database(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = UserRepository(db_connection)
    raw_password = 'I_love_Horses&'
    hashed_password = hashlib.sha256('I_love_Horses&'.encode("utf-8")).hexdigest()
    user = User(3, 'Username', raw_password)
    repo.create(user)
    results = repo.find('Username', raw_password)
    assert results == User(3, 'Username', hashed_password)

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
we want to test that a users password is stored as a hash in the database
'''

def test_password_is_stored_as_hash(db_connection):
    db_connection.seed('seeds/maplebnb.sql')
    repo = UserRepository(db_connection)
    raw_password = 'I_hate_tests%'
    user_1 = User(1, 'Username999', raw_password)
    repo.create(user_1)
    hashed_password = hashlib.sha256(raw_password.encode("utf-8")).hexdigest()
    result = repo.find('Username999', raw_password) 
    assert result.password == hashed_password 

    




