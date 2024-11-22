import time
import allure
import pytest
from autotests.tests.mane_site_tests.test_connect import connect_valid_wallet
from autotests.pages.mane_site.nintondo_mane import NintondoUserMenu
from autotests.pages.mane_site.nintondo_profile import Inscriptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver")
@allure.feature("Testing valid inscription listing")
# Checking the publication and withdrawal of inscriptions from sale
def test_valid_inscription_list(driver):

    connect_valid_wallet(driver)
    time.sleep(0.5)

    menu = NintondoUserMenu(driver)
    inscription = Inscriptions(driver)

    menu.open_menu()
    menu.menu_profile_btn()

    inscription.select_inscription()
    time.sleep(0.3)
    
    inscription.inscription_field_price()
    inscription.inscription_list_btn()

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    windows = driver.window_handles
    time.sleep(0.3)
    driver.switch_to.window(windows[1])
    driver.set_window_size(1280, 1280)

    inscription.sign_btn()
    time.sleep(0.3)

    driver.switch_to.window(windows[0])

    expected_success_message = "Inscription(s) listed successfully"
    try:
        success_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "go3958317564")))
        
        assert success_message.is_displayed(), "The success message is not displayed"
        assert success_message.text == expected_success_message, \
            f"Expected success message: '{expected_success_message}', but got: '{success_message.text}'"
    except Exception as e:
        pytest.fail(f"Error when checking success message after publication: {e}")
        

@pytest.mark.usefixtures("driver")
@allure.feature("Test valid inscription unlisting")

def test_valid_inscription_unlist(driver):

    connect_valid_wallet(driver)
    time.sleep(0.5)

    menu = NintondoUserMenu(driver)
    inscription = Inscriptions(driver)

    menu.open_menu()
    menu.menu_profile_btn()
    time.sleep(0.5)
    inscription.select_inscription()
    inscription.inscription_unlist()
    time.sleep(0.5)
    inscription.inscription_unlist_btn()

    expected_unlist_error = "Inscription(s) listed successfully"
    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "go3958317564"))
        )
        assert error_message.is_displayed(), "The error message is not displayed"
        assert error_message.text == expected_unlist_error, f"An error message was expected: '{expected_unlist_error}', but received: '{error_message.text}'"
    except Exception as e:
        pytest.fail(f"Error when checking error message after cancelation: {e}")


@pytest.mark.usefixtures("driver")
@allure.feature("Testing invalid inscription listing")
@pytest.mark.parametrize("amount, expected_error, check_type", [
    ("21000001", "Price should be less than 21,000,000 BEL", "group2"),
    ("0", "Invalid price", "group1"),
    ("0.00000001", "Price must be at least 1000 satoshi", "group1"),
])

def test_invalid_inscription_list(driver, amount, expected_error, check_type):

    connect_valid_wallet(driver)
    time.sleep(0.5)

    menu = NintondoUserMenu(driver)
    inscription = Inscriptions(driver)

    menu.open_menu()
    menu.menu_profile_btn()

    inscription.select_inscription()
    inscription.inscription_list()
    inscription.inscription_field_invalid_price(amount)

    try:
        # Check for the first group of parameters
        if check_type == "group1":
            inscription.inscription_list_btn()
            error_message = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "go3958317564"))
            )
            assert error_message.is_displayed(), "No error message is displayed"
            assert error_message.text == expected_error, f"An error message was expected: '{expected_error}', but received: '{error_message.text}'"

        elif check_type == "group2":
            error_message_under_field = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'styles_errorText__')]"))
            )
            error_text = error_message_under_field.text
            allure.attach(error_text, name="Error Message Under Field", attachment_type=allure.attachment_type.TEXT)

            assert error_message_under_field.is_displayed(), "The error message below the input field is not displayed"
            assert error_text == expected_error, f"An error message was expected: '{expected_error}', but received: '{error_text}'"

    except Exception as e:
        pytest.fail(f"Message validation error: {e}")