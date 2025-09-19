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
    expect(page.locator('h1')).to_have_text('You just booked None on None!')

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
    expect(page.locator('h1')).to_have_text('You just booked House_1 on 2025-10-17!')

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
    expect(page.locator('h1')).to_have_text('You just booked None on None!')
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
    expect(page.locator('h1')).to_have_text('You just booked None on None!')
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
    expect(page.locator('h1')).to_have_text('Welcome back, Sarahmonster9000! Here are your bookings:')
    expect(page.locator('.t-bookings-list')).to_have_text('House_1, 2025-09-17')
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
    expect(page.locator('h1')).to_have_text('Welcome back, HunoristheGOAT! Here are your bookings:')
    expect(page.locator('.t-bookings-list')).to_have_text('House_2, 2025-08-17')


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
    expect(page.locator('h1')).to_have_text('You just booked House_1 on 2025-10-17!')
    page.goto(f'http://{test_web_address}/my_bookings/1')
    expect(page.locator('h1')).to_have_text('Welcome back, Sarahmonster9000! Here are your bookings:')
    expect(page.locator('.t-bookings-list')).to_have_text([
        'House_1, 2025-09-17',
        'House_1, 2025-10-17'
        ])
    
"""
After signin, I am redirected to my_bookings/{user_id} and I can see my bookings
"""
def test_signin_redirects_to_my_bookings_(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/')
    page.fill("input[name=username]", 'Sarahmonster9000')
    page.fill("input[name=password]", 'Iloveponies!')
    page.click("text='Sign In'")
    expect(page.locator('h1')).to_have_text('Welcome back, Sarahmonster9000! Here are your bookings:')
    expect(page.locator('.t-bookings-list')).to_have_text('House_1, 2025-09-17')
    

    
"""
When I create a new booking and then go to my_bookings, 
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
    expect(page.locator('h1')).to_have_text('You just booked House_1 on 2025-10-17!')
    page.goto(f'http://{test_web_address}/my_bookings/1')
    expect(page.locator('h1')).to_have_text('Welcome back, Sarahmonster9000! Here are your bookings:')
    expect(page.locator('.t-bookings-list')).to_have_text([
      'House_1, 2025-09-17',
      'House_1, 2025-10-17'
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


"""
When I try to create a duplicate booking, 
it re-renders the show_one_space page, does not redirect to booking_confirmation
This duplicate booking is NOT shown in the list of unavailable dates
"""
def test_duplicate_booking_is_not_redirected_2(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/spaces/2')
    expect(page.locator('h1')).to_have_text('House_2')
    page.fill("input[name=booking_date]", '2025-08-17')
    page.fill("input[name=booking_user_id]", '2')
    page.click("text=Create booking")
    expect(page.locator('h1')).to_have_text('House_2')
    expect(page.locator('h5')).to_have_text('2025-08-17')
    expect(page.locator('.t-errors')).to_have_text('Unfortunately this space is being used for a Pokemon convention on that date, please try a different date.')
    
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


"""
When I visit the create a booking form on show_one_space
it does NOT have the error message we would get from creating a duplicate booking
"""
def test_show_one_space_does_not_have_error_message(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/spaces/2')
    expect(page.locator('h1')).to_have_text('House_2')
    expect(page.locator('.t-errors')).to_have_count(0)
    