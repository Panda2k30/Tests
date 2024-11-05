from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Nintondo.AutoTests.conftest import driver
from Nintondo.AutoTests.Pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

wait = WebDriverWait

class ProfilePageSelector:

    AVATAR = (By.XPATH, "/html/body/main/div/div[1]/div[1]")
    NICKNAME = (By.XPATH, "/html/body/main/div/div[1]/div[2]/div[1]/div/div[2]")
    NICKNAME_FIELD = (By.XPATH, "//*[@id='input-form']/input")
    NICKNAME_SAVE_BTN = (By.XPATH, "//button[text()='Save']")

    WALLET_ADDRESS = (By.XPATH, "/html/body/main/div/div[1]/div[2]/div[1]/h3")
    BALANCE = (By.XPATH, "/html/body/main/div/div[1]/div[2]/div[2]/div[1]/span[2]")

    INSCRIPTIONS = (By.XPATH, "/html/body/main/div/div[3]/div/div[2]/div[2]/div/div[1]/div[1]/img")
    INSCRIPTIONS_COUNT = (By.XPATH, "")

    INSCRIPTIONS_LIST = (By.XPATH, "//button/span[text()='List']")
    INSCRIPTIONS_SEND = (By.XPATH, "//button/span[text()='Send']")
    INSCRIPTIONS_UNLIST = (By.XPATH, "//button/span[text()='Unlist']")

    INSCRIPTIONS_FIELD_PRICE = (By.XPATH, "/html/body/div[4]/div/div/div/div/div/div/div[3]/div[1]/div[1]/input")
    INSCRIPTIONS_LIST_BTN = (By.XPATH, "//button[text()='List']")
    INSCRIPTIONS_SIGN_BTN = (By.XPATH, "//button[text()='Sign']")

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

    def nickname_field(self, nickname):
        nickname_field = wait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.NICKNAME_FIELD))

        nickname_field.clear()
        nickname_field.send_keys(nickname)

        print("- Кликнули на: Поле ввода")

    def nickname_save_btn(self):
        nickname_save_btn = wait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.NICKNAME_SAVE_BTN))
        nickname_save_btn.click()
        print("- Кликнули на: Change nickname")

class Inscriptions(BasePage):

    def select_inscription(self):
        # Ожидание кликабельности элемента
        select_inscription = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ProfilePageSelector.INSCRIPTIONS)
        )

        # Используем ActionChains для наведения и клика по элементу
        actions = ActionChains(self.driver)
        actions.move_to_element(select_inscription).click(select_inscription).perform()

        print("- Кликнули на: Первую инскрипцию")

    def inscription_list(self):
        inscription_list = wait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.INSCRIPTIONS_LIST))
        inscription_list.click()
        print("- Кликнули на: List")

    def inscription_send(self):
        inscription_send = wait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.INSCRIPTIONS_SEND))
        inscription_send.click()
        print("- Кликнули на: Send")

    def inscription_unlist(self):
        inscription_unlist = wait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.INSCRIPTIONS_UNLIST))
        inscription_unlist.click()
        print("- Кликнули на: Unlist")

    def inscription_field_price(self):
        inscription_field_price = wait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.INSCRIPTIONS_FIELD_PRICE))
        inscription_field_price.send_keys("1")
        print("- Ввели в поле стоимость")

    def inscription_list_btn(self):
        inscription_list_btn = wait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.INSCRIPTIONS_LIST_BTN))
        inscription_list_btn.click()
        print("- Ввели в поле стоимость")

    def sign_btn(self):
        sign_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ProfilePageSelector.INSCRIPTIONS_SIGN_BTN))
        sign_btn.click()
        print("- Во втором окне кликнули: Sign")