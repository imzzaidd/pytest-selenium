import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from config.config import Config
from selenium.webdriver.support.ui import Select

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class InventoryView:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def load_page(self):
        
        try:
            self.driver.get(Config.LOGIN_SAUCEDEMO_URL)
            self.driver.maximize_window()
            logger.info("Login page cargada con éxito.")
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
    def go_back(self):
        self.driver.back()
        logger.info("Go back to previous page")

    def select_by_value(self, xpath, value):
        try:
            select = Select(self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath))))
            select.select_by_value(value)
            logger.info(f"Selected {value} from dropdown {xpath}")
        except Exception as e:
            logger.error(f"Error selecting {value} from dropdown {xpath}.", exc_info=True)
            raise e

    

    
        
