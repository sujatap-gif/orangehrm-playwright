# # from pages.login_page import LoginPage
# # from pages.admin_page import AdminPage
# # from utils.config import USERNAME, PASSWORD

# # def test_admin_search(page):
# #     login = LoginPage(page)
# #     admin = AdminPage(page)

# #     login.goto()
# #     login.login("Admin", "admin123")

# #     admin.go_to_admin()
# #     admin.search_user("Admin")

# #     assert "Admin" in page.content()
from pages.admin_page import AdminPage

def test_admin_search(logged_in_page):
    admin = AdminPage(logged_in_page)

    admin.go_to_admin()
    admin.search_user("Admin")

    assert logged_in_page.get_by_text("System Users").is_visible()