class AdminPage:
    def __init__(self, page):
        self.page = page

    def go_to_admin(self):
         self.page.get_by_role("link", name="Admin").click()
         self.page.wait_for_selector("h5:has-text('System Users')")

    # def search_user(self, username):
    #     self.page.fill("input[placeholder='Username']", username)
    #     self.page.click("button[type='submit']")
    def search_user(self, username):
    # get first username input
     self.page.locator("input.oxd-input").nth(1).fill(username)
     self.page.get_by_role("button", name="Search").click()