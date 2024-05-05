import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.login.practice_login_page import LoginView
from tests.config import  username_input,username,password_input,password,login_button_xpath,congrats_message_xpath

'''
@pytest.fixture(scope="session")
def browser():
    options = FirefoxOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')

    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()
'''

def test_login_success(browser):
    login_page = LoginView(browser)
    login_page.login_successfully(username_input, username, password_input, password, login_button_xpath)
    assert login_page.verify_login_successful(congrats_message_xpath) == True
