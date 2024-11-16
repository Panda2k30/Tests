from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AutoTests.data import Data
from AutoTests.conftest import driver
from AutoTests.pages.base_page import BasePage
import requests
import time

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
        print("- Opened the inscription")

    def send_btn(self):
        send_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.INSCRIPTION_SEND_BTN))
        send_btn.click()
        print("- Clicked on: Send")

    def enter_address(self, valid_address):
        enter_address = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.INSCRIPTION_ADDRESS_INPUT))
        enter_address.send_keys(valid_address)
        
        print("- Entered a valid address:", valid_address)
        
        return valid_address

    def continue_btn(self):
        continue_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.INSCRIPTION_CONT_BTN))
        continue_btn.click()
        print("- Clicked on: Continue")

    def confirm_btn(self):
        confirm_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.INSCRIPTION_CONF_BTN))
        confirm_btn.click()
        print("- Clicked on: Confirm")

    def return_id_card(self):
        id_card = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.INSCRIPTION_ID_CARD))

        id_card = id_card.text
        
        print("- ID in the description:", id_card)
        
        return id_card

    def return_id_tabl(self):
        id_tabl = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.INSCRIPTION_ID_CONF))

        id_tabl = id_tabl.text
        print("- Table ID:", id_tabl)
        
        return id_tabl

    def return_from_address_tabl(self):
        from_address_tabl = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.INSCRIPTION_FROM_ADDRESS_CONF))

        from_address_tabl = from_address_tabl.text
        print("- The address of the sender in the table:", from_address_tabl)
        
        return from_address_tabl

    def return_to_address_tabl(self):
        to_address_tabl = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.INSCRIPTION_TO_ADDRESS_CONF))

        to_address_tabl = to_address_tabl.text
        print("- The recipient's address in the table:", to_address_tabl)
        
        return to_address_tabl

    def back_btn(self):
        time.sleep(0.5)
        back_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.INSCRIPTION_BACK_BTN))
        back_btn.click()
        print("- Clicked on: Back")
        

class TransfersPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
    
    def bel_btn(self):
        bel_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.BEL))
        bel_btn.click()
        print("- Opened BEL-20")

    def select_transfer(self):
        select_transfer = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.SELECT_TRANSFER))
        select_transfer.click()
        print("- Selected an transfer")

    def mint_btn(self):
        mint_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.MINT_BTN))
        mint_btn.click()
        print("- Clicked: Mint transfer")
        
    def amount(self, count):
        amount = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.AMOUNT_BTN))
        amount.send_keys(count)
        print("- Enter:", count)
        
    def inscribe_btn(self):
        inscribe_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.INSCRIBE_BTN))
        inscribe_btn.click()
        print("- Clicked: Inscribe")
    
    def check_transfer_balance(self):
        
        url = "https://testnet.nintondo.io/electrs/address/EMpxzi7FujHsQHbrZy7wsuiRHFsvxKZSaB/tokens"

        response = requests.get(url)

        data = response.json()

        for item in data:
            if item['tick'] == 'ondo':  # Check if the tick is 'ondo'
                print(item['transferable_balance'])
                
    def check_balance(self):
        
        url = "https://testnet.nintondo.io/electrs/address/EMpxzi7FujHsQHbrZy7wsuiRHFsvxKZSaB/tokens"

        response = requests.get(url)

        data = response.json()

        for item in data:
            if item['tick'] == 'ondo':  # Check if the tick is 'ondo'
                print(item['balance'])
            
    def send_btn(self):
        send_btn = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.SEND_BTN))
        send_btn.click()
        print("- Clicked: Send")

    def address_input(self, address):
        address_input = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.ADDRESS_INPUT))
        address_input.send_keys(address)
        print("- Enter:", address)
        
    def select_amount(self):
        select_amount = wait(self.driver, 10).until(
            EC.element_to_be_clickable(NFTPageSelector.SELECT_AMOUNT))
        select_amount.click()
        print("- Select Transfer amount")

