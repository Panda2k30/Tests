from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Nintondo.AutoTests.Data import Data
from Nintondo.AutoTests.conftest import driver
from .Base_page import BasePage

wait = WebDriverWait

class ManePageSelector:

    # PAGES BTN

    SEND_PAGE_BTN = (By.LINK_TEXT, "Send")
    RECEIVE_PAGE_BTN = (By.LINK_TEXT, "Receive")
    WALLET_PAGE_BTN = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/a")
    SETTINGS_PAGE_BTN = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div/a[2]")
    ACCOUNT_PAGE_BTN = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[3]/a")
    NFT_PAGE_BTN = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div/a[1]")

    # INFO
    BALANCE_WALLET_MANE = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/div/div/span[1]")
    BALANCE_WALLET_SECOND = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/div/div/span[2]")
    INSCRIPRION_ALLERT = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div/a[1]")
    TRANSACTION_LIST = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[3]/div[1]/a[1]/div[1]/div[2]")
    TESTNET_BTN = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div/div[2]")

class ManePage(BasePage):
    def __init__(self, driver):
        self.driver = driver  # Сохраняем переданный драйвер

    def send_page_btn(self):
        send_page_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ManePageSelector.SEND_PAGE_BTN))
        send_page_btn.click()
        print("- Перешли на страницу: Send")

    def receive_page_btn(self):
        receive_page_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ManePageSelector.RECEIVE_PAGE_BTN))
        receive_page_btn.click()
        print("- Перешли на страницу: Receive")

    def wallet_page_btn(self):
        wallet_page_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ManePageSelector.WALLET_PAGE_BTN))
        wallet_page_btn.click()
        print("- Перешли в раздел: Wallets")

    def settings_page_btn(self):
        settings_page_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ManePageSelector.SETTINGS_PAGE_BTN))
        settings_page_btn.click()
        print("- Перешли в раздел: Settings")

    def account_page_btn(self):
        account_page_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ManePageSelector.ACCOUNT_PAGE_BTN))
        account_page_btn.click()
        print("- Перешли в раздел: Account")

    def nft_page_btn(self):
        nft_page_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ManePageSelector.NFT_PAGE_BTN))
        nft_page_btn.click()
        print("- Перешли в раздел: NFT")

    def get_balance(self):
        # Получает и возвращает текущий баланс пользователя.
        get_balance_mane = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ManePageSelector.BALANCE_WALLET_MANE))
        get_balance_sec = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ManePageSelector.BALANCE_WALLET_SECOND))

        # Преобразуем текстовые значения в float после удаления лишних символов
        balance_mane = float(get_balance_mane.text.replace(" ", "").replace("$", ""))
        balance_sec = float(get_balance_sec.text.replace(" ", "").replace("$", ""))

        # Форматируем значения для вывода
        formatted_balance_mane = f"{balance_mane:g}"  # Оставляем 4 знака после запятой
        formatted_balance_sec = f"{balance_sec:.4f}"

        # Объединяем два значения с точкой между ними
        total_balance = f"{formatted_balance_mane}{formatted_balance_sec[1:]}"  # Убираем ведущий ноль у второго значения

        # Выводим результат
        print("Текущий баланс пользователя:", total_balance)
        return total_balance  # Возвращаем итоговый баланс


    def change_network(self):

        self.driver.get(f"chrome-extension://{Data.EX_ID}/index.html#/pages/network-settings")

        print("- Перешли на страницу изменения типа сети")

        change_network = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ManePageSelector.TESTNET_BTN))
        change_network.click()
        print("- Поменяли сеть на TESTNET")

    def verify_transaction(self):
        get_transaction = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ManePageSelector.TRANSACTION_LIST))

        txid = get_transaction.text
        print("TXID:", txid)
        return txid