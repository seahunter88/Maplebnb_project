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
    
'''
@is_valid returns False when the password is less than 8 chars.
'''

def test_is_valid_returns_false_when_password_too_short():
    user_1 = User(1, 'username', '1234567')
    assert user_1.is_valid() == False
    
'''
@check_length returns False when password is too short
'''

def test_check_length_returns_false_when_password_is_too_short():
    user_1 = User(1, 'username', '1234567')
    assert user_1.check_length() == False
    
'''
@check_length returns True when password is correct length
'''

def test_check_length_returns_true_when_password_is_too_short():
    user_1 = User(1, 'username', '12345678')
    assert user_1.check_length() == True
    
'''
@special_chars returns False when the password does not contain a special character.
'''

def test_special_chars_returns_false_when_password_has_no_special_char():
    user_1 = User(1, 'username', '12345678')
    assert user_1.special_chars() == False
    
'''
@special_chars returns True when the password does contain a special character.
'''

def test_special_chars_returns_true_when_password_has_a_special_char():
    user_1 = User(1, 'username', '12345678!')
    assert user_1.special_chars() == True
    
    
'''
@is_valid returns False when the password does not have a special character.
'''

def test_is_valid_returns_false_when_password_does_not_have_special_character():
    user_1 = User(1, 'username', '1234567')
    assert user_1.is_valid() == False
  
  
# need to implement errors when password length is too short while not being triggered when the password is blank  
# '''
# @generate_errors returns a string of errors if password isn't long enough
# '''

# def test_generate_errors_returns_string_if_password_is_too_short():
#     user_1 = User(1, 'username', '1234567')
#     assert user_1.generate_errors() == "Password must be at least 8 characters long"
    