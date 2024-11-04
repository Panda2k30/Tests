from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Nintondo.AutoTests.conftest import driver
from .Base_page import BasePage

wait = WebDriverWait

class NintondoPageSelector:

    CONNECT_BTN = (By.XPATH, "/html/body/div[1]/nav[2]/div[2]/button")
    SIGN_BTN = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[3]/button[1]")
    CHANGE_NETWORK = (By.XPATH, "/html/body/div[1]/nav[1]/div[1]/span")

class NintondoPage(BasePage):
    def __init__(self, driver):
        self.driver = driver  # Сохраняем переданный драйвер

    def connect_btn(self):
        connect_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NintondoPageSelector.CONNECT_BTN))
        connect_btn.click()
        print("- Кликнули на кнопку: Connect")

    def sign_btn(self):
        sign_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NintondoPageSelector.SIGN_BTN))
        sign_btn.click()
        print("- Во втором окне кликнули: Sign")

    def change_network_btn(self):
        change_network_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NintondoPageSelector.CHANGE_NETWORK))
        change_network_btn.click()
        print("- Поменяли сеть")