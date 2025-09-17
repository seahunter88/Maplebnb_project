from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    p_tag_1 = page.locator(".t-homepage")
    p_tag_2 = page.locator(".t-signup")

    # We assert that it has the text "This is the homepage."
    expect(p_tag_1).to_have_text("This is the homepage.")
    expect(p_tag_2).to_have_text("Create an Account")
    

"""
We can render the show_spaces page
"""
def test_show_spaces(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces")
    h1_tag = page.locator("h1")
    h2_tag = page.locator("h2")
    expect(h1_tag).to_have_text("All Spaces")
    expect(h2_tag).to_have_text([
        "House_1",
        "House_2"
    ])
    

def test_get_first_space(page, db_connection, test_web_address):
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/spaces/1')
    h1_tag = page.locator('h1')
    h2_tag = page.locator('h2')
    h3_tag = page.locator('h3')
    expect(h1_tag).to_have_text(["House_1"])
    expect(h2_tag).to_have_text(["Price per night: 100"])
    expect(h3_tag).to_have_text(["Description: a nice house"])


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
    expect(page.locator('.t-errors')).to_have_text('Here are your errors: username cannot be blank')

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
    expect(page.locator('.t-errors')).to_have_text('Here are your errors: username cannot be blank, password must be 8-16 characters in length and contain a special character')