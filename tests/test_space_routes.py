from playwright.sync_api import Page, expect

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
    
"""
we can render specific spaces on their on detailed view /spaces/<space_id>
"""  
def test_get_first_space(page, db_connection, test_web_address):
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/spaces/1')
    h1_tag = page.locator('h1')
    h2_tag = page.locator('h2')
    h3_tag = page.locator('h3')
    expect(h1_tag).to_have_text(["House_1"])
    expect(h2_tag).to_have_text(["Price per night: 100"])
    expect(h3_tag).to_have_text(["Description: a nice house"])

def test_get_second_space(page, db_connection, test_web_address):
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/spaces/2')
    h1_tag = page.locator('h1')
    h2_tag = page.locator('h2')
    h3_tag = page.locator('h3')
    expect(h1_tag).to_have_text(["House_2"])
    expect(h2_tag).to_have_text(["Price per night: 150"])
    expect(h3_tag).to_have_text(["Description: a nicer house"])

"""
We can get from the welcome page to show all spaces page
"""
def test_welcome_page_link_to_show_all_spaces(page, db_connection, test_web_address):
    db_connection.seed('seeds/maplebnb.sql')
    page.goto(f'http://{test_web_address}/welcome')
    page.click("text=Browse Spaces")
    expect(page.locator('h1')).to_have_text("All Spaces")