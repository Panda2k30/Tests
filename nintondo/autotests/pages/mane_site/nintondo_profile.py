from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from autotests.pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
import allure
import random
import time

wait = WebDriverWait

class ProfilePageSelector:
 
    IMAGE = (By.XPATH, "//div/div[1]/div[1]/div")
    IMAGE_URL = (By. XPATH, "//div/img")
    IMAGE_FIELD = (By.XPATH, "//input[@placeholder='Inscription ID']")
    
    NICKNAME = (By.XPATH, "/html/body/main/div/div[1]/div[2]/div[1]/div/div[2]")
    NICKNAME_FIELD = (By.XPATH, "//*[@id='input-form']/input")
    NICKNAME_SAVE_BTN = (By.XPATH, "//button[text()='Save']")

    WALLET_ADDRESS = (By.XPATH, "//div/div[1]/div[2]/div[1]/h3")
    BALANCE = (By.XPATH, "//div/div[1]/div[2]/div[2]/div[1]/span[2]")

    INSCRIPTIONS = (By.XPATH, "//div/div[3]/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/img")
    INSCRIPTIONS_COUNT = (By.XPATH, "")
    INSCRIPTIONS_VIEW_BTN = (By.XPATH, "/html/body/main/div/div[3]/div/div/div[2]/div[2]/div/div[1]/div[3]/a/button")
    INSCRIPTIONS_PRICE = (By.XPATH, "//div/div[1]/div[1]/div/div/span[1]")

    INSCRIPTIONS_LIST = (By.XPATH, "//button/span[text()='List']")
    INSCRIPTIONS_SEND = (By.XPATH, "//button/span[text()='Send']")
    INSCRIPTIONS_UNLIST = (By.XPATH, "//button/span[text()='Unlist']")

    INSCRIPTIONS_FIELD_PRICE = (By.XPATH, "//input[@placeholder='bel/inscription']")
    INSCRIPTIONS_LIST_BTN = (By.XPATH, "//button[text()='List']")
    INSCRIPTIONS_SIGN_BTN = (By.XPATH, "//button[text()='Sign']")

    INSCRIPTIONS_UNLIST_BTN = (By.XPATH, "//button[text()='Unlist']")
    
    INSCRIPTIONS_BUY_BTN = (By.XPATH, "//button[text()='Buy']")
    INSCRIPTIONS_CREATE_BTN = (By.XPATH, "//button[text()='Create']")
    INSCRIPTIONS_CONFIRM_BTN = (By.XPATH, "//button[text()='Confirm']")


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
        
        time.sleep(0.3)
        
        image_url = wait(self.driver, 10).until(
                 EC.element_to_be_clickable(ProfilePageSelector.IMAGE_URL))
        image_url = image_url.get_attribute("src")
        print(image_url)
        allure.attach(f"Copy Image URL: {image_url}", name="Copy Image URL", attachment_type=allure.attachment_type.TEXT)
        return image_url
                
    def image_field(self, image_id):
        # Ожидаем, пока поле станет кликабельным
        image_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ProfilePageSelector.IMAGE_FIELD))

        # Инициализация ActionChains
        actions = ActionChains(self.driver)

        # Два клика по полю (для активации поля)
        actions.click(image_field).click(image_field)

        # Выделяем весь текст и удаляем его
        actions.send_keys(Keys.CONTROL + "a")  # Выделить весь текст
        actions.send_keys(Keys.BACKSPACE)  # Удалить весь текст

        # Вводим новое значение
        actions.send_keys(image_id)

        # Выполняем все действия
        actions.perform()

        allure.attach(f"Entered image id (inscription): {image_id}", name="Image Field Action", attachment_type=allure.attachment_type.TEXT)
        
    def image_save_btn(self):
        image_save_btn = wait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.NICKNAME_SAVE_BTN))
        image_save_btn.click()
        allure.attach("Clicked on: Save", name="Save Image Button Action", attachment_type=allure.attachment_type.TEXT)


class Nickname(BasePage):

    def nickname_btn(self):
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
        time.sleep(2)
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
        # Генерация случайного числа от 1 до 5 с двумя знаками после запятой
        random_price = round(random.uniform(1, 5), 2)
    
        inscription_field_price = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ProfilePageSelector.INSCRIPTIONS_FIELD_PRICE)
        )
        inscription_field_price.send_keys(str(random_price))
        allure.attach(f"Entered the cost in the field: {random_price}", name="Price Field Action", attachment_type=allure.attachment_type.TEXT)

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
    attempts = 0
    while attempts < 3:
        try:
            sign_btn = wait.until(
                EC.element_to_be_clickable((By.ID, "sign_button"))
            )
            sign_btn.click()

            error_message = 'Insufficient balance. Non-Inscription balance (0 BEL) is lower than 0.0000522 BEL'
            expected_message = 'Balance not enough to pay network fee.'
            assert expected_message in error_message, (
                f"Expected error message '{expected_message}', but got '{error_message}'"
            )

            allure.attach(
                error_message,
                name="Error Message Details",
                attachment_type=allure.attachment_type.TEXT
            )
            break
        except StaleElementReferenceException:
            attempts += 1
            print(f"Attempt {attempts}: Retrying to locate the element")
    
    allure.attach("In the second window clicked: Sign", name="Sign Button Action", attachment_type=allure.attachment_type.TEXT)
        
    def inscription_view_btn(self):
        
        # Wait until the page is fully loaded
        wait(self.driver, 30).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
        
        try:
            # Re-locate the element after window switch
            inscription_view_btn = wait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.INSCRIPTIONS_VIEW_BTN)
            )
        except StaleElementReferenceException:
            # If element becomes stale, find it again
            inscription_view_btn = wait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.INSCRIPTIONS_VIEW_BTN)
            )
        
        # Scroll the element into view before clicking
        self.driver.execute_script("arguments[0].scrollIntoView(true);", inscription_view_btn)
        
        # Click the button
        inscription_view_btn.click()
        allure.attach("Go to: inspect inscription", name="View inscription", attachment_type=allure.attachment_type.TEXT)

        
    def inscription_buy_btn(self):
        
        self.driver.set_window_size(1280, 1080)
        time.sleep(0.3)
        
        inscription_price = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ProfilePageSelector.INSCRIPTIONS_PRICE))
        inscription_price_text = inscription_price.text
        
        inscription_buy = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ProfilePageSelector.INSCRIPTIONS_BUY_BTN))
        inscription_buy.click()
        
        allure.attach(f"Price {inscription_price_text}, Clicked on: Buy", name="Buy Button Action and Price", attachment_type=allure.attachment_type.TEXT)
        
    def inscription_confirm_btn(self):
        
        try:
        # Пытаемся найти и кликнуть на INSCRIPTIONS_CONFIRM_BTN
            inscription_confirm_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.INSCRIPTIONS_CONFIRM_BTN))
            inscription_confirm_btn.click()
        except:
            # Если не удалось, ищем и кликаем на INSCRIPTIONS_CONTINUE_BTN
            inscription_continue_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(ProfilePageSelector.INSCRIPTIONS_CREATE_BTN))
            inscription_continue_btn.click()
        
        allure.attach("Clicked on: Create/Continue", name="Button Action", attachment_type=allure.attachment_type.TEXT)     