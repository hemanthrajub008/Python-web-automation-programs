import time

import pytest
import allure
from allure_commons.types import AttachmentType

from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.smoke
@allure.title("Verify that login is working in iDrive website")
@allure.description("Verifying the warning notice as Your free trial has expired message after login.")
def test_sign_in_to_iDrive_360():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login/")
    driver.maximize_window()
    time.sleep(2)

    allure.attach(driver.get_screenshot_as_png(), name="signin_page-screenshot", attachment_type=AttachmentType.PNG)

    emailid_element = driver.find_element(By.XPATH, "//input[starts-with(@name, 'username')]")

    emailid_element.send_keys('augtest_040823@idrive.com')

    password_element = driver.find_element(By.XPATH, "//input[starts-with(@name, 'password')]")

    password_element.send_keys("123456")

    sign_in_button = driver.find_element(By.ID, 'frm-btn')
    sign_in_button.click()

    time.sleep(20)
    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"
    free_trail_expired_label = driver.find_element(By.XPATH, '//h5[contains(@class, \'id-card-title\')]')
    assert free_trail_expired_label.text == "Your free trial has expired"
    allure.attach(driver.get_screenshot_as_png(), name="free_trail_expired-screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(1)
    driver.quit()
