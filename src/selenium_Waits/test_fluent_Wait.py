from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_sig_in_to_orange_HRM_website():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
    wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=ignore_list)

    try:
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".orangehrm-login-branding"), "OrangeHRM")
        )
        print("Text 'OrangeHRM' is present in the element.")
    except Exception as e:
        print(f"An exception occurred: {e}")
    finally:
        driver.quit()
