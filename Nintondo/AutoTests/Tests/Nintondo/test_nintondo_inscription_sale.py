import time
import allure
import pytest
from Nintondo.AutoTests.conftest import driver
from Nintondo.AutoTests.Tests.Nintondo.test_connect import test_connect
from Nintondo.AutoTests.Pages.Nintondo_Mane import NintondoUserMenu
from Nintondo.AutoTests.Pages.Nintondo_Profile import ProfilePage

@pytest.mark.usefixtures("driver")
@allure.feature("Test inscription sale")
# Тестируем публикацию инскрипций на продажу
def test_inscription_sale(driver):

    test_connect(driver)

    menu = NintondoUserMenu(driver)
    profile = ProfilePage(driver)

    menu.open_menu()
    menu.menu_profile_btn()
    time.sleep(0.2)

    profile.nickname_btn()
    profile.nickname_field()
    time.sleep(1)





