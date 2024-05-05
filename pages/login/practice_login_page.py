from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import pdb

class LoginView:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 4)
    
    def verify_login_view(self,logo_page_xpath,header_page_xpath,home_header_option_xpath,home_header_practice_option_xpath,home_header_courses_option_xpath,home_header_blog_option_xpath,home_header_contact_option_xpath,title_page_xpath):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, logo_page_xpath)))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, header_page_xpath)))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, home_header_option_xpath)))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, home_header_practice_option_xpath)))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, home_header_courses_option_xpath)))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, home_header_blog_option_xpath)))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, home_header_contact_option_xpath)))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, title_page_xpath)))

    def fill_username_input(self, username,username_input):
        time.sleep(1)
        username_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, username_input)))
        username_input.clear()
        username_input.send_keys(username)
        
    def fill_password_input(self, password,password_input):
        time.sleep(1)
        password_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, password_input)))
        password_input.clear()
        password_input.send_keys(password)


def login_successfully(self, username, username_input,password,password_input):
    self.driver.get('https://practicetestautomation.com/practice-test-login/')
    self.driver.maximize_window()
    self.fill_username_input(username,username_input)
    self.fill_password_input(password,password_input)