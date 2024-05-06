import pytest
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.login.practice_login_page import LoginView
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

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
