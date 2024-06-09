from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
from dotenv import load_dotenv
import os

load_dotenv()

class LoginView:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def fill_username_input(self, username, username_input):
        time.sleep(1)
        username_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, username_input)))
        username_input.clear()
        username_input.send_keys(username)

    def fill_password_input(self, password, password_input):
        time.sleep(1)
        password_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, password_input)))
        password_input.clear()
        password_input.send_keys(password)
        
    def click_login_button(self, login_button_xpath):
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, login_button_xpath)))
        login_button.click()

    def click_logout_button(self, logout_button_xpath):
        time.sleep(1)
        logout_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, logout_button_xpath)))
        logout_button.click()
        
    def verify_login_successful(self):
        try:
            time.sleep(1)
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[@class='post-title'][contains(.,'Logged In Successfully')]")))
            return True
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error durante la verificación del login: {str(e)}")
        return False

    def verify_logout_successful(self):
        try:
            time.sleep(1)
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'Test login')]")))
            return True
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error durante la verificación del logout: {str(e)}")
        return False

    def login_successfully(self, username_input, username, password_input, password, login_button_xpath):
        login_url = os.getenv('LOGIN_URL')
        if not login_url:
            raise ValueError("LOGIN_URL no se cargó correctamente desde el archivo .env")
        self.driver.get(login_url)
        self.driver.maximize_window()
        self.fill_username_input(username, username_input)
        self.fill_password_input(password, password_input)
        self.click_login_button(login_button_xpath)
        return self.verify_login_successful()
        
    def logout_successfully(self, username_input, username, password_input, password, login_button_xpath, logout_button_xpath):
        login_url = os.getenv('LOGIN_URL')
        if not login_url:
            raise ValueError("LOGIN_URL no se cargó correctamente desde el archivo .env")
        self.driver.get(login_url)
        self.driver.maximize_window()
        self.fill_username_input(username, username_input)
        self.fill_password_input(password, password_input)
        self.click_login_button(login_button_xpath)
        if self.verify_login_successful():
            self.click_logout_button(logout_button_xpath)
            return self.verify_logout_successful()
        return False
