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

"""
GET /booking_confirmation
  Parameters: None
  Expected response (200 OK):
  "Welcome to Maplebnb!"
"""
def test_link_from_booking_confirmation_to_welcome_page(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/booking_confirmation')
    expect(page.locator('h1')).to_have_text('Booking created!')
    page.click("text=Go to welcome page")
    expect(page.locator('h1')).to_have_text('Welcome to Maplebnb!')

"""
GET /booking_confirmation
  Parameters: None
  Expected response (200 OK):
  "All Spaces"
"""
def test_link_from_booking_confirmation_to_spaces_page(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/booking_confirmation')
    expect(page.locator('h1')).to_have_text('Booking created!')
    page.click("text=Go to spaces page")
    expect(page.locator('h1')).to_have_text('All Spaces')


