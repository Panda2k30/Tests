from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from autotests.pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import allure
import time

wait = WebDriverWait

class ProfilePageSelector:
 
    IMAGE = (By.XPATH, "/html/body/main/div/div[1]/div[1]")
    IMAGE_URL = (By. XPATH, "//div/img")
    IMAGE_FIELD = (By.XPATH, "//input[@placeholder='Inscription ID']")
    
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


class Image(BasePage):
    
    def image_btn(self):
        image_btn = wait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.IMAGE))
        image_btn.click()
        allure.attach("Clicked on: User Photo", name="Avatar Button Action", attachment_type=allure.attachment_type.TEXT)
    
    def image_url(self):
        time.sleep(0.5)
        image_url = wait(self.driver, 10).until(
                 EC.element_to_be_clickable(ProfilePageSelector.IMAGE_URL))
        image_url = image_url.get_attribute("src")
        allure.attach(f"Copy Image URL: {image_url}", name="Copy Image URL", attachment_type=allure.attachment_type.TEXT)
        return image_url
                
    def image_field(self, image_id):
        image_field = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ProfilePageSelector.IMAGE_FIELD))

        image_field.click()
        image_field.send_keys(Keys.CONTROL + "a")  # Выделяем весь текст
        image_field.send_keys(Keys.BACKSPACE)  # Удаляем весь текст
        image_field.send_keys(image_id)

        allure.attach(f"Entered image id (inscription): {image_id}", name="Image Field Action", attachment_type=allure.attachment_type.TEXT)
        
    def image_save_btn(self):
        image_save_btn = wait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.NICKNAME_SAVE_BTN))
        image_save_btn.click()
        allure.attach("Clicked on: Save", name="Save Image Button Action", attachment_type=allure.attachment_type.TEXT)


class Nickname(BasePage):

    def nickname_btn(self):
        time.sleep(0.4)
        nickname_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ProfilePageSelector.NICKNAME))
        nickname_btn.click()
        allure.attach("Clicked on: Change nickname", name="Nickname Button Action", attachment_type=allure.attachment_type.TEXT)

    def nickname_field(self, nickname):
        nickname_field = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ProfilePageSelector.NICKNAME_FIELD))

        nickname_field.click()
        nickname_field.send_keys(Keys.CONTROL + "a")
        nickname_field.send_keys(Keys.BACKSPACE)
        nickname_field.send_keys(nickname)

        allure.attach(f"Entered nickname: {nickname}", name="Nickname Field Action", attachment_type=allure.attachment_type.TEXT)

    def nickname_save_btn(self):
        nickname_save_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ProfilePageSelector.NICKNAME_SAVE_BTN))
        nickname_save_btn.click()
        time.sleep(0.3)
        allure.attach("Clicked on: Change nickname", name="Save Nickname Button Action", attachment_type=allure.attachment_type.TEXT)
        
    def get_current_name(self):
        time.sleep(0.6)
        return self.driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[2]/div[1]/div/div[1]").text

    def get_success_message(self):
        time.sleep(0.6)
        return self.driver.find_element(By.XPATH, "//div[@class='go4109123758']").text

    def get_error_message(self):
        time.sleep(0.6)
        return self.driver.find_element(By.XPATH, "//div[@class='go4109123758']").text


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