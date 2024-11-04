import time
import allure
import pytest
from Nintondo.AutoTests.Pages.Registration_page import CreateMnemonic
from Nintondo.AutoTests.Data import Data
from Nintondo.AutoTests.Pages.Nintondo_Mane import NintondoPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from Nintondo.AutoTests.conftest import driver
from Nintondo.AutoTests.tests.test_connect import test_connect
from Nintondo.AutoTests.Pages.Nintondo_Mane import NintondoUserMenu

@pytest.mark.usefixtures("driver")
@allure.feature("Test inscription sale")
# Тестируем публикацию инскрипций на продажу
def test_inscription_sale(driver):

    test_connect(driver)

    menu = NintondoUserMenu(driver)

    menu.open_menu()
    menu.menu_profile_btn()
    time.sleep(3)



