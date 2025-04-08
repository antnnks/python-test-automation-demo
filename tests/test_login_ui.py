from pages.login_page import LoginPage

def test_successful_login(driver):
    page = LoginPage(driver)
    page.open("https://example.com/login")
    page.login("testuser", "testpass")
    assert "dashboard" in driver.current_url
