import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def browser():
    options = Options()
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()
