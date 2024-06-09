import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    LOGIN_URL = os.getenv('LOGIN_URL2')  # Corrección aquí
    USERNAME_INPUT_XPATH = os.getenv('USERNAME_INPUT_XPATH2')
    PASSWORD_INPUT_XPATH = os.getenv('PASSWORD_INPUT_XPATH2')
    SUBMIT_BUTTON_XPATH = os.getenv('SUBMIT_BUTTON_XPATH2')
    PRODUCTS_HEADER_XPATH = os.getenv('PRODUCTS_HEADER_XPATH')
    USERNAME = os.getenv('USERNAME2')
    PASSWORD = os.getenv('PASSWORD2')
    
    @classmethod
    def validate(cls):
        variables = {
            'LOGIN_URL2': cls.LOGIN_URL,
            'USERNAME_INPUT_XPATH2': cls.USERNAME_INPUT_XPATH,
            'PASSWORD_INPUT_XPATH2': cls.PASSWORD_INPUT_XPATH,
            'SUBMIT_BUTTON_XPATH2': cls.SUBMIT_BUTTON_XPATH,
            'PRODUCTS_HEADER_XPATH': cls.PRODUCTS_HEADER_XPATH,
            'USERNAME2': cls.USERNAME,
            'PASSWORD2': cls.PASSWORD,
        }
        
        for var_name, var_value in variables.items():
            if var_value is None:
                raise ValueError(f"Environment variable {var_name} is not set.")

# Validate configuration at the import time
Config.validate()
