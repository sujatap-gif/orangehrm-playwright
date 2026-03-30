from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD

def test_login(page):
    login = LoginPage(page)

    login.goto()
    login.login("Admin", "admin123")
    assert "dashboard" in page.url