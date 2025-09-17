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
    