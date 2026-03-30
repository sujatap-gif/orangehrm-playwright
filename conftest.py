# # import pytest
# # import os

# # @pytest.hookimpl(hookwrapper=True)
# # def pytest_runtest_makereport(item, call):
# #     outcome = yield
# #     rep = outcome.get_result()

# #     if rep.when == "call" and rep.failed:
# #         page = item.funcargs.get("page")
# #         if page:
# #             os.makedirs("screenshots", exist_ok=True)
# #             page.screenshot(path=f"screenshots/{item.name}.png")
# import pytest
# import os

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()

#     if rep.when == "call" and rep.failed:
#         page = item.funcargs.get("page")
#         if page:
#             os.makedirs("screenshots", exist_ok=True)
#             page.screenshot(path=f"screenshots/{item.name}.png")
import pytest
import os
from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD

# ✅ Screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("screenshots", exist_ok=True)
            page.screenshot(path=f"screenshots/{item.name}.png")

# ✅ Login fixture
@pytest.fixture
def logged_in_page(page):
    login = LoginPage(page)
    login.goto()
    login.login(USERNAME, PASSWORD)
    return page