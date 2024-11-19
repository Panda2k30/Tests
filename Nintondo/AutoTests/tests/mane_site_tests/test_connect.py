import time
import allure
import pytest
from AutoTests.tests.wallet_tests.test_wallet_recovery_by_private_key import restore_by_private_key_proc
from AutoTests.pages.mane_site.nintondo_mane import NintondoPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from AutoTests.pages.wallet.wallet_mane_page import ManePage


@pytest.mark.usefixtures("driver")
@allure.feature("Test Connect wallet_tests")
def test_connect(driver):

    ex_id, password = restore_by_private_key_proc(driver)

    change_network = ManePage(driver)

    change_network.get_balance()
    change_network.change_network(ex_id)

    connect = NintondoPage(driver)

    driver.get("https://nintondo.io/")

    time.sleep(0.2)
    connect.change_network_btn()

    driver.set_window_size(800, 768)

    time.sleep(0.2)
    connect.connect_btn()

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    windows = driver.window_handles
    time.sleep(0.3)
    driver.switch_to.window(windows[1])

    page_title = driver.title
    allure.attach(page_title, name="Page Title", attachment_type=allure.attachment_type.TEXT)

    allure.attach(f"Switched to the new window. Page title: {page_title}", name="Window Switch Action", attachment_type=allure.attachment_type.TEXT)

    connect.sign_btn()
    time.sleep(0.5)
    
    driver.switch_to.window(windows[0])
    driver.set_window_size(1280, 720)
    
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(@id, 'headlessui-popover-button')]"))
    )

    assert element is not None, "Element with the specified class was not found."
    