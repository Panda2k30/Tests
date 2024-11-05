import time
import allure
import pytest
from Nintondo.AutoTests.conftest import driver
from Nintondo.AutoTests.Tests.Nintondo.test_connect import test_connect
from Nintondo.AutoTests.Pages.Nintondo.nintondo_mane import NintondoUserMenu
from Nintondo.AutoTests.Pages.Nintondo.nintondo_profile import ProfilePage, Inscriptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver")
@allure.feature("Test valid inscription list")
# Тестируем публикацию инскрипций на продажу
def test_inscription_list(driver):
    test_connect(driver)

    menu = NintondoUserMenu(driver)
    profile = ProfilePage(driver)
    inscription = Inscriptions(driver)

    menu.open_menu()
    menu.menu_profile_btn()

    inscription.select_inscription()
    inscription.inscription_list()
    inscription.inscription_field_price()
    inscription.inscription_list_btn()

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    windows = driver.window_handles
    time.sleep(0.3)
    driver.switch_to.window(windows[1])

    # Нажимаем кнопку для публикации инскрипции
    inscription.sign_btn()
    time.sleep(0.3)

    # Переключаемся обратно на основное окно
    driver.switch_to.window(windows[0])

    # Проверка сообщения об ошибке после публикации инскрипции
    expected_sign_error = "Inscription(s) listed successfully"
    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "go3958317564"))
        )
        assert error_message.is_displayed(), "Сообщение об ошибке не отображается"
        assert error_message.text == expected_sign_error, f"Ожидалось сообщение об ошибке: '{expected_sign_error}', но получено: '{error_message.text}'"
    except Exception as e:
        pytest.fail(f"Ошибка при проверке сообщения об ошибке после публикации: {e}")

    # Возвращаемся к списку инскрипций
    inscription.select_inscription()
    inscription.inscription_unlist()
    inscription.inscription_unlist_btn()

    # Проверка сообщения об ошибке после аннулирования инскрипции
    expected_unlist_error = "Inscription(s) listed successfully"
    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "go3958317564"))
        )
        assert error_message.is_displayed(), "Сообщение об ошибке не отображается"
        assert error_message.text == expected_unlist_error, f"Ожидалось сообщение об ошибке: '{expected_unlist_error}', но получено: '{error_message.text}'"
    except Exception as e:
        pytest.fail(f"Ошибка при проверке сообщения об ошибке после аннулирования: {e}")