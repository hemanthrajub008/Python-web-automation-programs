from selenium import webdriver
from selenium.webdriver.common.by import By


def test_sig_in_to_orange_HRM_website():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    # Set implicit wait
    driver.implicitly_wait(10)  # seconds

    # Perform actions (e.g., find elements, assert conditions)
    try:
        element = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-branding")
        assert "OrangeHRM" in element.text
        print("Text 'OrangeHRM' is present in the element.")
    except Exception as e:
        print(f"An exception occurred: {e}")
    finally:
        driver.quit()
