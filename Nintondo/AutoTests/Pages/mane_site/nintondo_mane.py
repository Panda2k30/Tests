from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Nintondo.AutoTests.conftest import driver
from Nintondo.AutoTests.Pages.base_page import BasePage

wait = WebDriverWait

class NintondoPageSelector:

    CONNECT_BTN = (By.XPATH, "/html/body/div[1]/nav[2]/div[2]/button")
    SIGN_BTN = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[3]/button[1]")
    CHANGE_NETWORK = (By.XPATH, "/html/body/div[1]/nav[1]/div[1]/span")
    SWITCH_NETWORK = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[3]/button[1]")

    OPEN_MENU = (By.XPATH, "/html/body/div[1]/nav[1]/div[3]/div/div/button")
    PROFILE_BNT = (By.XPATH, "/html/body/div[4]/div/div/div[2]/a[1]")

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

    def switch_network_btn(self):
        switch_network_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NintondoPageSelector.SWITCH_NETWORK))
        switch_network_btn.click()
        print("- Поменяли сеть")

class NintondoUserMenu(BasePage):
    def __init__(self, driver):
        self.driver = driver  # Сохраняем переданный драйвер

    def open_menu(self):
        open_menu = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NintondoPageSelector.OPEN_MENU))
        open_menu.click()
        print("- Кликнули на раскрытие меню")

    def menu_profile_btn(self):
        menu_profile_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NintondoPageSelector.PROFILE_BNT))
        menu_profile_btn.click()
        print("- Кликнули на: Profile")
