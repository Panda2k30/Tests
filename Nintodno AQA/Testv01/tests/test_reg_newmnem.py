import pytest
from Testv01.Pages.Registration_page import CreateMnemonic
from Testv01.Data import Data
import allure

@allure.feature("Craate wallet with new Mnemonic")
@pytest.mark.usefixtures("driver")
def test_create_mnemonic(driver):
    """Тестирование создания кошелька при помощи нового мнемоника"""
    test_create_mnemonic = CreateMnemonic(driver)

    test_create_mnemonic.enter_password(Data.PASS) # Ввод пароля
    test_create_mnemonic.conf_password(Data.CONFPASS) # Подтверждение пароля
    test_create_mnemonic.click_reg_button() # Жмем на кнопку продолжения
    test_create_mnemonic.type_reg() # Выбираем тип авторизации - Новая мнемоника
    test_create_mnemonic.copy_mnem() # Копируем фразы
    test_create_mnemonic.paste_mnen() # Выводим фразы
    test_create_mnemonic.conf_save() # Подтверждаем сохранение мнемоники
    test_create_mnemonic.conf_create_wallet() # Подтверждаем создание кошелька
    test_create_mnemonic.choose_type_wallet() # Выбираем: Legacy Type"
    test_create_mnemonic.conf_create_wallet() # Подтверждаем создание кошелька

@allure.feature("Restore wallet by private key")
def test_restore_by_private_key(driver):
    """Тестирование восстановления кошелька при помощи нового мнемоника"""
    test_restore_by_private_key = CreateMnemonic(driver)

    test_restore_by_private_key.enter_password(Data.PASS) # Ввод пароля
    test_restore_by_private_key.conf_password(Data.CONFPASS) # Подтверждение пароля
    test_restore_by_private_key.click_reg_button() # Жмем на кнопку продолжения