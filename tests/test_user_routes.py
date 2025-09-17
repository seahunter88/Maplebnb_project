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
    page.goto(f'http://{test_web_address}/signup')
    page.fill("input[name=username]", 'Leo12345')
    page.fill("input[name=password]", 'password!')
    page.click("text=Create a new account")
    page.goto(f'http://{test_web_address}/signin')
    page.fill("input[name=username]", 'Leo12345')
    page.fill("input[name=password]", 'password!')
    page.click("text=Sign In")
    expect(page.locator('h1')).to_have_text('Welcome to Maplebnb!')
