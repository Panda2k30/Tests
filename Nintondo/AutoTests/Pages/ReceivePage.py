import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Nintondo.AutoTests.conftest import driver
from .Base_page import BasePage

wait = WebDriverWait

class ReceivePageSelector:

    WALLET_ADDRESS_TEXT = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div/div/div[2]")
    WALLET_ADDRESS_COPY_BTN = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div/button")
    WALLET_ADDRESS_QR = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div/div/div[1]")


class ReceivePage(BasePage):
    def __init__(self, driver):
        self.driver = driver  # Сохраняем переданный драйвер

    def receive_address_text(self):
        receive_address_text = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ReceivePageSelector.WALLET_ADDRESS_TEXT))
        receive_address_text.click()
        print("- ")
        text_address = receive_address_text.text
        print("Адрес из строки:", text_address)
        return text_address

    def receive_address_btn(self):
        receive_address_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ReceivePageSelector.WALLET_ADDRESS_COPY_BTN))
        receive_address_btn.click()
        print("- Кликнули на: Copy Address ")

        btn_address = pyperclip.paste().strip()
        print("Адрес из кнопки:", btn_address)
        return btn_address

    def receive_address_qr(self):
        receive_address_qr = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ReceivePageSelector.WALLET_ADDRESS_QR))
        receive_address_qr.click()
        print("- Кликнули на: QR copy image")