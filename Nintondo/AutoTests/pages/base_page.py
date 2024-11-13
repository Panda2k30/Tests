from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, by, locator):
        for _ in range(3): 
            try:
                element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, locator)))
                element.click()
                return
            except StaleElementReferenceException:
                continue
        raise Exception(f"Failed to click on an item {locator} after several attempts.")

    def input_text(self, by, locator, text):
        for _ in range(3): 
            try:
                element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, locator)))
                element.clear()
                element.send_keys(text)
                return
            except StaleElementReferenceException:
                continue
        raise Exception(f"Failed to enter text into the {locator} element after several attempts.")
