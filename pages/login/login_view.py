import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from config.config import Config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LoginView:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def load_page(self):
        try:
            self.driver.get(Config.LOGIN_SAUCEDEMO_URL)
            self.driver.maximize_window()
            logger.info("Login page loaded successfully.")
        except Exception as e:
            logger.error("Failed to load login page.", exc_info=True)
            raise e

    def fill_input(self, xpath, value):
        try:
            input_field = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            input_field.clear()
            input_field.send_keys(value)
            logger.info(f"Filled input field {xpath} with value: {value}")
        except TimeoutException:
            logger.error(f"Timeout while waiting for input field {xpath}.", exc_info=True)
            raise
        except Exception as e:
            logger.error(f"Error filling input field {xpath} with value: {value}.", exc_info=True)
            raise e

    def click_element(self, xpath):
        try:
            element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()
            logger.info(f"Clicked element {xpath}")
        except TimeoutException:
            logger.error(f"Timeout while waiting for element {xpath} to be clickable.", exc_info=True)
            raise
        except Exception as e:
            logger.error(f"Error clicking element {xpath}.", exc_info=True)
            raise e

    def is_element_visible(self, xpath):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            logger.info(f"Element {xpath} is visible.")
            return True
        except TimeoutException:
            logger.warning(f"Element {xpath} is not visible (timeout).")
            return False
        except NoSuchElementException:
            logger.warning(f"Element {xpath} is not visible (no such element).")
            return False
        except Exception as e:
            logger.error(f"Error checking visibility of element {xpath}.", exc_info=True)
            raise e

    def login_success(self, username, password):
        self.load_page()
        self.fill_input(Config.USERNAME_INPUT_XPATH, username)
        self.fill_input(Config.PASSWORD_INPUT_XPATH, password)
        self.click_element(Config.SUBMIT_BUTTON_XPATH)
        return self.is_element_visible(Config.PRODUCTS_HEADER_XPATH)
    
    def login_failure(self, invalid_username, invalid_password):
        self.load_page()
        self.fill_input(Config.USERNAME_INPUT_XPATH, invalid_username)
        self.fill_input(Config.PASSWORD_INPUT_XPATH, invalid_password)
        self.click_element(Config.SUBMIT_BUTTON_XPATH)
        return not self.is_element_visible(Config.INVALID_MESSAGE_XPATH)

    def login_empty_fields(self, empty_username, empty_password):
        self.load_page()
        self.fill_input(Config.USERNAME_INPUT_XPATH, empty_username)
        self.fill_input(Config.PASSWORD_INPUT_XPATH, empty_password)
        self.click_element(Config.SUBMIT_BUTTON_XPATH)
        return not self.is_element_visible(Config.EMPTY_MESSAGE_XPATH)
    
    def login_empty_username(self, empty_username, password):
        self.load_page()
        self.fill_input(Config.USERNAME_INPUT_XPATH, empty_username)
        self.fill_input(Config.PASSWORD_INPUT_XPATH, password)
        self.click_element(Config.SUBMIT_BUTTON_XPATH)
        return not self.is_element_visible(Config.EMPTY_MESSAGE_XPATH)
    
    def login_empty_password(self, username, empty_password):
        self.load_page()
        self.fill_input(Config.USERNAME_INPUT_XPATH, username)
        self.fill_input(Config.PASSWORD_INPUT_XPATH, empty_password)
        self.click_element(Config.SUBMIT_BUTTON_XPATH)
        return not self.is_element_visible(Config.EMPTY_MESSAGE_XPATH)