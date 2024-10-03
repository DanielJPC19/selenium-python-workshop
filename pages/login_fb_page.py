from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginFBPage(BasePage):
    USER_USERNAME = (By.ID, "username")
    USER_PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "loginbtn")
    
    def login(self, username, password):
        self.enter_text(self.USER_USERNAME, username)
        self.enter_text(self.USER_PASSWORD, password)
        self.click(self.LOGIN_BTN)