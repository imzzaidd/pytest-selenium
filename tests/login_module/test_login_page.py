import pytest
from pages.login.practice_login_page import LoginView
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.mark.usefixtures("browser")
class TestLogin:
    def test_login_success(self, browser):
        login_page_view = LoginView(browser)
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')
        username_input = os.getenv('USERNAME_INPUT_XPATH')
        password_input = os.getenv('PASSWORD_INPUT_XPATH')
        login_button_xpath = os.getenv('LOGIN_BUTTON_XPATH')

        assert username is not None, "USERNAME no se cargó correctamente desde el archivo .env"
        assert password is not None, "PASSWORD no se cargó correctamente desde el archivo .env"
        assert username_input is not None, "USERNAME_INPUT_XPATH no se cargó correctamente desde el archivo .env"
        assert password_input is not None, "PASSWORD_INPUT_XPATH no se cargó correctamente desde el archivo .env"
        assert login_button_xpath is not None, "LOGIN_BUTTON_XPATH no se cargó correctamente desde el archivo .env"

        assert login_page_view.login_successfully(username_input, username, password_input, password, login_button_xpath)

    def test_logout_success(self, browser):
        login_page_view = LoginView(browser)
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')
        username_input = os.getenv('USERNAME_INPUT_XPATH')
        password_input = os.getenv('PASSWORD_INPUT_XPATH')
        login_button_xpath = os.getenv('LOGIN_BUTTON_XPATH')
        logout_button_xpath = os.getenv('LOGOUT_BUTTON_XPATH')

        assert username is not None, "USERNAME no se cargó correctamente desde el archivo .env"
        assert password is not None, "PASSWORD no se cargó correctamente desde el archivo .env"
        assert username_input is not None, "USERNAME_INPUT_XPATH no se cargó correctamente desde el archivo .env"
        assert password_input is not None, "PASSWORD_INPUT_XPATH no se cargó correctamente desde el archivo .env"
        assert login_button_xpath is not None, "LOGIN_BUTTON_XPATH no se cargó correctamente desde el archivo .env"
        assert logout_button_xpath is not None, "LOGOUT_BUTTON_XPATH no se cargó correctamente desde el archivo .env"

        assert login_page_view.logout_successfully(username_input, username, password_input, password, login_button_xpath, logout_button_xpath)
