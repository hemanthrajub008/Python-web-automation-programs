# import logging

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

# driver = webdriver.Chrome()
# logger = logging.getLogger('selenium')

from selenium.webdriver.common.by import By
import time


def test_login_to_make_appointment():
    driver = webdriver.Chrome()

    driver.get("https://katalon-demo-cura.herokuapp.com/")

    driver.maximize_window()

    appointment_button_element = driver.find_element(By.ID, "btn-make-appointment")
    appointment_button_element.click()
    time.sleep(3)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"


    userid_element = driver.find_element(By.XPATH, "//input[starts-with(@id, 'txt-username')]")

    userid_element.send_keys('John Doe')

    password_element = driver.find_element(By.XPATH, "//input[starts-with(@id, 'txt-password')]")

    password_element.send_keys('ThisIsNotAPassword')

    login_button = driver.find_element(By.ID, 'btn-login')

    login_button.click()


    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"

    make_appointment_label = driver.find_element(By.XPATH,"//h2[contains(text(),\"Make Appointment\")]")

    assert make_appointment_label.text == "Make Appointment"

    print( make_appointment_label)

    driver.quit()
