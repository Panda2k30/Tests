from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Nintondo.AutoTests.pages.base_page import BasePage

wait = WebDriverWait

class SendPageSelector:

    # INPUTS
    ADDRESS_INPUT = (By.XPATH, "//span[text()='Address']/ancestor::div//input")
    AMOUNT_INPUT = (By.XPATH, "//input[@placeholder='Amount to send']")

    # BUTTONS
    FEE_SLOW_BTN = (By.XPATH, "//div[text()='Slow']")
    FEE_FAST_BTN = (By.XPATH, "//div[text()='Fast']")
    FEE_CUSTOM_BTN = (By.XPATH, "//div[text()='Custom']")
    CONTINUE_BUTTON = (By.XPATH, "//button[text()='Continue']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Confirm']")
    BACK_BUTTON = (By.XPATH, "//a[text()='Back']")

    INCLUDE_FEE = (By.XPATH, "//button[following-sibling::label[contains(text(), 'Include fee in the amount')]]")
    SAVE_ADDRESS = (By.XPATH, "//button[following-sibling::label[contains(text(), 'Save address for the next payments')]]")

class SendPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def enter_address(self, valid_address):
        enter_address = wait(self.driver, 10).until(
            EC.element_to_be_clickable(SendPageSelector.ADDRESS_INPUT))
        enter_address.send_keys(valid_address)
        print("- Enter a valid address")

    def enter_amount(self, valid_amount):
        enter_amount = wait(self.driver, 10).until(
            EC.element_to_be_clickable(SendPageSelector.AMOUNT_INPUT))
        enter_amount.send_keys(valid_amount)
        print("- Entered the amount to be transferred")

    def include_fee(self):
        # Include the commission in the amount
        include_fee = wait(self.driver, 10).until(
            EC.element_to_be_clickable(SendPageSelector.INCLUDE_FEE))
        include_fee.click()
        print("- Included the commission in the amount")

    def save_address(self):
        # Save the address in the book
        save_address = wait(self.driver, 10).until(
            EC.element_to_be_clickable(SendPageSelector.SAVE_ADDRESS))
        save_address.click()
        print("- Kept the address in the book.")

    def cont_send_money(self):
        # Confirm sending funds from the wallet
        cont_send_money = wait(self.driver, 10).until(
            EC.element_to_be_clickable(SendPageSelector.CONTINUE_BUTTON))
        cont_send_money.click()
        print("- Clicked on: Continue")

    def conf_send_money(self):
        # Confirm sending funds from the wallet
        conf_send_money = wait(self.driver, 10).until(
            EC.element_to_be_clickable(SendPageSelector.CONFIRM_BUTTON))
        conf_send_money.click()
        print("- Clicked on: Confirm")

    def back_to_home(self):
        back_to_home = wait(self.driver, 10).until(
            EC.element_to_be_clickable(SendPageSelector.BACK_BUTTON))
        back_to_home.click()
        print("- Clicked on: Back to Home")