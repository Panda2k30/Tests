from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from autotests.conftest import driver
from autotests.pages.base_page import BasePage
import time
import allure

wait = WebDriverWait

class ManePageSelector:

    # PAGES BTN
    SEND_PAGE_BTN = (By.LINK_TEXT, "Send")
    RECEIVE_PAGE_BTN = (By.LINK_TEXT, "Receive")
    WALLET_PAGE_BTN = (By.XPATH, "//a[@href='#/pages/switch-wallet']")
    SETTINGS_PAGE_BTN = (By.XPATH, "//a[@href='#/pages/settings']")
    ACCOUNT_PAGE_BTN = (By.XPATH, "//a[@href='#/pages/switch-account']")
    NFT_PAGE_BTN = (By.XPATH, "//a/img")
    BACK_BTN = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div[1]")

    # INFO
    BALANCE_WALLET_MANE = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/div/div/span[1]")
    BALANCE_WALLET_SECOND = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/div/div/span[2]")
    INSCRIPTION_ALLERT = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div/a[1]")
    TRANSACTION_LIST = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[3]/div[1]/a[1]/div[1]/div[2]")
    TESTNET_BTN = (By.XPATH, "//div[text()='TESTNET']")
    TRANSACTION_CONT = (By.XPATH, "//*[contains(@class, 'transactionsDiv')]")
    ACCOUNT_ADDRESS = (By.CSS_SELECTOR, "._walletDiv_1nrdb_1 ._accPanel_1nrdb_4 ._accPubAddress_1nrdb_13")

    # Wallets
    ADD_WALLET_BTN = (By.XPATH, "//a[@href='#/pages/create-new-wallet']")
    PRIVATE_KEY_BTN = (By.LINK_TEXT, "Restore from private key")


import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time

class ManePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def send_page_btn(self):
        send_page_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ManePageSelector.SEND_PAGE_BTN))
        send_page_btn.click()
        message = "- Go to the page: Send"
        allure.attach(message, name="Action", attachment_type=allure.attachment_type.TEXT)

    def receive_page_btn(self):
        receive_page_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ManePageSelector.RECEIVE_PAGE_BTN))
        receive_page_btn.click()
        message = "- Go to the page: Receive"
        allure.attach(message, name="Action", attachment_type=allure.attachment_type.TEXT)

    def wallet_page_btn(self):
        wallet_page_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ManePageSelector.WALLET_PAGE_BTN))
        wallet_page_btn.click()
        message = "- Go to: Wallets"
        allure.attach(message, name="Action", attachment_type=allure.attachment_type.TEXT)

    def settings_page_btn(self):
        settings_page_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ManePageSelector.SETTINGS_PAGE_BTN))
        settings_page_btn.click()
        message = "- Go to: Settings"
        allure.attach(message, name="Action", attachment_type=allure.attachment_type.TEXT)

    def account_page_btn(self):
        account_page_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ManePageSelector.ACCOUNT_PAGE_BTN))
        account_page_btn.click()
        message = "- Go to: Accounts"
        allure.attach(message, name="Action", attachment_type=allure.attachment_type.TEXT)

    def nft_page_btn(self):
        nft_page_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ManePageSelector.NFT_PAGE_BTN))
        nft_page_btn.click()
        message = "- Go to: NFT"
        allure.attach(message, name="Action", attachment_type=allure.attachment_type.TEXT)

    def add_wallet_btn(self):
        add_wallet_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ManePageSelector.ADD_WALLET_BTN))
        add_wallet_btn.click()
        message = "- Clicked: Add Wallet"
        allure.attach(message, name="Action", attachment_type=allure.attachment_type.TEXT)

    def get_balance(self):
        time.sleep(0.4)
        get_balance_mane = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ManePageSelector.BALANCE_WALLET_MANE))
        get_balance_sec = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ManePageSelector.BALANCE_WALLET_SECOND))

        balance_mane = float(get_balance_mane.text.replace(" ", "").replace("$", ""))
        balance_sec = float(get_balance_sec.text.replace(" ", "").replace("$", ""))
        formatted_balance_mane = f"{balance_mane:g}"
        formatted_balance_sec = f"{balance_sec:.4f}"
        total_balance = f"{formatted_balance_mane}{formatted_balance_sec[1:]}"
        
        message = f"The user's current balance: {total_balance}"
        allure.attach(message, name="Balance", attachment_type=allure.attachment_type.TEXT)
        return total_balance

    def change_network(self, ex_id):
        wait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[text()='No transactions']")))

        self.driver.get(f"chrome-extension://{ex_id}/index.html#/pages/network-settings")
        allure.attach("- Go to the page for changing the network type", name="Navigation", attachment_type=allure.attachment_type.TEXT)

        change_network = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ManePageSelector.TESTNET_BTN))
        change_network.click()
        allure.attach("- Changed the network to TESTNET", name="Action", attachment_type=allure.attachment_type.TEXT)

    def verify_transaction(self):
        get_transaction = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ManePageSelector.TRANSACTION_LIST))
        txid = get_transaction.text
        allure.attach(f"Last TXID: {txid}", name="Transaction", attachment_type=allure.attachment_type.TEXT)
        return txid

    def back_btn(self):
        back_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ManePageSelector.BACK_BTN))
        back_btn.click()
        allure.attach("- You clicked on the “Back” button.", name="Action", attachment_type=allure.attachment_type.TEXT)

    def account_address_btn(self):
        button = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ManePageSelector.ACCOUNT_ADDRESS))
        account_address = self.driver.execute_script(
            "return arguments[0].getAttribute('title');", button)
        allure.attach(f"The address of the account is on the home page: {account_address}", name="Account Address", attachment_type=allure.attachment_type.TEXT)
        return account_address

    def trans_cont(self):
        wait(self.driver, 10).until(
            EC.element_to_be_clickable(ManePageSelector.TRANSACTION_CONT))
        allure.attach("- Wait for the transaction list to load", name="Transaction List", attachment_type=allure.attachment_type.TEXT)
