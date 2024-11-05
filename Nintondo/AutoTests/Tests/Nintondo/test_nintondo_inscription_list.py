import time
import allure
import pytest
from Nintondo.AutoTests.conftest import driver
from Nintondo.AutoTests.Tests.Nintondo.test_connect import test_connect
from Nintondo.AutoTests.Pages.Nintondo.nintondo_mane import NintondoUserMenu
from Nintondo.AutoTests.Pages.Nintondo.nintondo_profile import ProfilePage, Inscriptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures("driver")
@allure.feature("Test inscription list")
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

    inscription.sign_btn()
    time.sleep(0.3)





