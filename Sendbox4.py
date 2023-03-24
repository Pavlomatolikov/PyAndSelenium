from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

    # alert = browser.switch_to.alert
    # alert.accept()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    val = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)

    result = calc(val)

    field = browser.find_element(By.CSS_SELECTOR, "#answer")
    field.send_keys(result)

    submit = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    submit.click()

    # browser.execute_script("prompt('Hello')")
    # time.sleep(2)

    # alert = browser.switch_to.alert
    # print(alert.text)
    # alert.dismiss()

    time.sleep(10)

finally:
    browser.quit()