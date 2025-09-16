from lib.users import User

'''
When we construct a user, it has an id, username and password
'''

def test_user_constructs_with_properties():
    user = User(1, 'Username', 'Password!')
    assert user.id == 1
    assert user.username == 'Username'
    assert user.password == 'Password!'

'''
user objects are treated equally if they have equal values
'''

def test_equality():
    user_1 = User(1, 'Username', 'Password!')
    user_2 = User(1, 'Username', 'Password!')
    assert user_1 == user_2

'''
user objects are formatted as a nice string
'''

def test_user_formats_nicely_as_a_string():
    user_1 = User(1, 'Username', 'Password!')
    assert str(user_1) == 'User(1, Username, Password!)'
