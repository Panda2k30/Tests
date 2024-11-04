from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Nintondo.AutoTests.conftest import driver
from .Base_page import BasePage

wait = WebDriverWait

class ProfilePageSelector:

    AVATAR = (By.XPATH, "/html/body/main/div/div[1]/div[1]")
    NICKNAME = (By.XPATH, "/html/body/main/div/div[1]/div[2]/div[1]/div/div[2]")
    NICKNAME_FIELD = (By.XPATH, "//*[@id='input-form']/input")

    WALLET_ADDRESS = (By.XPATH, "/html/body/main/div/div[1]/div[2]/div[1]/h3")
    BALANCE = (By.XPATH, "/html/body/main/div/div[1]/div[2]/div[2]/div[1]/span[2]")

    INSCRIPTIONS = (By.XPATH, "")
    INSCRIPTIONS_COUNT = (By.XPATH, "")



class ProfilePage(BasePage):
    def __init__(self, driver):
        self.driver = driver  # Сохраняем переданный драйвер

    def profile_btn(self):
        avatar_btn = wait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.AVATAR))
        avatar_btn.click()
        print("- Кликнули на: User Photo")

    def nickname_btn(self):
        nickname_btn = wait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.NICKNAME))
        nickname_btn.click()
        print("- Кликнули на: Change nickname")

    def nickname_field(self):
        nickname_field = wait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.NICKNAME_FIELD))
        nickname_field.clear()
        print("- Кликнули на: Поле ввода")