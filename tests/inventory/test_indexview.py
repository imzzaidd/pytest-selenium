import pytest
from selenium import webdriver
from pages.index.index_view import InventoryView
from tests.login_module.test_login_view import test_login_success
from config.config import Config

'''
@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
'''
class TestInventoryView:

    """
    Test suite for Inventory functionality
    """

    def test_index_view(self, browser):
        """
        Test de Inventory
        """   
        test_login_success(browser)
        
    def test_hamburger_menu(self, browser):
        """
        Test del menú hamburguesa
        """
        inventory_page = InventoryView(browser)
        test_login_success(browser)
        inventory_page.click_element(Config.MENU_BUTTON_XPATH)
        inventory_page.is_element_visible(Config.ABOUT_LINK), "About link is not visible"
        inventory_page.click_element(Config.ABOUT_LINK)
        inventory_page.is_element_visible(Config.LOGO_SAUSELABS_XPATH), "Saucelabs logo is not visible"
        inventory_page.go_back()
        inventory_page.is_element_visible(Config.PRODUCTS_HEADER_XPATH), "Back to products page failed"
        inventory_page.click_element(Config.MENU_BUTTON_XPATH)
        inventory_page.click_element(Config.LOGOUT_BUTTON_XPATH)
        inventory_page.is_element_visible(Config.USERNAME_INPUT_XPATH), "Logout failed"

        