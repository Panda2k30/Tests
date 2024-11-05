from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, by, locator):
        for _ in range(3):  # Попробуем 3 раза
            try:
                element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, locator)))
                element.click()
                return
            except StaleElementReferenceException:
                continue
        raise Exception(f"Не удалось кликнуть на элемент {locator} после нескольких попыток.")

    def input_text(self, by, locator, text):
        for _ in range(3):  # Попробуем 3 раза
            try:
                element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, locator)))
                element.clear()  # Очистить поле перед вводом
                element.send_keys(text)
                return
            except StaleElementReferenceException:
                continue
        raise Exception(f"Не удалось ввести текст в элемент {locator} после нескольких попыток.")