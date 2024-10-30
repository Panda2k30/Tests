import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

wait = WebDriverWait

class LoginPageSelectors:
    PASSWORD_FIELD = (By.XPATH, '//input[@id="password"]')
    CONF_PASSWORD_FIELD = (By.XPATH, '//input[@id="confirmPassword"]')
    REG_BUTTON = (By.XPATH, "//button[text()='Create password']")

    # Типы восстановления кошелька
    NEW_MNEMONIC = (By.LINK_TEXT, "New mnemonic")
    RESTORE_MNEMONIC = (By.LINK_TEXT, "Restore mnemonic")
    PRIVAT_KEY = (By.LINK_TEXT, "Restore from private key")

    COPY_MNEMONIC = (By.XPATH, "//div[@id='root']//button")
    CONF_MNEMONIC = (By.ID, "headlessui-control-:r0:")
    CREATE_BUTTON = (By.XPATH, "//button[text()='Continue']")
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Recover']")

    RESTORE_INPUT = (By.XPATH, "//input[@id='privKey']")
    RESTORE_MNEMONIC_INPUT = (By.XPATH, "//input[@class='_input_u2hpt_1']")
    RESTORE_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/button")

    LEGACY_TYPE = (By.XPATH, "//div[@id='root']//div[2]//div[2]//div[1]//div[2]")
    NATIVE_SEGWIT = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]")


class CreateMnemonic:
    def __init__(self, driver):
        self.driver = driver  # Сохраняем переданный драйвер

    def enter_password(self, password):  # Принимаем пароль как аргумент
        password_field = wait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageSelectors.PASSWORD_FIELD))
        password_field.send_keys(password)  # Используем переданный аргумент
        print("- Ввели валидный пароль")

    def conf_password(self, confpassword):  # Принимаем подтверждение пароля как аргумент
        confpassword_field = wait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageSelectors.CONF_PASSWORD_FIELD))
        confpassword_field.send_keys(confpassword)  # Используем переданный аргумент
        print("- Подтвердили пароль")

    def click_reg_button(self):
        reg_button = wait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageSelectors.REG_BUTTON))
        reg_button.click()
        print("- Кликнули на кнопку: Create password")

    def type_reg_new_mnem(self):
        type_reg = wait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageSelectors.NEW_MNEMONIC))
        type_reg.click()
        print("- Кликнули на: New mnemonic")

    def type_reg_privacy_key(self):
        type_reg_privacy_key = wait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageSelectors.PRIVAT_KEY))
        type_reg_privacy_key.click()
        print("- Кликнули восстановление через приватник")

    def type_reg_mnemonic(self):
        type_reg_mnemonic = wait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageSelectors.RESTORE_MNEMONIC))
        type_reg_mnemonic.click()
        print("- Кликнули восстановление через мнемонику")

    def type_reg_restore_mnem(self, mnemonic):
        input_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageSelectors.RESTORE_MNEMONIC_INPUT)
        )

        for word in mnemonic:
            input_field.send_keys(word)  # Вводим слово
            input_field.send_keys(Keys.TAB)  # Переходим к следующему полю
            input_field = self.driver.switch_to.active_element  # Обновляем ссылку на текущее поле
        print("- Ввели seed-фразы в поля")

    def copy_mnem(self):
        copy_mnem = wait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageSelectors.COPY_MNEMONIC))
        copy_mnem.click()
        print("- Скопировали фразы в буфер обмена")

    def paste_mnen(self):
        clipboard_text = pyperclip.paste()
        print("Ваши фразы:", clipboard_text)

    def conf_save(self):
        # Подтверждаем сохранение мнемоники
        conf_save = wait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageSelectors.CONF_MNEMONIC))
        conf_save.click()
        print("- Подтвердили сохранение фраз")

    def conf_create_wallet(self):
        # Подтверждаем создание кошелька
        createbtn_mnemonic = wait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageSelectors.CREATE_BUTTON))
        createbtn_mnemonic.click()
        print("- Кликнули на: Continue")

    def choose_type_legacy(self):
        # Выбираем: Legacy Type"
        legacy_type = wait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageSelectors.LEGACY_TYPE))
        legacy_type.click()
        print("- Выбрали: Legacy Type")

    def choose_type_native(self):
        # Выбираем: Native Segwit"
        choose_type_native = wait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageSelectors.NATIVE_SEGWIT))
        choose_type_native.click()
        print("- Выбрали: Native Segwit")

    def conf_create_wallet(self):
        # Подтверждаем создание кошелька
        createbtn_mnemonic = wait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageSelectors.CREATE_BUTTON))
        createbtn_mnemonic.click()
        print("- Подтвердлили создание кошелька")

    def conf_recover_wallet(self):
        # Подтверждаем создание кошелька
        conf_recover_wallet = wait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageSelectors.RECOVER_BUTTON))
        conf_recover_wallet.click()
        print("- Кликнули на: Recover")

    def restore_input(self, privat_key):
        # Подтверждаем создание кошелька
        restore_input = wait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageSelectors.RESTORE_INPUT))
        restore_input.send_keys(privat_key)  # Используем переданный аргумент
        print("- Ввели приватный ключ")

    def click_restore_button(self):
        # Подтверждаем восстановление кошелька по мнемоникам
        click_restore_button = wait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageSelectors.RESTORE_BUTTON))
        click_restore_button.click()
        print("- Кликнули на кнопку: Continue")