from lib.user import User

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

'''
@is_valid returns false if username is empty string
'''

def test_is_valid_returns_false_for_empty_username():
    user_1 = User(1, '', 'Password!')
    assert user_1.is_valid() == False


'''
@is_valid returns false if password is empty string
'''

def test_is_valid_returns_false_for_empty_password():
    user_1 = User(1, 'Username', '')
    assert user_1.is_valid() == False

'''
@is_valid returns true if username and password are strings
'''

def test_is_valid_returns_true_for_string_username_and_password():
    user_1 = User(1, 'Username', 'Password!')
    assert user_1.is_valid() == True

'''
@generate_errors returns a string if username is blank
'''

def test_generate_errors_returns_string_if_username_blank():
    user_1 = User(1, '', 'Password!')
    assert user_1.generate_errors() == "Username cannot be blank"

'''
@generate_errors returns a string if password is blank
'''

def test_generate_errors_returns_string_if_password_blank():
    user_1 = User(1, 'Username', '')
    assert user_1.generate_errors() == "Password cannot be blank"

'''
@generate_errors returns a string of errors if username and password are blank
'''

def test_generate_errors_returns_string_if_password_blank():
    user_1 = User(1, '', '')
    assert user_1.generate_errors() == "Username cannot be blank, Password cannot be blank"