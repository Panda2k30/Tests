import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait

class SendPageSelector:

    # INPUTS
    ADDRESS_INPUT = (By.XPATH, '//*[@id="headlessui-combobox-input-:r3:"]')
    AMOUNT_INPUT = (By.XPATH, '//*[@id=":r0:"]/div[1]/div[2]/div/div/input"]')

    # BUTTONS

    FEE_SLOW_BTN = (By.XPATH, '//*[@id=":r0:"]/div[2]/div[1]/div/div/div[1]')
    FEE_FAST_BTN = (By.XPATH, '//*[@id=":r0:"]/div[2]/div[1]/div/div/div[2]')
    FEE_CUSTOM_BTN = (By.XPATH, '//*[@id=":r0:"]/div[2]/div[1]/div/div/div[3]')

    INCLUDE_FEE = (By.XPATH, '//*[@id="headlessui-control-:r4:"]')
    SAVE_ADDRESS = (By.XPATH, '//*[@id="headlessui-control-:r7:"]')

class SendPage:
    def __init__(self, driver):
        self.driver = driver  # Сохраняем переданный драйвер

    def enter_address(self, valid_address):  # Принимаем пароль как аргумент
        enter_address = wait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageSelectors.ADDRESS_INPUT))
        enter_address.send_keys(valid_address)  # Используем переданный аргумент
        print("- Ввели валидный адрес")