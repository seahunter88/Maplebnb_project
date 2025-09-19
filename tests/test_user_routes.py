from playwright.sync_api import Page, expect
"""
POST /signin
  Parameters:
    username: Leo12345
    password: password!
  Expected response (200 OK):
  "Welcome back Leo12345!"
"""
def test_post_signup(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/signup')
    page.fill("input[name=username]", 'Leo12345')
    page.fill("input[name=password]", 'password!')
    page.fill("input[name=confirm_password]", 'password!')
    page.click("text=Create a new account")
    expect(page.locator('h1')).to_have_text('Welcome to Maplebnb!')


'''
POST /signin
  Parameters:
    username: ""
    password: password!
  Expected response (200 OK):
  "Here are your errors: Username cannot be blank
'''

def test_post_signup_with_blank_username(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/signup')
    page.fill("input[name=username]", '')
    page.fill("input[name=password]", 'password!')
    page.fill("input[name=confirm_password]", 'password!')
    page.click("text=Create a new account")
    expect(page.locator('.t-errors')).to_have_text('Here are your errors: username must be 4-16 characters in length')

    '''
POST /signin
  Parameters:
    username: username
    password: ""
  Expected response (200 OK):
  "Here are your errors: Password cannot be blank
'''

def test_post_signup_with_blank_password(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/signup')
    page.fill("input[name=username]", 'Username')
    page.fill("input[name=password]", '')
    page.fill("input[name=confirm_password]", '')
    page.click("text=Create a new account")
    expect(page.locator('.t-errors')).to_have_text('Here are your errors: password must be 8-16 characters in length and contain a special character')

    '''
POST /signin
  Parameters:
    username: username
    password: ""
  Expected response (200 OK):
  "Here are your errors: Password cannot be blank
'''

def test_post_signup_with_blank_password_and_username(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/signup')
    page.fill("input[name=username]", '')
    page.fill("input[name=password]", '')
    page.fill("input[name=confirm_password]", '')
    page.click("text=Create a new account")
    expect(page.locator('.t-errors')).to_have_text('Here are your errors: username must be 4-16 characters in length, password must be 8-16 characters in length and contain a special character')

'''
POST /signin
  Parameters:
    username: username
    password: "password1!"
    Expected response: "Welcome Page."
'''

def test_post_signin(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/')
    page.fill("input[name=username]", 'Sarahmonster9000')
    page.fill("input[name=password]", 'Iloveponies!')
    page.click("text='Sign In'")
    expect(page.locator('h1')).to_have_text('Welcome back, Sarahmonster9000! Here are your bookings:')

'''
when username and password do not match a record in the database, sign in fails
'''

def test_post_signin_fails_when_username_and_password_incorrect(page, test_web_address, db_connection):
  page.set_default_timeout(1000)
  db_connection.seed('seeds/maplebnb.sql')
  page.goto(f'http://{test_web_address}/')
  page.fill("input[name=username]", 'Sarahmonster')
  page.fill("input[name=password]", 'Ilovepony!')
  page.click("text='Sign In'")
  expect(page.locator('.t-user_not_found_error')).to_have_text('An account with those details is not found.')


'''
when there is a duplicate username in the database, show an error when signing up
'''

def test_post_signup_with_duplicate_username(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/signup')
    page.fill("input[name=username]", 'Sarahmonster9000')
    page.fill("input[name=password]", 'Password12345!')
    page.fill("input[name=confirm_password]", 'Password12345!')
    page.click("text=Create a new account")
    expect(page.locator('.t-duplicate_username_error')).to_have_text('Username is already in use.')

'''
when passwords do not match on sign up, show an error saying 'passwords do not match'
'''

def test_post_signup_with_mismatching_passwords(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/signup')
    page.fill("input[name=username]", 'Sarahmonster123')
    page.fill("input[name=password]", 'Password12345!')
    page.fill("input[name=confirm_password]", 'Password123!')
    page.click("text=Create a new account")
    expect(page.locator('.t-errors')).to_have_text('Here are your errors: passwords do not match')

'''
when passwords do match on sign up, the user is shown the welcome page
'''

def test_post_signup_with_matching_passwords(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/signup')
    page.fill("input[name=username]", 'Sarahmonster123')
    page.fill("input[name=password]", 'Password12345!')
    page.fill("input[name=confirm_password]", 'Password12345!')
    page.click("text=Create a new account")
    expect(page.locator('h1')).to_have_text('Welcome to Maplebnb!')

'''
when passwords do not match and are invalid on sign up, the user is shown an error
'''

def test_post_signup_with_mismatching_and_invalid_passwords(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/signup')
    page.fill("input[name=username]", 'Sarahmonster123')
    page.fill("input[name=password]", 'Pass')
    page.fill("input[name=confirm_password]", 'Passw')
    page.click("text=Create a new account")
    expect(page.locator('.t-errors')).to_have_text('Here are your errors: password must be 8-16 characters in length and contain a special character, passwords do not match')
