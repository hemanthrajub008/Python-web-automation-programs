import time
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.smoke
@allure.title("Search for 16gb variants in ebay")
@allure.description("Searching for the 16gb variant from high cost to low cost of the item.")
def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")

    assert driver.current_url == "https://www.ebay.com/"
    driver.maximize_window()

    allure.attach(driver.get_screenshot_as_png(), name="ebay_homepage-screenshot", attachment_type=AttachmentType.PNG)
    search_box = driver.find_element(By.XPATH, "//input[@id='gh-ac']")

    search_box.send_keys("16 gb")

    search_btn = driver.find_element(By.XPATH, "//input[@id='gh-btn']")
    search_btn.click()

    list_results = driver.find_elements(By.XPATH, "//span[@role='heading']")
    for i in list_results:
        print(i.text)

    time.sleep(5)
    driver.quit()
