# from utils.config import BASE_URL

# class LoginPage:
#     def __init__(self, page):
#         self.page = page

#     def goto(self):
#         self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#     def login(self, username, password):
#     self.page.get_by_placeholder("Username").fill(username)
#     self.page.get_by_placeholder("Password").fill(password)
#     self.page.get_by_role("button", name="Login").click()
#     self.page.wait_for_selector("h6:has-text('Dashboard')")
from utils.config import BASE_URL

class LoginPage:
    def __init__(self, page):
        self.page = page

    def goto(self):
        self.page.goto(BASE_URL, wait_until="domcontentloaded",timeout=60000)
    def login(self, username, password):
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

        # wait for dashboard element (BEST practice)
        self.page.wait_for_selector("h6:has-text('Dashboard')")