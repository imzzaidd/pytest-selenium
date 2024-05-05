import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.login.practice_login_page import LoginView
from config import logo_page_xpath, header_page_xpath, home_header_option_xpath, home_header_practice_option_xpath, home_header_courses_option_xpath, home_header_blog_option_xpath, home_header_contact_option_xpath, title_page_xpath, username, username_input, password, password_input
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
def test_create_template(browser):
    practice_login_page = LoginView(browser)
    practice_login_page.login_successfully(logo_page_xpath, header_page_xpath, home_header_option_xpath, home_header_practice_option_xpath, home_header_courses_option_xpath, home_header_blog_option_xpath, home_header_contact_option_xpath, title_page_xpath, username, username_input, password, password_input)
    verification_results = []
    verification_results.append(practice_login_page.verify_login_view())
    for i, result in enumerate(verification_results, start=1):
        if result:
            print(f"Verificación {i}: Éxito")
        else:
            print(f"Verificación {i}: Error")

    if False in verification_results:
        print("La prueba falló: Uno o más elementos no pudieron ser verificados correctamente.")
    else:
        print("La prueba fue exitosa: Todos los elementos fueron verificados correctamente.")