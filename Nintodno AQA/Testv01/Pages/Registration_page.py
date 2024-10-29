import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait

class LoginPage:
    PASSWORD_FIELD = (By.XPATH, '//input[@id="password"]')
    CONF_PASSWORD_FIELD = (By.XPATH, '//input[@id="confirmPassword"]')
    REG_BUTTON = (By.XPATH, "//button[text()='Create password']")

    # Создание новой мнемоники
    NEW_MNEMONIC = (By.LINK_TEXT, "New mnemonic")
    COPY_MNEMONIC = (By.XPATH, "//div[@id='root']//button")
    CONF_MNEMONIC = (By.ID, "headlessui-control-:r0:")
    CREATE_BUTTON = (By.XPATH, "//button[text()='Continue']")

    LEGACY_TYPE = (By.XPATH, "//div[@id='root']//div[2]//div[2]//div[1]//div[2]")

class CreateMnemonic:
    def __init__(self, driver):
        self.driver = driver  # Сохраняем переданный драйвер

    def enter_password(self, password):  # Принимаем пароль как аргумент
        password_field = wait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPage.PASSWORD_FIELD))
        password_field.send_keys(password)  # Используем переданный аргумент
        print("- Ввели пароль")

    def conf_password(self, confpassword):  # Принимаем подтверждение пароля как аргумент
        confpassword_field = wait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPage.CONF_PASSWORD_FIELD))
        confpassword_field.send_keys(confpassword)  # Используем переданный аргумент
        print("- Подтвердили пароль")

    def click_reg_button(self):
        reg_button = wait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPage.REG_BUTTON))
        reg_button.click()
        print("- Нажали на кнопку регистрации")

    def type_reg(self):
        type_reg = wait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPage.NEW_MNEMONIC))
        type_reg.click()
        print("- Нажали на New mnemonic")

    def copy_mnem(self):
        copy_mnem = wait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPage.COPY_MNEMONIC))
        copy_mnem.click()
        print("- Скопироали фразы в буфер обмена")

    def paste_mnen(self):
        clipboard_text = pyperclip.paste()
        print("Ваши фразы:", clipboard_text)

    def conf_save(self):
        # Подтверждаем сохранение мнемоники
        conf_save = wait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPage.CONF_MNEMONIC))
        print("- Подтверждаем сохранение фраз")
        conf_save.click()

    def conf_create_wallet(self):
        # Подтверждаем создание кошелька
        createbtn_mnemonic = wait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPage.CREATE_BUTTON))
        print("- Подтверждаем создрание кошелька")
        createbtn_mnemonic.click()

    def choose_type_wallet(self):
        # Выбираем: Legacy Type"
        legacy_type = wait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPage.LEGACY_TYPE))
        print("- Выбираем: Legacy Type")
        legacy_type.click()

    def conf_create_wallet(self):
        # Подтверждаем создание кошелька
        createbtn_mnemonic = wait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPage.CREATE_BUTTON))
        print("- Подтверждаем создрание кошелька")
        createbtn_mnemonic.click()

