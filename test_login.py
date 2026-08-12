from playwright.sync_api import Page, expect

def test_successful_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_login_with_wrong_password(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce1")
    page.click("#login-button")
    error_message = page.locator("[data-test='error']")
    expect(error_message).to_contain_text("Username and password do not match")

def test_locked_out_user_cannot_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "locked_out_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    error_message = page.locator("[data-test='error']")
    expect(error_message).to_contain_text("this user has been locked out")