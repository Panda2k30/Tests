from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from autotests.pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
import allure

wait = WebDriverWait

class ProfilePageSelector:
 
    AVATAR = (By.XPATH, "/html/body/main/div/div[1]/div[1]")
    NICKNAME = (By.XPATH, "/html/body/main/div/div[1]/div[2]/div[1]/div/div[2]")
    NICKNAME_FIELD = (By.XPATH, "//*[@id='input-form']/input")
    NICKNAME_SAVE_BTN = (By.XPATH, "//button[text()='Save']")

    WALLET_ADDRESS = (By.XPATH, "/html/body/main/div/div[1]/div[2]/div[1]/h3")
    BALANCE = (By.XPATH, "/html/body/main/div/div[1]/div[2]/div[2]/div[1]/span[2]")

    INSCRIPTIONS = (By.XPATH, "/html/body/main/div/div[3]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/img")
    INSCRIPTIONS_COUNT = (By.XPATH, "")

    INSCRIPTIONS_LIST = (By.XPATH, "//button/span[text()='List']")
    INSCRIPTIONS_SEND = (By.XPATH, "//button/span[text()='Send']")
    INSCRIPTIONS_UNLIST = (By.XPATH, "//button/span[text()='Unlist']")

    INSCRIPTIONS_FIELD_PRICE = (By.XPATH, "/html/body/div[5]/div/div/div/div/div/div/div[3]/div[1]/div[1]/input")
    INSCRIPTIONS_LIST_BTN = (By.XPATH, "//button[text()='List']")
    INSCRIPTIONS_SIGN_BTN = (By.XPATH, "//button[text()='Sign']")

    INSCRIPTIONS_UNLIST_BTN = (By.XPATH, "//button[text()='Unlist']")


class ProfilePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def profile_btn(self):
        avatar_btn = wait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.AVATAR))
        avatar_btn.click()
        allure.attach("Clicked on: User Photo", name="Avatar Button Action", attachment_type=allure.attachment_type.TEXT)

    def nickname_btn(self):
        nickname_btn = wait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.NICKNAME))
        nickname_btn.click()
        allure.attach("Clicked on: Change nickname", name="Nickname Button Action", attachment_type=allure.attachment_type.TEXT)

    def nickname_field(self, nickname):
        nickname_field = wait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.NICKNAME_FIELD))

        nickname_field.clear()
        nickname_field.send_keys(nickname)

        allure.attach(f"Entered nickname: {nickname}", name="Nickname Field Action", attachment_type=allure.attachment_type.TEXT)

    def nickname_save_btn(self):
        nickname_save_btn = wait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.NICKNAME_SAVE_BTN))
        nickname_save_btn.click()
        allure.attach("Clicked on: Change nickname", name="Save Nickname Button Action", attachment_type=allure.attachment_type.TEXT)


class Inscriptions(BasePage):

    def select_inscription(self):
        select_inscription = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ProfilePageSelector.INSCRIPTIONS)
        )

        actions = ActionChains(self.driver)
        actions.move_to_element(select_inscription).click(select_inscription).perform()

        allure.attach("Clicked on: The First Inscription", name="Select Inscription Action", attachment_type=allure.attachment_type.TEXT)

    def inscription_list(self):
        inscription_list = wait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.INSCRIPTIONS_LIST))
        inscription_list.click()
        allure.attach("Clicked on: List", name="Inscription List Action", attachment_type=allure.attachment_type.TEXT)

    def inscription_send(self):
        inscription_send = wait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.INSCRIPTIONS_SEND))
        inscription_send.click()
        allure.attach("Clicked on: Send", name="Send Inscription Action", attachment_type=allure.attachment_type.TEXT)

    def inscription_unlist(self):
        inscription_unlist = wait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.INSCRIPTIONS_UNLIST))
        inscription_unlist.click()
        allure.attach("Clicked on: Unlist", name="Unlist Inscription Action", attachment_type=allure.attachment_type.TEXT)

    def inscription_field_price(self):
        inscription_field_price = wait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.INSCRIPTIONS_FIELD_PRICE))
        inscription_field_price.send_keys("1")
        allure.attach("Entered the cost in the field", name="Price Field Action", attachment_type=allure.attachment_type.TEXT)

    def inscription_field_invalid_price(self, amount):
        inscription_field_invalid_price = wait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.INSCRIPTIONS_FIELD_PRICE))
        inscription_field_invalid_price.send_keys(amount)
        allure.attach(f"Entered a non-valid value: {amount} in the field", name="Invalid Price Field Action", attachment_type=allure.attachment_type.TEXT)

    def inscription_list_btn(self):
        inscription_list_btn = wait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.INSCRIPTIONS_LIST_BTN))
        inscription_list_btn.click()
        allure.attach("Clicked on: List", name="List Button Action", attachment_type=allure.attachment_type.TEXT)

    def inscription_unlist_btn(self):
        inscription_unlist_btn = wait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.INSCRIPTIONS_UNLIST_BTN))
        inscription_unlist_btn.click()
        allure.attach("Clicked on: Unlist", name="Unlist Button Action", attachment_type=allure.attachment_type.TEXT)

    def sign_btn(self):
        sign_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ProfilePageSelector.INSCRIPTIONS_SIGN_BTN))
        sign_btn.click()
        allure.attach("In the second window clicked: Sign", name="Sign Button Action", attachment_type=allure.attachment_type.TEXT)