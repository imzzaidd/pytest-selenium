import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.webdriver import WebDriver as SafariDriver

@pytest.fixture(scope="session")
def browser(request):
    browser_names = request.config.getoption("--browser")
    drivers = []
    for browser_name in browser_names:
        if browser_name == "chrome":
            options = ChromeOptions()
            options.headless = True  # Ejecución en modo headless
            options.add_argument("--disable-dev-shm-usage")  # Deshabilita el uso de la memoria compartida
            options.add_argument("--no-sandbox")  # Evita problemas de sandbox
            options.add_argument("--ignore-certificate-errors")  # Ignora errores de certificado SSL
            driver = webdriver.Chrome(options=options)
        elif browser_name == "safari":
            driver = SafariDriver()
        elif browser_name == "firefox":
            options = FirefoxOptions()
            options.headless = True  # Ejecución en modo headless
            options.add_argument("--disable-dev-shm-usage")  # Deshabilita el uso de la memoria compartida
            options.add_argument("--no-sandbox")  # Evita problemas de sandbox
            options.add_argument("--ignore-certificate-errors")  # Ignora errores de certificado SSL
            driver = webdriver.Firefox(options=options)
        else:
            raise Exception("Unsupported browser!")
        driver.maximize_window()
        driver.implicitly_wait(10)
        drivers.append(driver)
    yield drivers
    for driver in drivers:
        driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", nargs='+', default=["firefox"], help="Type of browser(s) to use: chrome, safari, and/or firefox")
