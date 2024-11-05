# import time
# import allure
# import pytest
# from Nintondo.AutoTests.conftest import driver
# from Nintondo.AutoTests.Tests.Nintondo.test_nintondo_inscription_list import test_inscription_list
# from Nintondo.AutoTests.Pages.Nintondo.nintondo_mane import NintondoUserMenu
# from Nintondo.AutoTests.Pages.Nintondo.nintondo_profile import ProfilePage, Inscriptions
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
#
# @pytest.mark.usefixtures("driver")
# @allure.feature("Test inscription unlist")
#
# def test_inscription_unlist(driver):
#
#     test_inscription_list(driver)
#
#     menu = NintondoUserMenu(driver)
#     profile = ProfilePage(driver)
#     inscription = Inscriptions(driver)
#
#     menu.open_menu()
#     menu.menu_profile_btn()
#
#     inscription.select_inscription()
#     inscription.inscription_list()
#     inscription.inscription_field_price()
#     inscription.inscription_list_btn()
#
