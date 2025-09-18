from lib.user import User

'''
When we construct a user, it has an id, username and password
'''

def test_user_constructs_with_properties():
    user = User(1, 'Username', 'Password!', 'Password!')
    assert user.id == 1
    assert user.username == 'Username'
    assert user.password == 'Password!'
    assert user.confirm_password == 'Password!'

'''
user objects are treated equally if they have equal values
'''

def test_equality():
    user_1 = User(1, 'Username', 'Password!', 'Password!')
    user_2 = User(1, 'Username', 'Password!', 'Password!')
    assert user_1 == user_2

'''
user objects are formatted as a nice string
'''

def test_user_formats_nicely_as_a_string():
    user_1 = User(1, 'Username', 'Password!', 'Password!')
    assert str(user_1) == 'User(1, Username, Password!, Password!)'

'''
@is_valid returns false if username is empty string
'''

def test_is_valid_returns_false_for_empty_username():
    user_1 = User(1, '', 'Password!', 'Password!')
    assert user_1.is_valid() == False


'''
@is_valid returns false if password is empty string
'''

def test_is_valid_returns_false_for_empty_password():
    user_1 = User(1, 'Username', '', 'Password!')
    assert user_1.is_valid() == False

'''
@is_valid returns true if username and password are strings
'''

def test_is_valid_returns_true_for_string_username_and_password():
    user_1 = User(1, 'Username', 'Password!', 'Password!')
    assert user_1.is_valid() == True

'''
@generate_errors returns a string if username is blank
'''

def test_generate_errors_returns_string_if_username_blank():
    user_1 = User(1, '', 'Password!', 'Password!')
    assert user_1.generate_errors() == "username must be 4-16 characters in length"

'''
@generate_errors returns a string if password is blank
'''

def test_generate_errors_returns_string_if_password_blank():
    user_1 = User(1, 'Username', '', '')
    assert user_1.generate_errors() == "password must be 8-16 characters in length and contain a special character"

'''
@generate_errors returns a string of errors if username and password are blank
'''

def test_generate_errors_returns_string_if_username_and_password_blank():
    user_1 = User(1, '', '', '')
    assert user_1.generate_errors() == "username must be 4-16 characters in length, password must be 8-16 characters in length and contain a special character"

'''
@is_valid returns False when the password is less than 8 chars.
'''

def test_is_valid_returns_false_when_password_too_short():
    user_1 = User(1, 'username', '1234567', '1234567')
    assert user_1.is_valid() == False

'''
@check_length returns False when password is too short
'''

def test_check_password_length_returns_false_when_password_is_too_short():
    user_1 = User(1, 'username', '1234567', '1234567')
    assert user_1.check_password_length() == False

'''
@check_length returns False when password is too long
'''

def test_check_password_length_returns_false_when_password_is_too_long():
    user_1 = User(1, 'username', '123456712345671234567', '123456712345671234567')
    assert user_1.check_password_length() == False

'''
@check_password_length returns True when password is correct length
'''

def test_check_password_length_returns_true_when_password_is_long_enough():
    user_1 = User(1, 'username', '12345678', '12345678')
    assert user_1.check_password_length() == True

'''
@check_username_length returns True when username is correct length
'''

def test_check_username_length_returns_true_when_username_is_long_enough():
    user_1 = User(1, 'username', '12345678', '12345678')
    assert user_1.check_username_length() == True

'''
@check_username_length returns False when username is too short
'''

def test_check_username_length_returns_true_when_username_is_too_short():
    user_1 = User(1, 'bob', '12345678', '12345678')
    assert user_1.check_username_length() == False

'''
@check_username_length returns False when username is too long
'''

def test_check_username_length_returns_true_when_username_is_too_long():
    user_1 = User(1, 'bobbobbobbobbobbobbob', '12345678', '12345678')
    assert user_1.check_username_length() == False

'''
@special_chars returns False when the password does not contain a special character.
'''

def test_special_chars_returns_false_when_password_has_no_special_char():
    user_1 = User(1, 'username', '12345678', '12345678')
    assert user_1.special_chars() == False

'''
@special_chars returns True when the password does contain a special character.
'''

def test_special_chars_returns_true_when_password_has_a_special_char():
    user_1 = User(1, 'username', '12345678!', '12345678!')
    assert user_1.special_chars() == True

'''
@check_passwords_match returns True when passwords match
'''

def test_check_password_returns_true_when_passwords_match():
    user_1 = User(1, 'username', '12345678!', '12345678!')
    assert user_1.check_passwords_match() == True

'''
@check_passwords_match returns False when passwords do not match
'''

def test_check_password_returns_true_when_passwords_match():
    user_1 = User(1, 'username', '12345678!', '123456789!')
    assert user_1.check_passwords_match() == False

'''
@is_valid returns False when the password does not have a special character.
'''

def test_is_valid_returns_false_when_password_does_not_have_special_character():
    user_1 = User(1, 'username', '1234567', '1234567')
    assert user_1.is_valid() == False


'''
@generate_errors returns a string of errors if password isn't long enough
'''

def test_generate_errors_returns_string_if_password_is_too_short():
    user_1 = User(1, 'username', '1234567', '1234567')
    assert user_1.generate_errors() == "password must be 8-16 characters in length and contain a special character"

'''
@generate_errors returns a string of errors if the password doesn't contain a special char
'''

def test_generate_errors_returns_string_if_password_does_not_have_special_char():
    user_1 = User(1, 'username', '12345678', '12345678')
    assert user_1.generate_errors() == "password must be 8-16 characters in length and contain a special character"

