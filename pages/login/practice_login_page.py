from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import os
from dotenv import load_dotenv

load_dotenv()

class LoginView:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def load_page(self):
        self.driver.get(os.getenv('LOGIN_URL'))
        self.driver.maximize_window()

    def fill_username(self, username):
        username_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, os.getenv('USERNAME_INPUT_XPATH'))))
        username_input.clear()
        username_input.send_keys(username)

    def fill_password(self, password):
        password_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, os.getenv('PASSWORD_INPUT_XPATH'))))
        password_input.clear()
        password_input.send_keys(password)
        
    def click_login(self):
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, os.getenv('LOGIN_BUTTON_XPATH'))))
        login_button.click()

    def click_logout(self):
        logout_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, os.getenv('LOGOUT_BUTTON_XPATH'))))
        logout_button.click()

    def is_login_successful(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, os.getenv('TITLE_SUCCESSFUL_LOGIN_XPATH'))))
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def is_logout_successful(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, os.getenv('TITLE_PAGE_XPATH'))))
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def login(self, username, password):
        self.load_page()
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()
        return self.is_login_successful()
        
    def logout(self):
        if self.is_login_successful():
            self.click_logout()
            return self.is_logout_successful()
        return False
