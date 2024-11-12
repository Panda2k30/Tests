import time

import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Nintondo.AutoTests.pages.base_page import BasePage

wait = WebDriverWait

class LoginPageSelectors:
    PASSWORD_FIELD = (By.XPATH, '//input[@id="password"]')
    CONF_PASSWORD_FIELD = (By.XPATH, '//input[@id="confirmPassword"]')
    REG_BUTTON = (By.XPATH, "//button[text()='Create password']")

    # Types of wallet recovery
    NEW_MNEMONIC = (By.LINK_TEXT, "New mnemonic")
    RESTORE_MNEMONIC = (By.LINK_TEXT, "Restore mnemonic")
    PRIVAT_KEY = (By.LINK_TEXT, "Restore from private key")

    COPY_MNEMONIC = (By.XPATH, "//div[@id='root']//button")
    CONF_MNEMONIC = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/button")
    CREATE_BUTTON = (By.XPATH, "//button[text()='Continue']")
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Recover']")

    RESTORE_INPUT = (By.XPATH, "//input[@id='privKey']")
    RESTORE_MNEMONIC_INPUT = (By.XPATH, "//input[@class='_input_u2hpt_1']")
    RESTORE_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/button")

    LEGACY_TYPE = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div/div[2]")
    NATIVE_SEGWIT = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]")


class CreateMnemonic(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def enter_password(self, password):
        password_field = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.PASSWORD_FIELD))
        password_field.send_keys(password)
        print("- Enter a valid password")

    def conf_password(self, confpassword):
        confpassword_field = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.CONF_PASSWORD_FIELD))
        confpassword_field.send_keys(confpassword)
        print("- Confirmed password")

    def click_reg_button(self):
        reg_button = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.REG_BUTTON))
        reg_button.click()
        print("- Clicked on the button: Create password")

    def type_reg_new_mnem(self):
        type_reg = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.NEW_MNEMONIC))
        type_reg.click()
        print("- Clicked on: New mnemonic.")

    def type_reg_privacy_key(self):
        type_reg_privacy_key = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.PRIVAT_KEY))
        type_reg_privacy_key.click()
        print("- Clicked recovery via private key")

    def type_reg_mnemonic(self):
        type_reg_mnemonic = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.RESTORE_MNEMONIC))
        type_reg_mnemonic.click()
        print("- Clicked recovery through the mnemonic")

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

        print("- Entered seed phrases into the fields")

    def show_words(self):
        copy_mnem = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.COPY_MNEMONIC))
        copy_mnem.click()
        print("- Copied the phrases to the clipboard")

    def paste_mnen(self):
        clipboard_text = pyperclip.paste()
        print("Your phrases:", clipboard_text)

    def conf_save(self):
        conf_save = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.CONF_MNEMONIC))
        conf_save.click()
        print("- Confirmed phrase retention")

    def conf_create_wallet(self):
        createbtn_mnemonic = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.CREATE_BUTTON))
        createbtn_mnemonic.click()
        print("- Clicked on: Continue")

    def choose_type_legacy(self):
        legacy_type = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.LEGACY_TYPE))
        legacy_type.click()
        print("- Chosen: Legacy Type")

    def choose_type_native(self):
        choose_type_native = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.NATIVE_SEGWIT))
        choose_type_native.click()
        print("- Chosen: Native Segwit")

    def conf_create_wallet(self):
        createbtn_mnemonic = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.CREATE_BUTTON))
        createbtn_mnemonic.click()
        print("- Confirmed the creation of the wallet")

    def conf_recover_wallet(self):
        conf_recover_wallet = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.RECOVER_BUTTON))
        conf_recover_wallet.click()
        print("- Clicked on: Recover")

    def restore_input(self, privat_key):

        restore_input = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.RESTORE_INPUT))
        restore_input.send_keys(privat_key)
        print("- Entered a private key")

    def click_restore_button(self):
        # Confirm wallet recovery by mnemonics
        click_restore_button = wait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageSelectors.RESTORE_BUTTON))
        click_restore_button.click()
        print("- Click on the button: Continue")

    def exec_id(self):
        self.ex_id = self.driver.execute_script("return window.location.host;")

        print("\nCurrent ID:", self.ex_id)
        return self.ex_id

    def use_id(self):
        self.driver.get(f'chrome-extension:{self.ex_id}/index.html')



