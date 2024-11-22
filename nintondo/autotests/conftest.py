import os
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException
import allure

@pytest.fixture(autouse=True, scope="function")
def driver(request):
    
    options = webdriver.ChromeOptions()

    options.add_argument("--disable-animations")

    prefs = {"profile.managed_default_content_settings.images": 2} 
    options.add_experimental_option("prefs", prefs)

    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1280,720")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')

    # project_path = os.path.dirname(os.path.abspath(__file__))
    # extension_path = f"{project_path}/extension/dist/chrome"
    
    # CI
    extension_path = "/app/extension" 
    
    options.add_argument(f"--load-extension={extension_path}")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(4)
    allure.attach("- Driver initialized", name="Driver", attachment_type=allure.attachment_type.TEXT)

    driver.get('chrome://newtab')
    
    driver.execute_script("""
        var style = document.createElement('style');
        style.innerHTML = '*, *::before, *::after { transition: none !important; animation: none !important; }';
        document.head.appendChild(style);
    """)

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
            # Attach for when the window is closed
            allure.attach("Screenshot not saved, as all windows were closed", name="Screenshot Status", attachment_type=allure.attachment_type.TEXT)
    except NoSuchWindowException:
        # Attach for window error case
        allure.attach("Window closed, screenshot not done", name="Screenshot Status", attachment_type=allure.attachment_type.TEXT)
    finally:
        driver.quit()