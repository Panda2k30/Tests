import time
import random
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from autotests.pages.base_page import BasePage
from faker import Faker

fake = Faker()
wait = WebDriverWait

class LoginPageSelectors:
    PASSWORD_FIELD = (By.XPATH, '//input[@id="password"]')
    CONF_PASSWORD_FIELD = (By.XPATH, '//input[@id="confirmPassword"]')
    REG_BUTTON = (By.XPATH, "//button[text()='Create password']")

    # Types of wallet recovery
    NEW_MNEMONIC = (By.LINK_TEXT, "New mnemonic")
    RESTORE_MNEMONIC = (By.LINK_TEXT, "Restore mnemonic")
    PRIVATE_KEY = (By.LINK_TEXT, "Restore from private key")

    COPY_MNEMONIC = (By.XPATH, "//div[@id='root']//button")
    CONF_MNEMONIC = INCLUDE_FEE = (By.XPATH, "//button[following-sibling::label[contains(text(), 'I saved this phrase')]]")
    CREATE_BUTTON = (By.XPATH, "//button[text()='Continue']")
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Recover']")

    RESTORE_INPUT = (By.XPATH, "//input[@id='privKey']")
    RESTORE_MNEMONIC_INPUT = (By.XPATH, "//input[contains(@class, '_input_')]")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Continue']")

    LEGACY_TYPE = (By.XPATH, "//div[text()='Legacy']")
    NATIVE_SEGWIT = (By.XPATH, "//div[text()='Taproot']")


class CreateMnemonic(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.fake = Faker()

    def enter_invalid_password(self, password):
        password_field = wait(self.driver, 2).until(
            EC.element_to_be_clickable(LoginPageSelectors.PASSWORD_FIELD))
        password_field.send_keys(password)
        allure.attach("- Enter a valid password", name="Action", attachment_type=allure.attachment_type.TEXT)

    def enter_password(self):
        password_length = random.randint(10, 50)
        password = self.fake.password(length=password_length, special_chars=True, digits=True, upper_case=True)

        password_field = wait(self.driver, 5).until(
            EC.element_to_be_clickable(LoginPageSelectors.PASSWORD_FIELD))

        password_field.send_keys(password)
        
        allure.attach(f"Entered a password of length {password_length}: {password}", name="Password", attachment_type=allure.attachment_type.TEXT)

        return password

    def conf_password(self, confpassword):
        confpassword_field = wait(self.driver, 2).until(
            EC.element_to_be_clickable(LoginPageSelectors.CONF_PASSWORD_FIELD))
        confpassword_field.send_keys(confpassword)
        allure.attach("- Confirmed password", name="Action", attachment_type=allure.attachment_type.TEXT)

    def click_reg_button(self):
        reg_button = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.REG_BUTTON))
        reg_button.click()
        allure.attach("- Clicked on the button: Create password", name="Action", attachment_type=allure.attachment_type.TEXT)

    def type_reg_new_mnem(self):
        type_reg = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.NEW_MNEMONIC))
        type_reg.click()
        allure.attach("- Clicked on: New mnemonic.", name="Action", attachment_type=allure.attachment_type.TEXT)

    def type_reg_privacy_key(self):
        type_reg_privacy_key = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.PRIVATE_KEY))
        type_reg_privacy_key.click()
        allure.attach("- Clicked recovery via private key", name="Action", attachment_type=allure.attachment_type.TEXT)

    def type_reg_mnemonic(self):
        type_reg_mnemonic = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.RESTORE_MNEMONIC))
        type_reg_mnemonic.click()
        allure.attach("- Clicked recovery through the mnemonic", name="Action", attachment_type=allure.attachment_type.TEXT)

    def type_reg_restore_mnem(self, mnemonic):
        input_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.RESTORE_MNEMONIC_INPUT)
        )

        for word in mnemonic:
            for char in word:
                input_field.send_keys(char)
                time.sleep(0.001)

            input_field.send_keys(Keys.TAB)
            input_field = self.driver.switch_to.active_element

        allure.attach("- Entered seed phrases into the fields", name="Action", attachment_type=allure.attachment_type.TEXT)

    def conf_save(self):
        conf_save = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.CONF_MNEMONIC))
        conf_save.click()
        allure.attach("- Confirmed phrase retention", name="Action", attachment_type=allure.attachment_type.TEXT)

    def conf_create_wallet(self):
        createbtn_mnemonic = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.CREATE_BUTTON))
        createbtn_mnemonic.click()
        allure.attach("- Clicked on: Continue", name="Action", attachment_type=allure.attachment_type.TEXT)

    def choose_type_legacy(self):
        legacy_type = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.LEGACY_TYPE))
        legacy_type.click()
        allure.attach("- Chosen: Legacy Type", name="Action", attachment_type=allure.attachment_type.TEXT)

    def choose_type_native(self):
        choose_type_native = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.NATIVE_SEGWIT))
        choose_type_native.click()
        allure.attach("- Chosen: Native Segwit", name="Action", attachment_type=allure.attachment_type.TEXT)

    def conf_create_wallet(self):
        createbtn_mnemonic = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.CREATE_BUTTON))
        createbtn_mnemonic.click()
        allure.attach("- Confirmed the creation of the wallet", name="Action", attachment_type=allure.attachment_type.TEXT)

    def conf_recover_wallet(self):
        conf_recover_wallet = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.RECOVER_BUTTON))
        conf_recover_wallet.click()
        allure.attach("- Clicked on: Recover", name="Action", attachment_type=allure.attachment_type.TEXT)

    def restore_input(self, privat_key):
        restore_input = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.RESTORE_INPUT))
        restore_input.send_keys(privat_key)
        allure.attach("- Entered a private key", name="Action", attachment_type=allure.attachment_type.TEXT)

    def click_restore_button(self):
        click_restore_button = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.RESTORE_BUTTON))
        click_restore_button.click()
        allure.attach("- Click on the button: Continue", name="Action", attachment_type=allure.attachment_type.TEXT)

    def exec_id(self):
        self.ex_id = self.driver.execute_script("return window.location.host;")
        allure.attach(f"Current ID: {self.ex_id}", name="Current ID", attachment_type=allure.attachment_type.TEXT)
        return self.ex_id

    def use_id(self):
        self.driver.get(f'chrome-extension:{self.ex_id}/index.html')



