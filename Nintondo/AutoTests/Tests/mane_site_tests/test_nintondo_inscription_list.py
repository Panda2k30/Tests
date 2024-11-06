import time
import allure
import pytest
from Nintondo.AutoTests.conftest import driver
from Nintondo.AutoTests.Tests.mane_site_tests.test_connect import test_connect
from Nintondo.AutoTests.Pages.mane_site.nintondo_mane import NintondoUserMenu
from Nintondo.AutoTests.Pages.mane_site.nintondo_profile import ProfilePage, Inscriptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException


@pytest.mark.usefixtures("driver")
@allure.feature("Test valid inscription listing/unlisting")
# Проверяем публикацию и снятие инскрипций с продажи
def test_valid_inscription_list(driver):
    test_connect(driver)

    menu = NintondoUserMenu(driver)
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

    inscription.sign_btn()
    time.sleep(0.3)

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


@pytest.mark.usefixtures("driver")
@allure.feature("Test invalid inscription listing")
@pytest.mark.parametrize("amount, expected_error, check_type", [
    ("21000001", "Price should be less than 21,000,000 BEL", "group2"),
    ("0", "Invalid price", "group1"),
    ("0.00000001", "Price must be at least 1000 satoshi", "group1"),
])

# Проверяем публикацию и снятие инскрипций с продажи
def test_invalid_inscription_list(driver, amount, expected_error, check_type):
    test_connect(driver)

    menu = NintondoUserMenu(driver)
    inscription = Inscriptions(driver)

    menu.open_menu()
    menu.menu_profile_btn()

    inscription.select_inscription()
    inscription.inscription_list()
    inscription.inscription_field_invalid_price(amount)

    try:
        # Проверка для первой группы параметров
        if check_type == "group1":
            inscription.inscription_list_btn()
            error_message = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "go3958317564"))
            )
            assert error_message.is_displayed(), "Сообщение об ошибке не отображается"
            assert error_message.text == expected_error, f"Ожидалось сообщение об ошибке: '{expected_error}', но получено: '{error_message.text}'"

        # Проверка для второй группы параметров
        elif check_type == "group2":
            error_message_under_field = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'styles_errorText__')]"))
            )
            print(error_message_under_field)
            assert error_message_under_field.is_displayed(), "Сообщение об ошибке под полем ввода не отображается"
            assert error_message_under_field.text == expected_error, f"Ожидалось сообщение об ошибке: '{expected_error}', но получено: '{error_message_under_field.text}'"

    except Exception as e:
        pytest.fail(f"Ошибка при проверке сообщения: {e}")