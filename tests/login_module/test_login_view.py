import pytest
from selenium import webdriver
from pages.login.login_view import LoginView
from config.config import Config

'''
@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
'''

@pytest.mark.usefixtures("browser")
class TestLoginView:

    """
    Test suite for Login functionality
    """

    def test_login_success(self, browser):
        """
        Test del Login con credenciales correctas
        """
        login_page = LoginView(browser)
        
        username = Config.USERNAME
        password = Config.PASSWORD
        
        assert username, "USERNAME is not set in the environment variables"
        assert password, "PASSWORD is not set in the environment variables"
        
        assert login_page.login_success(username, password), "Login failed: Unable to login with provided credentials"
        assert login_page.is_element_visible(Config.PRODUCTS_HEADER_XPATH), "Login verification failed: User is not logged in"

    def test_login_failure(self, browser):
        """
        Test del Login con credenciales incorrectas
        """
        login_page = LoginView(browser)
        
        invalid_username = Config.INVALID_USERNAME
        invalid_password = Config.INVALID_PASSWORD
        
        assert invalid_username, "INVALID_USERNAME is not set in the environment variables"
        assert invalid_password, "INVALID_PASSWORD is not set in the environment variables"

        login_page.login_failure(invalid_username,invalid_password), "Login should fail with invalid credentials"
        login_page.is_element_visible(Config.INVALID_MESSAGE_XPATH), "Error message not displayed for invalid credentials"

    def test_empty_fields(self, browser):
        """
        Test del Login con campos vacíos
        """
        login_page = LoginView(browser)
        
        empty_username = ""
        empty_password = ""

        login_page.login_empty_fields(empty_username, empty_password), "Login should fail with empty credentials"
        login_page.is_element_visible(Config.EMPTY_MESSAGE_XPATH), "Error message not displayed for empty fields"
    
    def test_empty_username(self, browser):
        """
        Test del Login con campo de usuario vacío
        """
        login_page = LoginView(browser)
        
        empty_username = ""
        password = Config.PASSWORD

        login_page.login_empty_username(empty_username, password), "Login should fail with empty username"
        login_page.is_element_visible(Config.EMPTY_MESSAGE_XPATH), "Error message not displayed for empty username"
    
    def test_empty_password(self, browser):
        """
        Test del Login con campo de contraseña vacío
        """
        login_page = LoginView(browser)
        
        username = Config.USERNAME
        empty_password = ""

        login_page.login_empty_password(username, empty_password), "Login should fail with empty password"
        login_page.is_element_visible(Config.EMPTY_MESSAGE_XPATH), "Error message not displayed for empty password"