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


"""
GET /my_bookings/1
  Parameters: None
  Expected response (200 OK):
  "My Bookings:"
"""
def test_my_bookings_page_exists_1(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/my_bookings/1')
    expect(page.locator('h1')).to_have_text('My Bookings:')
    expect(page.locator('.t-bookings-list')).to_have_text('2025-09-17')
    # page.click("text=Go to welcome page")
    # expect(page.locator('h1')).to_have_text('Welcome to Maplebnb!')

"""
GET /my_bookings/2
  Parameters: None
  Expected response (200 OK):
  "My Bookings:"
"""
def test_my_bookings_page_exists_2(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/my_bookings/2')
    expect(page.locator('h1')).to_have_text('My Bookings:')
    expect(page.locator('.t-bookings-list')).to_have_text('2025-08-17')


"""
When I create a booking, I can see that reflected in my_bookings
"""
def test_my_bookings_updates_with_new_bookings(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/spaces/1')
    expect(page.locator('h1')).to_have_text('House_1')
    page.fill("input[name=booking_date]", '2025-10-17')
    page.fill("input[name=booking_user_id]", '1')
    page.click("text=Create booking")
    expect(page.locator('h1')).to_have_text('Booking created!')
    page.goto(f'http://{test_web_address}/my_bookings/1')
    expect(page.locator('h1')).to_have_text('My Bookings:')
    expect(page.locator('.t-bookings-list')).to_have_text([
        '2025-09-17',
        '2025-10-17'
        ])
    
"""
When I visit the welcome page, I can see the text: 'view your bookings'
"""
def test_welcome_page_shows_view_your_bookings(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/welcome')
    expect(page.locator('h1')).to_have_text('Welcome to Maplebnb!')
    expect(page.locator('h2')).to_have_text('View your bookings:')
    
"""
When I visit the welcome page, I can input my user id and see my_bookings page.
"""
def test_welcome_page_form_redirects_to_my_bookings_page(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/welcome')
    expect(page.locator('h1')).to_have_text('Welcome to Maplebnb!')
    expect(page.locator('h2')).to_have_text('View your bookings:')
    page.fill("input[name=user_id]", '1')
    page.click("text=Submit")
    expect(page.locator('h1')).to_have_text('My Bookings:')
    expect(page.locator('.t-bookings-list')).to_have_text('2025-09-17')
    
"""
When I visit the welcome page, I can input my user id and see my_bookings page.
"""
def test_welcome_page_form_redirects_to_my_bookings_page_2(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/welcome')
    expect(page.locator('h1')).to_have_text('Welcome to Maplebnb!')
    expect(page.locator('h2')).to_have_text('View your bookings:')
    page.fill("input[name=user_id]", '2')
    page.click("text=Submit")
    expect(page.locator('h1')).to_have_text('My Bookings:')
    expect(page.locator('.t-bookings-list')).to_have_text('2025-08-17')
    
"""
When I create a new booking and then go to welcome and then to my_bookings, 
I see the new booking in the list.
"""
def test_create_booking_shows_in_my_bookings(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/spaces/1')
    expect(page.locator('h1')).to_have_text('House_1')
    page.fill("input[name=booking_date]", '2025-10-17')
    page.fill("input[name=booking_user_id]", '1')
    page.click("text=Create booking")
    expect(page.locator('h1')).to_have_text('Booking created!')
    page.click("text=Go to welcome page")
    page.fill("input[name=user_id]", '1')
    page.click("text=Submit")
    expect(page.locator('h1')).to_have_text('My Bookings:')
    expect(page.locator('.t-bookings-list')).to_have_text([
      '2025-09-17',
      '2025-10-17'
    ])

"""
When I try to create a duplicate booking, 
it re-renders the show_one_space page, does not redirect to booking_confirmation
This duplicate booking is NOT shown in the list of unavailable dates
"""
def test_duplicate_booking_is_not_redirected(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/spaces/1')
    expect(page.locator('h1')).to_have_text('House_1')
    page.fill("input[name=booking_date]", '2025-09-17')
    page.fill("input[name=booking_user_id]", '1')
    page.click("text=Create booking")
    expect(page.locator('h1')).to_have_text('House_1')
    expect(page.locator('h5')).to_have_text('2025-09-17')
    expect(page.locator('.t-errors')).to_have_text('Unfortunately this space is being used for a Pokemon convention on that date, please try a different date.')