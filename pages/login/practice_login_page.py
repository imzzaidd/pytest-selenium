from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class LoginView:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50)

    def fill_username_input(self, username, username_input):
        time.sleep(2)
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
        
    def verify_login_successful(self, congrats_message_xpath):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, congrats_message_xpath)))
            return True
        except:
            return False
    

    def login_successfully(self, username_input, username, password_input, password, login_button_xpath):
        self.driver.get('https://practicetestautomation.com/practice-test-login/')
        self.driver.maximize_window()
        self.fill_username_input(username, username_input)
        self.fill_password_input(password, password_input)
        self.click_login_button(login_button_xpath)
        
        

