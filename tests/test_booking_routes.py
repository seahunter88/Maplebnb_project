from playwright.sync_api import Page, expect

"""
GET /booking_confirmation
  Parameters: None
  Expected response (200 OK):
  "Booking created!"
"""
def test_get_booking_confirmation(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/booking_confirmation')
    expect(page.locator('h1')).to_have_text('Booking created!')

"""
POST /create_booking
  Parameters: None
  Expected response (200 OK):
  "Create a booking!"
"""
def test_post_create_booking(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/spaces/1')
    expect(page.locator('h1')).to_have_text('House_1')
    page.fill("input[name=booking_date]", '2025-10-17')
    page.fill("input[name=booking_user_id]", '1')
    page.click("text=Create booking")
    expect(page.locator('h1')).to_have_text('Booking created!')



# """
# POST /signin
#   Parameters:
#     username: Leo12345
#     password: password!
#   Expected response (200 OK):
#   "Welcome back Leo12345!"
# """
# def test_post_signup(page, test_web_address, db_connection):
#     page.set_default_timeout(1000)
#     db_connection.seed('seeds/maplebnb.sql')
#     page.goto(f'http://{test_web_address}/signup')
#     page.fill("input[name=username]", 'Leo12345')
#     page.fill("input[name=password]", 'password!')
#     page.click("text=Create a new account")
#     expect(page.locator('h1')).to_have_text('Welcome to Maplebnb!')


# '''
# POST /signin
#   Parameters:
#     username: ""
#     password: password!
#   Expected response (200 OK):
#   "Here are your errors: Username cannot be blank
# '''

# def test_post_signup_with_blank_username(page, test_web_address, db_connection):
#     page.set_default_timeout(1000)
#     db_connection.seed('seeds/maplebnb.sql')
#     page.goto(f'http://{test_web_address}/signup')
#     page.fill("input[name=username]", '')
#     page.fill("input[name=password]", 'password!')
#     page.click("text=Create a new account")
#     expect(page.locator('.t-errors')).to_have_text('Here are your errors: username must be 4-16 characters in length')

#     '''
# POST /signin
#   Parameters:
#     username: username
#     password: ""
#   Expected response (200 OK):
#   "Here are your errors: Password cannot be blank
# '''

# def test_post_signup_with_blank_password(page, test_web_address, db_connection):
#     page.set_default_timeout(1000)
#     db_connection.seed('seeds/maplebnb.sql')
#     page.goto(f'http://{test_web_address}/signup')
#     page.fill("input[name=username]", 'Username')
#     page.fill("input[name=password]", '')
#     page.click("text=Create a new account")
#     expect(page.locator('.t-errors')).to_have_text('Here are your errors: password must be 8-16 characters in length and contain a special character')

#     '''
# POST /signin
#   Parameters:
#     username: username
#     password: ""
#   Expected response (200 OK):
#   "Here are your errors: Password cannot be blank
# '''

# def test_post_signup_with_blank_password_and_username(page, test_web_address, db_connection):
#     page.set_default_timeout(1000)
#     db_connection.seed('seeds/maplebnb.sql')
#     page.goto(f'http://{test_web_address}/signup')
#     page.fill("input[name=username]", '')
#     page.fill("input[name=password]", '')
#     page.click("text=Create a new account")
#     expect(page.locator('.t-errors')).to_have_text('Here are your errors: username must be 4-16 characters in length, password must be 8-16 characters in length and contain a special character')