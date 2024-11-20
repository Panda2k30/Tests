import time
import allure
import pytest
import random
from autotests.data import Data
from selenium.webdriver.common.by import By
from autotests.tests.mane_site_tests.test_connect import test_connect
from autotests.pages.mane_site.nintondo_mane import NintondoUserMenu
from autotests.pages.mane_site.nintondo_profile import Image


@pytest.mark.usefixtures("driver")
@allure.feature("Test valid change user profile image")

def test_valid_change_image(driver):
    
    random_id = random.choice(Data.ID)

    test_connect(driver)
    time.sleep(0.5)

    menu = NintondoUserMenu(driver)
    profile = Image(driver)

    menu.open_menu()
    menu.menu_profile_btn()
    
    profile.image_btn()
    old_url = profile.image_url()
    profile.image_field(random_id)
    profile.image_save_btn()
    
    driver.refresh
    
    profile.image_btn()
    new_url = profile.image_url()
    
    # time.sleep(5)
    
    assert old_url != new_url, f"Avatar URL did not change! Old URL: {old_url}, New URL: {new_url}"

    allure.attach(f"Old Image URL: {old_url}", name="Old Image URL", attachment_type=allure.attachment_type.TEXT)
    allure.attach(f"New Image URL: {new_url}", name="New Image URL", attachment_type=allure.attachment_type.TEXT)
    
    
@pytest.mark.usefixtures("driver")
@allure.feature("Test invalid change user profile image")

def test_invalid_change_image(driver):
    
    random_id = random.choice(Data.INVALID_ID)

    test_connect(driver)
    time.sleep(0.5)

    menu = NintondoUserMenu(driver)
    profile = Image(driver)

    menu.open_menu()
    menu.menu_profile_btn()
    
    profile.image_btn()
    profile.image_url()
    profile.image_field(random_id)
    
    save_button = driver.find_element(By.XPATH, "//button[text()='Save']")
    is_disabled = save_button.get_attribute("disabled")
    assert is_disabled == "true", "Save button is not disabled when it should be!"

    error_message = driver.find_element(By.XPATH, "//div[text()='Inscription is not yours']")
    assert error_message.is_displayed(), "Error message 'Inscription is not yours' did not appear!"
    
    
    
    
    
    
    