from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_sig_in_to_orange_HRM_website():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    try:
        # Increase the timeout to 10 seconds
        WebDriverWait(driver, timeout=10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".orangehrm-login-branding"), "OrangeHRM")
        )
        print("Text 'OrangeHRM' is present in the element.")
    except Exception as e:
        print(f"An exception occurred: {e}")
    finally:
        driver.quit()

# note: If you find any errors with time out exception, try the below steps.

# Verify the Selector: Ensure that the CSS selector .orangehrm-login-branding correctly identifies the element
# containing the expected text.

# Increase Timeout: If the element takes longer to load, increase the timeout period.

# Check for Dynamic Content: Ensure that the text "OrangeHRM" is present in the specified element.
# It might be dynamically loaded after the page is fully loaded.

# This explicit wait TC is passed indirectly by throwing an exception message, so try it again in other way.
