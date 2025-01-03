from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from autotests.pages.base_page import BasePage
from faker import Faker
import random
import allure

fake = Faker()
wait = WebDriverWait


class SettingsPageSelector:
    
    # Settings
    SECURITY_SETTINGS = (By.XPATH, "//div[text()='Security Settings']")
    WALLET_SETTINGS = (By.XPATH, "//div[text()='Wallet Settings']")
    
    # Security
    CHANGE_PASSWORD = (By.XPATH, "//div[text()='Change Password']")
    
    # Change Password
    OLD_PASSWORD = (By.XPATH, "//input[@id='oldPassword']")
    NEW_PASSWORD = (By.XPATH, "//input[@id='password']")
    CONFIRM_PASSWORD = (By.XPATH, "//input[@id='confirmPassword']")
    CHANGE_PASSWORD_BTN = (By.XPATH, "//button[text()='Change password']")
    
    # Wallet Settings
    NETWORK_SETTINGS = (By.XPATH, "//div[text()='Network Settings']")
    ADDRESS_TYPE = (By.XPATH, "//div[text()='Address Type']")
    
    # Network Settings
    TESTNET_BTN = (By.XPATH, "//div[text()='TESTNET']")
    MAINNET_BTN = (By.XPATH, "//div[text()='MAINNET']")
    
    # Address Type
    SEGWIT = (By.XPATH, "//div[text()='Native Segwit']")
    LEGACY = (By.XPATH, "//div[text()='Legacy']")
    

class SettingsSecurity(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.fake = Faker()

    def security_page(self):
        security_page = wait(self.driver, 10).until(
            EC.element_to_be_clickable(SettingsPageSelector.SECURITY_SETTINGS))
        security_page.click()
        allure.attach("- Go to the page: Security Settings", name="Action", attachment_type=allure.attachment_type.TEXT)
  
       
class ChangePassword(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.fake = Faker()

    def change_password_page(self):
        change_password_page = wait(self.driver, 10).until(
            EC.element_to_be_clickable(SettingsPageSelector.CHANGE_PASSWORD))
        change_password_page.click()
        allure.attach("- Go to the page: Change password", name="Action", attachment_type=allure.attachment_type.TEXT)
        
    def old_password(self, oldpassword):
        old_password = wait(self.driver, 10).until(
            EC.element_to_be_clickable(SettingsPageSelector.OLD_PASSWORD))
        old_password.send_keys(oldpassword)
        allure.attach("- Entered old password", name="Action", attachment_type=allure.attachment_type.TEXT)
        
    def new_password(self):
        password_length = random.randint(10, 50)
        new_password = self.fake.password(length=password_length, special_chars=True, digits=True, upper_case=True)

        password_field = wait(self.driver, 10).until(
            EC.element_to_be_clickable(SettingsPageSelector.NEW_PASSWORD))

        password_field.send_keys(new_password)
        
        allure.attach(f"- Entered a password of length {password_length}: {new_password}", name="Action", attachment_type=allure.attachment_type.TEXT)

        return new_password
    
    def test_password(self, new_pass):
        test_password = wait(self.driver, 10).until(
            EC.element_to_be_clickable(SettingsPageSelector.NEW_PASSWORD))
        test_password.send_keys(new_pass)
        allure.attach("- Entered conf password", name="Action", attachment_type=allure.attachment_type.TEXT)        
    
    def conf_password(self, confpassword):
        conf_password = wait(self.driver, 10).until(
            EC.element_to_be_clickable(SettingsPageSelector.CONFIRM_PASSWORD))
        conf_password.send_keys(confpassword)
        allure.attach("- Entered conf password", name="Action", attachment_type=allure.attachment_type.TEXT)
    
    def conf_btn(self):
        conf_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(SettingsPageSelector.CHANGE_PASSWORD_BTN))
        conf_btn.click()
        allure.attach("- Clicked: Change Password", name="Action", attachment_type=allure.attachment_type.TEXT)

        
class WalletSettings(BasePage):
    def __init__(self, driver):
        self.driver = driver
        
    def change_network(self, ex_id):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//p[text()='No transactions']")))

        self.driver.get(f"chrome-extension://{ex_id}/index.html#/pages/network-settings")
        allure.attach("- Go to the page for changing the network type", name="Action", attachment_type=allure.attachment_type.TEXT)

        change_network = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(SettingsPageSelector.TESTNET_BTN)
        )
        change_network.click()
        allure.attach("- Changed the network to TESTNET", name="Action", attachment_type=allure.attachment_type.TEXT)
        
    def change_type_legacy(self):
        wallet_settings = wait(self.driver, 10).until(
            EC.element_to_be_clickable(SettingsPageSelector.WALLET_SETTINGS))
        wallet_settings.click()
        
        address_type = wait(self.driver, 10).until(
            EC.element_to_be_clickable(SettingsPageSelector.ADDRESS_TYPE))
        address_type.click()
        
        segwit_type = wait(self.driver, 10).until(
            EC.element_to_be_clickable(SettingsPageSelector.LEGACY))
        segwit_type.click()
        allure.attach("- Chosen: Legacy", name="Action", attachment_type=allure.attachment_type.TEXT)

    