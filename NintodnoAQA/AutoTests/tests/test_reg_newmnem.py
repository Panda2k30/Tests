# import time
import allure
import pytest
from Pages.Registration_page import CreateMnemonic
from .Data import Data

@allure.feature("Create wallet with new Mnemonic")
@pytest.mark.usefixtures("driver")
def test_create_mnemonic(driver):
    test_create_mnemonic = CreateMnemonic(driver)

    test_create_mnemonic.enter_password(Data.PASS) # Ввод пароля
    test_create_mnemonic.conf_password(Data.CONFPASS) # Подтверждение пароля
    test_create_mnemonic.click_reg_button() # Жмем на кнопку продолжения
    test_create_mnemonic.type_reg_new_mnem() # Выбираем тип авторизации - Новая мнемоника
    test_create_mnemonic.copy_mnem() # Копируем фразы
    test_create_mnemonic.paste_mnen() # Выводим фразы
    test_create_mnemonic.conf_save() # Подтверждаем сохранение мнемоники
    test_create_mnemonic.conf_create_wallet() # Подтверждаем создание кошелька
    test_create_mnemonic.choose_type_legacy() # Выбираем: Legacy Type"
    test_create_mnemonic.conf_create_wallet() # Подтверждаем создание кошелька

@allure.feature("Restore wallet by private key")
def test_restore_by_private_key(driver):
    test_restore_by_private_key = CreateMnemonic(driver)
    test_restore_by_private_key.enter_password(Data.PASS) # Ввод пароля
    test_restore_by_private_key.conf_password(Data.CONFPASS) # Подтверждение пароля
    test_restore_by_private_key.click_reg_button() # Жмем на кнопку продолжения
    test_restore_by_private_key.type_reg_privacy_key() # Выбираем восстановление через приватник
    test_restore_by_private_key.restore_input(Data.PRIV_KEY) # Вводим приватник
    test_restore_by_private_key.conf_recover_wallet()  # Подтверждаем создание кошелька

    # test_restore_by_private_key.choose_type_legacy() # Выбираем: Legacy Type"
    # test_restore_by_private_key.conf_create_wallet() # Подтверждаем создание кошелька

@allure.feature("Restore wallet by mnemonic")
def test_restore_by_mnemonic(driver):
    test_restore_by_mnemonic = CreateMnemonic(driver)

    test_restore_by_mnemonic.enter_password(Data.PASS)  # Ввод пароля
    test_restore_by_mnemonic.conf_password(Data.CONFPASS)  # Подтверждение пароля
    test_restore_by_mnemonic.click_reg_button()  # Жмем на кнопку продолжения
    test_restore_by_mnemonic.type_reg_mnemonic()  # Выбираем восстановление через мнемонику
    test_restore_by_mnemonic.type_reg_restore_mnem(Data.MNEMONIC_DATA)  # Вставляем мнемоники
    test_restore_by_mnemonic.click_restore_button()  # Жмем на кнопку продолжения
    test_restore_by_mnemonic.choose_type_native()   # Выбираем: Native Segwit
    test_restore_by_mnemonic.conf_create_wallet()  # Подтверждаем создание кошелька