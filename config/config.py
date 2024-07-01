import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    LOGIN_SAUCEDEMO_URL = os.getenv('LOGIN_SAUCEDEMO_URL')
    USERNAME_INPUT_XPATH = os.getenv('USERNAME_INPUT_XPATH')
    PASSWORD_INPUT_XPATH = os.getenv('PASSWORD_INPUT_XPATH')
    SUBMIT_BUTTON_XPATH = os.getenv('SUBMIT_BUTTON_XPATH')
    PRODUCTS_HEADER_XPATH = os.getenv('PRODUCTS_HEADER_XPATH')
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    INVALID_USERNAME = os.getenv('INVALID_USERNAME')
    INVALID_PASSWORD = os.getenv('INVALID_PASSWORD')
    INVALID_MESSAGE_XPATH = os.getenv('INVALID_MESSAGE_XPATH')
    EMPTY_MESSAGE_XPATH= os.getenv('EMPTY_MESSAGE_XPATH')
    MENU_BUTTON_XPATH = os.getenv('MENU_BUTTON_XPATH')
    ABOUT_LINK= os.getenv('ABOUT_LINK_XPATH')
    LOGO_SAUSELABS_XPATH = os.getenv('LOGO_SAUSLABS_XPATH')
    LOGOUT_BUTTON_XPATH = os.getenv('LOGOUT_BUTTON_XPATH')
    LOGO_PAGE_XPATH = os.getenv('LOGO_PAGE_XPATH')

    @classmethod
    def validate(cls):
        variables = {
            'LOGIN_SAUCEDEMO_URL': cls.LOGIN_SAUCEDEMO_URL,
            'USERNAME_INPUT_XPATH': cls.USERNAME_INPUT_XPATH,
            'PASSWORD_INPUT_XPATH': cls.PASSWORD_INPUT_XPATH,
            'SUBMIT_BUTTON_XPATH': cls.SUBMIT_BUTTON_XPATH,
            'PRODUCTS_HEADER_XPATH': cls.PRODUCTS_HEADER_XPATH,
            'USERNAME': cls.USERNAME,
            'PASSWORD': cls.PASSWORD,
            'INVALID_USERNAME': cls.INVALID_USERNAME,
            'INVALID_PASSWORD': cls.INVALID_PASSWORD,
            'ERROR_MESSAGE_XPATH': cls.INVALID_MESSAGE_XPATH,
            'EMPTY_FIELD_ERROR_MESSAGE_XPATH': cls.EMPTY_MESSAGE_XPATH,
            'MENU_BUTTON_XPATH': cls.MENU_BUTTON_XPATH,
            'ABOUT_LINK_XPATH': cls.ABOUT_LINK,
            'LOGO_SAUSLABS_XPATH': cls.LOGO_SAUSELABS_XPATH,
            'LOGOUT_BUTTON_XPATH': cls.LOGOUT_BUTTON_XPATH,
            'LOGO_PAGE_XPATH': cls.LOGO_PAGE_XPATH,
        }

        for var_name, var_value in variables.items():
            if var_value is None:
                raise ValueError(f"Environment variable {var_name} is not set.")

Config.validate()
