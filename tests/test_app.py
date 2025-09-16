from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    p_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    expect(p_tag).to_have_text("This is the homepage.")
    

"""
We can render the show_spaces page
"""
def test_show_spaces(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/spaces")

    # We look at the <p> tag
    p_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    expect(p_tag).to_have_text("SHOW SPACES")
    

"""
POST /signin
  Parameters:
    username: Leo12345
    password: password!
  Expected response (200 OK):
  "Welcome back Leo12345!"
"""
# def test_post_signup(page, test_web_address, db_connection):
#     page.set_default_timeout(1000)
#     db_connection.seed('seeds/maplebnb.sql')
#     page.goto(f'http://{test_web_address}/signup')
#     page.fill("input[username=username]", 'Leo12345')
#     page.fill("input[password=password]", 'password!')
#     page.click("text=Create a new account")
#     expect(page.locator('h1')).to_have_text('Welcome to Maplebnb!')
