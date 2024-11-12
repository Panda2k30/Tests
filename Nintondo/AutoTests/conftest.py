import os
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException
import allure

@pytest.fixture(autouse=True, scope="function")
def driver(request):

    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1280,720")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')

    project_path = os.path.dirname(os.path.abspath(__file__))
    extension_path = f"{project_path}/extension/dist/chrome"

    # extension_path = "/app/extension"
    options.add_argument(f"--load-extension={extension_path}")

    # Initialize the driver
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(4)
    print("Driver initialized")

    driver.get('chrome://newtab')

    # Directory for screenshots
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)

    yield driver

    # Trying to create a screenshot for the gait
    screenshot_path = f"{screenshot_dir}/{request.node.name}.png"
    try:
        if len(driver.window_handles) > 0:
            driver.save_screenshot(screenshot_path)
            allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        else:
            print("Screenshot not saved, as all windows were closed")
    except NoSuchWindowException:
        print("Window closed, screenshot not done")
    finally:
        driver.quit()