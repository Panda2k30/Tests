import time
import allure
import pytest
from autotests.tests.mane_site_tests.test_connect import connect_valid_wallet, connect_zero_balance_wallet
from autotests.pages.mane_site.nintondo_mane import NintondoUserMenu
from autotests.pages.mane_site.nintondo_profile import Inscriptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver")
@pytest.mark.xfail(reason="this run removes the inscription from the listing, in case of an error")
def test_unlist_error_(driver):

    connect_valid_wallet(driver)

    inscription = Inscriptions(driver)

    driver.get('https://nintondo.io/belinals/address/tbel1qxdp6v2u0q0tthc67e8sz2t3udykz99yrmnmvc5?content_filter=images')

    inscription.select_inscription()
    inscription.inscription_unlist()
    time.sleep(0.5)
    inscription.inscription_unlist_btn()

test_passed = False

@pytest.mark.usefixtures("driver")
@allure.feature("Testing valid purchase inscription")
def test_valid_purchase_inscription(driver):
    global test_passed

    connect_valid_wallet(driver)
    
    inscription = Inscriptions(driver)
    
    driver.get('https://nintondo.io/belinals/address/tbel1qxdp6v2u0q0tthc67e8sz2t3udykz99yrmnmvc5?content_filter=images')
    driver.set_window_size(1280, 1280)
    time.sleep(0.5)
    
    inscription.select_inscription()
    inscription.inscription_list()
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


    # expected_sign_error = "Inscription(s) listed successfully"
    # try:
    #     error_message = WebDriverWait(driver, 10).until(
    #         EC.visibility_of_element_located((By.CLASS_NAME, "go3958317564"))
    #     )
    #     assert error_message.is_displayed(), "The error message is not displayed"
    #     assert error_message.text == expected_sign_error, f"An error message was expected: '{expected_sign_error}', but received: '{error_message.text}'"
    # except Exception as e:
    #     pytest.fail(f"Error when checking error message after publication: {e}")

    time.sleep(2)
    inscription.inscription_view_btn()
    inscription.inscription_buy_btn()
    time.sleep(0.5)
    inscription.inscription_confirm_btn()

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    windows = driver.window_handles
    time.sleep(0.3)
    driver.switch_to.window(windows[1])
    driver.set_window_size(1280, 1280)

    inscription.sign_btn()
    time.sleep(0.3)
    
    driver.switch_to.window(windows[0])

    expected_success_message = "Successfully bought"
    try:
        success_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "go3958317564")))
        
        assert success_message.is_displayed(), "The success message is not displayed"
        assert success_message.text == expected_success_message, \
            f"Expected success message: '{expected_success_message}', but got: '{success_message.text}'"
    except Exception as e:
        pytest.fail(f"Error when checking success message after publication: {e}")
        

@pytest.mark.usefixtures("driver")
@pytest.mark.skipif(test_passed, reason="Test skipped because the previous test passed")
def test_unlist_error_inscription(driver):

    connect_valid_wallet(driver)

    inscription = Inscriptions(driver)

    driver.get('https://nintondo.io/belinals/address/tbel1qxdp6v2u0q0tthc67e8sz2t3udykz99yrmnmvc5?content_filter=images')

    inscription.select_inscription()
    inscription.inscription_unlist()
    time.sleep(0.5)
    inscription.inscription_unlist_btn()

        
@pytest.mark.usefixtures("driver")
@allure.feature("Testing the purchase inscriptions if there are insufficient funds on the balance")
# 
def test_purchase_inscription_without_money(driver):

    connect_zero_balance_wallet(driver)

    menu = NintondoUserMenu(driver)
    inscription = Inscriptions(driver)

    driver.get('https://nintondo.io/belinals/address/tbel1qakfl52nkd9wp4tse0mhfp70v8xkjhkvhyxcpmd')
    
    time.sleep(0.3)
    inscription.inscription_view_btn()
    time.sleep(0.3)
    inscription.inscription_buy_btn()
    
    expected_error_message = "Insufficient funds"
    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "go3958317564")))
        
        assert error_message.is_displayed(), "The success message is not displayed"
        assert error_message.text == expected_error_message, \
            f"Expected success message: '{expected_error_message}', but got: '{error_message.text}'"
    except Exception as e:
        pytest.fail(f"Error when checking success message after publication: {e}")        