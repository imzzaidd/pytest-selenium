import pytest
from pages.login.login2_page import Login2View
from config.config import Config

@pytest.mark.usefixtures("browser")
class TestLogin2:
    def test_login_success(self, browser):
        login_page = Login2View(browser)
        
        username = Config.USERNAME
        password = Config.PASSWORD
        
        assert username, "USERNAME2 is not set in the environment variables"
        assert password, "PASSWORD2 is not set in the environment variables"
        
        assert login_page.login(username, password), "Login failed: Unable to login with provided credentials"
        assert login_page.is_element_visible(Config.PRODUCTS_HEADER_XPATH), "Login verification failed: User is not logged in"
