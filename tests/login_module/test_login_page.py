import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.login.practice_login_page import LoginView
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from tests.config import  username_input, username, password_input, password, login_button_xpath, logout_button_xpath

@pytest.fixture(scope="session")
def browser():
    options = FirefoxOptions()
    options.headless = True
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')

    # Use RemoteWebDriver instead of webdriver.Firefox
    driver = RemoteWebDriver(
        command_executor='http://localhost:4444/wd/hub',
        options=options
    )
    yield driver
    driver.quit()
def test_login_success(browser):
    login_page_view = LoginView(browser)
    login_page_view.login_successfully(username_input, username, password_input, password, login_button_xpath)
    verification_results = []
    verification_results.append(login_page_view.verify_login_successful())
    for i, result in enumerate(verification_results, start=1):
        if result:
            print(f"Verification {i}: Success")
        else:
            print(f"Verification {i}: Error")
    assert all(verification_results), "Test failed: One or more elements could not be verified correctly."

def test_logout_success(browser):
    login_page_view = LoginView(browser)
    login_page_view.logout_successfully(username_input, username, password_input, password, login_button_xpath, logout_button_xpath)
    verification_results = []
    verification_results.append(login_page_view.verify_logout_sucessful())  # Corrected method name
    for i, result in enumerate(verification_results, start=1):
        if result:
            print(f"Verification {i}: Success")
        else:
            print(f"Verification {i}: Error")
    assert all(verification_results), "Test failed: One or more elements could not be verified correctly."
