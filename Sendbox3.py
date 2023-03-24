import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    first_name.send_keys("Pavlo")

    last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    last_name.send_keys("Mato")

    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys("Pavlo@gmail.com")

    dir_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(dir_path, 'Sendbox4.py')

    upload = browser.find_element(By.CSS_SELECTOR, "#file")
    upload.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    time.sleep(5)

finally:
    browser.quit()