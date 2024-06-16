import pytest
from selenium import webdriver
from pages.index.index_view import InventoryView
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
class TestInventoryView:

    """
    Test suite for Login functionality
    """

    def test_index_view(self, browser):
        """
        Test del Login con credenciales correctas
        """
        login_page = InventoryView(browser)
        
        username = Config.USERNAME
        password = Config.PASSWORD
        
        assert username, "USERNAME is not set in the environment variables"
        assert password, "PASSWORD is not set in the environment variables"
        
        login_page.index_view(username, password), "Login failed: Unable to login with provided credentials"
        login_page.is_element_visible(Config.PRODUCTS_HEADER_XPATH), "Login verification failed: User is not logged in"

    