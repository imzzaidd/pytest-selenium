import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.login.practice_login_page import LoginView
from tests.config import  username_input, username, password_input, password, login_button_xpath,logout_button_xpath

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
    login_page_view = LoginView(browser)
    login_page_view.login_successfully(username_input,username, password_input,password, login_button_xpath)
    verification_results = []
    verification_results.append(login_page_view.verify_login_successful())
    for i, result in enumerate(verification_results, start=1):
        if result:
            print(f"Verificación {i}: Éxito")
        else:
            print(f"Verificación {i}: Error")
    if False in verification_results:
        print("La prueba falló: Uno o más elementos no pudieron ser verificados correctamente.")
    else:
        print("La prueba fue exitosa: Todos los elementos fueron verificados correctamente.")
        
def test_logout_success(browser):
    login_page_view = LoginView(browser)
    login_page_view.logout_successfully(username_input,username, password_input,password, login_button_xpath,logout_button_xpath)
    verification_results = []
    verification_results.append(login_page_view.verify_logout_sucessful())
    for i, result in enumerate(verification_results, start=1):
        if result:
            print(f"Verificación {i}: Éxito")
        else:
            print(f"Verificación {i}: Error")
    if False in verification_results:
        print("La prueba falló: Uno o más elementos no pudieron ser verificados correctamente.")
    else:
        print("La prueba fue exitosa: Todos los elementos fueron verificados correctamente.")