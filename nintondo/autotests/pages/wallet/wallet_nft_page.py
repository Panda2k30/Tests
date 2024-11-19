from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from autotests.data import Data
from autotests.conftest import driver
from autotests.pages.base_page import BasePage
import requests
import time
import allure

wait = WebDriverWait

class NFTPageSelector:

    # Inscription page

    INSCRIPTION = (By.XPATH, "//div/img")
    INSCRIPTION_SEND_BTN = (By.XPATH, "//button[text()='Send']")
    INSCRIPTION_ADDRESS_INPUT = (By.XPATH, "//div/input")
    INSCRIPTION_CONT_BTN = (By.XPATH, "//button[text()='Continue']")
    INSCRIPTION_CONF_BTN = (By.XPATH, "//button[text()='Confirm']")
    INSCRIPTION_BACK_BTN = (By.XPATH, "//a[text()='Back']")

    INSCRIPTION_ID_CARD = (By.XPATH, "//label[text()='Inscription id']/following-sibling::div")
    INSCRIPTION_ID_CONF = (By.XPATH, "//div[text()='Inscription Id']/following-sibling::div")
    INSCRIPTION_TO_ADDRESS_CONF = (By.XPATH, "//div[text()='To address']/following-sibling::div")
    INSCRIPTION_FROM_ADDRESS_CONF = (By.XPATH, "//div[text()='From address']/following-sibling::div")
    
    # Bel20 page
    
    BEL = (By.XPATH, "//div[span='Inscriptions']")
    SELECT_TRANSFER = (By.XPATH, "//div[span='ONDO']")
    
    SEND_BTN = (By.XPATH, "//button[text()='Send']")
    MINT_BTN = (By.XPATH, "//button[text()='Mint transfer']")
    
    AMOUNT_BTN = (By.XPATH, "//input[@placeholder='Amount to mint']")
    INSCRIBE_BTN = (By.XPATH, "//button[text()='Inscribe']")
    
    ADDRESS_INPUT = (By.XPATH, "//input")
    SELECT_AMOUNT = (By.XPATH, "//*[contains(@class, '_transfer_')]")
    
        
class SendInscription(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def select_inscription(self):
        select_inscription = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.INSCRIPTION))
        select_inscription.click()
        allure.attach("- Opened the inscription", name="Action", attachment_type=allure.attachment_type.TEXT)

    def send_btn(self):
        send_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.INSCRIPTION_SEND_BTN))
        send_btn.click()
        allure.attach("- Clicked on: Send", name="Action", attachment_type=allure.attachment_type.TEXT)

    def enter_address(self, valid_address):
        enter_address = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.INSCRIPTION_ADDRESS_INPUT))
        enter_address.send_keys(valid_address)
        allure.attach(f"- Entered a valid address: {valid_address}", name="Address Input", attachment_type=allure.attachment_type.TEXT)
        return valid_address

    def continue_btn(self):
        continue_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.INSCRIPTION_CONT_BTN))
        continue_btn.click()
        allure.attach("- Clicked on: Continue", name="Action", attachment_type=allure.attachment_type.TEXT)

    def confirm_btn(self):
        confirm_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.INSCRIPTION_CONF_BTN))
        confirm_btn.click()
        allure.attach("- Clicked on: Confirm", name="Action", attachment_type=allure.attachment_type.TEXT)

    def return_id_card(self):
        id_card = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.INSCRIPTION_ID_CARD)).text
        allure.attach(f"- ID in the description: {id_card}", name="ID Card", attachment_type=allure.attachment_type.TEXT)
        return id_card

    def return_id_tabl(self):
        id_tabl = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.INSCRIPTION_ID_CONF)).text
        allure.attach(f"- Table ID: {id_tabl}", name="Table ID", attachment_type=allure.attachment_type.TEXT)
        return id_tabl

    def return_from_address_tabl(self):
        from_address_tabl = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.INSCRIPTION_FROM_ADDRESS_CONF)).text
        allure.attach(f"- The address of the sender in the table: {from_address_tabl}", name="From Address", attachment_type=allure.attachment_type.TEXT)
        return from_address_tabl

    def return_to_address_tabl(self):
        to_address_tabl = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.INSCRIPTION_TO_ADDRESS_CONF)).text
        allure.attach(f"- The recipient's address in the table: {to_address_tabl}", name="To Address", attachment_type=allure.attachment_type.TEXT)
        return to_address_tabl

    def back_btn(self):
        time.sleep(0.5)
        back_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.INSCRIPTION_BACK_BTN))
        back_btn.click()
        allure.attach("- Clicked on: Back", name="Action", attachment_type=allure.attachment_type.TEXT)


class TransfersPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def bel_btn(self):
        bel_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.BEL))
        bel_btn.click()
        allure.attach("- Opened BEL-20", name="Action", attachment_type=allure.attachment_type.TEXT)

    def select_transfer(self):
        select_transfer = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.SELECT_TRANSFER))
        select_transfer.click()
        allure.attach("- Selected a transfer", name="Action", attachment_type=allure.attachment_type.TEXT)

    def mint_btn(self):
        mint_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.MINT_BTN))
        mint_btn.click()
        allure.attach("- Clicked: Mint transfer", name="Action", attachment_type=allure.attachment_type.TEXT)

    def amount(self, count):
        amount = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.AMOUNT_BTN))
        amount.send_keys(count)
        allure.attach(f"- Entered amount: {count}", name="Amount", attachment_type=allure.attachment_type.TEXT)

    def inscribe_btn(self):
        inscribe_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.INSCRIBE_BTN))
        inscribe_btn.click()
        allure.attach("- Clicked: Inscribe", name="Action", attachment_type=allure.attachment_type.TEXT)

    def check_transfer_balance(self):
        url = "https://testnet.nintondo.io/electrs/address/EMpxzi7FujHsQHbrZy7wsuiRHFsvxKZSaB/tokens"
        response = requests.get(url)
        data = response.json()
        for item in data:
            if item['tick'] == 'ondo':
                balance = item['transferable_balance']
                allure.attach(f"Transferable Balance: {balance}", name="Transfer Balance", attachment_type=allure.attachment_type.TEXT)

    def check_balance(self):
        url = "https://testnet.nintondo.io/electrs/address/EMpxzi7FujHsQHbrZy7wsuiRHFsvxKZSaB/tokens"
        response = requests.get(url)
        data = response.json()
        for item in data:
            if item['tick'] == 'ondo':
                balance = item['balance']
                allure.attach(f"Balance: {balance}", name="Balance", attachment_type=allure.attachment_type.TEXT)

    def send_btn(self):
        send_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.SEND_BTN))
        send_btn.click()
        allure.attach("- Clicked: Send", name="Action", attachment_type=allure.attachment_type.TEXT)

    def address_input(self, address):
        address_input = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.ADDRESS_INPUT))
        address_input.send_keys(address)
        allure.attach(f"- Entered address: {address}", name="Address Input", attachment_type=allure.attachment_type.TEXT)

    def select_amount(self):
        select_amount = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.SELECT_AMOUNT))
        select_amount.click()
        allure.attach("- Selected transfer amount", name="Action", attachment_type=allure.attachment_type.TEXT)

