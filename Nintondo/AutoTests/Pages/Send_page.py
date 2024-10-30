import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait

class SendPageSelector:

    # INPUTS
    ADDRESS_INPUT = ()
    AMOUNT_INPUT = ()

    # BUTTONS

    FEE_SLOW_BTN = ()
    FEE_FAST_BTN = ()
    FEE_CUSTOM_BTN = ()

class SendPage:
    def __init__(self, driver):
        self.driver = driver  # Сохраняем переданный драйвер

