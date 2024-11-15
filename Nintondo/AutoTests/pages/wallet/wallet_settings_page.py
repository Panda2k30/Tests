from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AutoTests.conftest import driver
from AutoTests.pages.base_page import BasePage
from faker import Faker
import random

fake = Faker()
wait = WebDriverWait


class SettingsPageSelector:
    
    # Settings
    SECURITY_SETTINGS = (By.XPATH, "//div[text()='Security Settings']")
    
    # Security
    CHANGE_PASSWORD = (By.XPATH, "//div[text()='Change Password']")
    
    # Change Password
    OLD_PASSWORD = (By.XPATH, "//input[@id='oldPassword']")
    NEW_PASSWORD = (By.XPATH, "//input[@id='password']")
    CONFIRM_PASSWORD = (By.XPATH, "//input[@id='confirmPassword']")
    
    CHANGE_PASSWORD_BTN = (By.XPATH, "//button[text()='Change password']")
    

class SettingsSecurity(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.fake = Faker()

    def security_page(self):
        security_page = wait(self.driver, 10).until(
            EC.element_to_be_clickable(SettingsPageSelector.SECURITY_SETTINGS))
        security_page.click()
        print("- Go to the page: Security Settings")

        
class ChangePassword(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.fake = Faker()

    def change_password_page(self):
        change_password_page = wait(self.driver, 10).until(
            EC.element_to_be_clickable(SettingsPageSelector.CHANGE_PASSWORD))
        change_password_page.click()
        print("- Go to the page: Change password")
        
    def old_password(self, oldpassword):
        old_password = wait(self.driver, 10).until(
            EC.element_to_be_clickable(SettingsPageSelector.OLD_PASSWORD))
        old_password.send_keys(oldpassword)
        print("- Inter old password")
        
    def new_password(self):
        
        password_length = random.randint(10, 50)
        new_password = self.fake.password(length=password_length, special_chars=True, digits=True, upper_case=True)

        password_field = wait(self.driver, 10).until(
            EC.element_to_be_clickable(SettingsPageSelector.NEW_PASSWORD))

        password_field.send_keys(new_password)
        
        print(f"- Entered a password of length {password_length}: {new_password}")

        return new_password
    
    def test_password(self, new_pass):
        test_password = wait(self.driver, 10).until(
            EC.element_to_be_clickable(SettingsPageSelector.NEW_PASSWORD))
        test_password.send_keys(new_pass)
        print("- Entered conf password")        
    
    def conf_password(self, confpassword):
        conf_password = wait(self.driver, 10).until(
            EC.element_to_be_clickable(SettingsPageSelector.CONFIRM_PASSWORD))
        conf_password.send_keys(confpassword)
        print("- Inter conf password")
    
    def conf_btn(self):
        conf_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(SettingsPageSelector.CHANGE_PASSWORD_BTN))
        conf_btn.click()
        print("- Clicked: Change Password")