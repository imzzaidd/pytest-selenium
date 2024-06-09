import pytest
from pages.login.login_page import LoginView
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.mark.usefixtures("browser")
class TestLogin:
    def test_login_success(self, browser):
        login_page = LoginView(browser)
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')

        assert login_page.login(username, password), "Login failed"
        assert login_page.is_login_successful(), "Login verification failed"

    def test_logout_success(self, browser):
        login_page = LoginView(browser)
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')

        assert login_page.login(username, password), "Login failed"
        assert login_page.is_login_successful(), "Login verification failed"
        assert login_page.logout(), "Logout failed"
        assert login_page.is_logout_successful(), "Logout verification failed"
