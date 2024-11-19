from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from autotests.conftest import driver
from autotests.pages.base_page import BasePage
import allure

wait = WebDriverWait

class ReceivePageSelector:

    WALLET_ADDRESS_TEXT = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div/div/div[2]")
    WALLET_ADDRESS_COPY_BTN = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div/button/div")
    WALLET_ADDRESS_QR = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div/div/div[1]")


class ReceivePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def receive_address_text(self):
        receive_address_text = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ReceivePageSelector.WALLET_ADDRESS_TEXT))
        receive_address_text.click()
        allure.attach("- Taking the address from the line", name="Action", attachment_type=allure.attachment_type.TEXT)
        text_address = receive_address_text.text
        allure.attach(f"The address from the string: {text_address}", name="Address", attachment_type=allure.attachment_type.TEXT)
        return text_address

    def receive_address_btn(self):
        receive_address_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ReceivePageSelector.WALLET_ADDRESS_COPY_BTN)
        )
        receive_address_btn.click()
        allure.attach("- Clicked on: Copy Address", name="Action", attachment_type=allure.attachment_type.TEXT)

        address_selector = ".text-xs"

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, address_selector))
        )

        self.driver.execute_script(f"""
            var addressElement = document.querySelector('{address_selector}');
            if (addressElement) {{
                var tempInput = document.createElement('input');
                tempInput.value = addressElement.textContent; 
                document.body.appendChild(tempInput);
                tempInput.select();  
                document.execCommand('copy');  
                document.body.removeChild(tempInput);  
            }} else {{
                console.error('Address element not found!');
            }}
        """)

        btn_address = self.driver.execute_script(
            f"return document.querySelector('{address_selector}') ? document.querySelector('{address_selector}').textContent : '';"
        ).strip()

        if not btn_address:
            allure.attach("Адрес не найден!", name="Error", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.driver.page_source, name="Page Source", attachment_type=allure.attachment_type.HTML)
        else:
            allure.attach(f"Address from the button: {btn_address}", name="Button Address", attachment_type=allure.attachment_type.TEXT)

        return btn_address

    def receive_address_qr(self):
        receive_address_qr = wait(self.driver, 10).until(
            EC.element_to_be_clickable(ReceivePageSelector.WALLET_ADDRESS_QR))
        receive_address_qr.click()
        allure.attach("- Clicked on: QR copy image", name="Action", attachment_type=allure.attachment_type.TEXT)