import time
import allure
import pytest
from autotests.tests.mane_site_tests.test_connect import test_connect
from autotests.pages.mane_site.nintondo_mane import NintondoUserMenu
from autotests.pages.mane_site.nintondo_profile import Nickname


@pytest.mark.usefixtures("driver")
@allure.feature("Test changing user name")
@pytest.mark.parametrize("name, expected_error, check_type", [
    # ("B0b", "The username must be between 4 and 20 characters long", "group2"), # 3 characters
    ("", "Name can't be empty", "group2"), # 0 characters
    ("A1ex", "", "group1"), # 4 characters
    ("MyName1sNintondo2024", "", "group1"), # 20 characters
])

def test_change_name(driver, name, expected_error, check_type):

    test_connect(driver)
    time.sleep(0.5)

    menu = NintondoUserMenu(driver)
    profile = Nickname(driver)

    menu.open_menu()
    menu.menu_profile_btn()

    profile.nickname_btn()
    profile.nickname_field(name)
    profile.nickname_save_btn()

    if check_type == "group1":
        success_message = profile.get_success_message()
        assert success_message == "Name changed successfully", "Unexpected success message!"
        
        allure.attach(f"Success Message: {success_message}", name="Success Message", attachment_type=allure.attachment_type.TEXT)
        
        # Check if the name is changed after refreshing the page
        driver.refresh()
        saved_name = profile.get_current_name()
        assert saved_name == name, f"Expected name '{name}' but got '{saved_name}'!"

        allure.attach(f"Expected Name: {name}", name="Expected Name", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Saved Name: {saved_name}", name="Saved Name", attachment_type=allure.attachment_type.TEXT)

    elif check_type == "group2":
        error_message = profile.get_error_message()
        assert error_message == expected_error, f"Expected error '{expected_error}' but got '{error_message}'!"

        allure.attach(f"Expected Error: {expected_error}", name="Expected Error", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Error Message: {error_message}", name="Error Message", attachment_type=allure.attachment_type.TEXT)

        # Check if the name has not changed
        driver.refresh()
        saved_name = profile.get_current_name()
        assert saved_name != name, f"Name should not have changed to '{name}'!"
        
        allure.attach(f"Original Name: {name}", name="Original Name", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Saved Name after refresh: {saved_name}", name="Saved Name after refresh", attachment_type=allure.attachment_type.TEXT)
    
    