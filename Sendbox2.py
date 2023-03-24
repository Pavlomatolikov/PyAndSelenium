import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "book")))
    button.click()

    val = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)

    result = calc(val)

    field = browser.find_element(By.CSS_SELECTOR, "#answer")
    field.send_keys(result)

    submit = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "solve")))
    submit.click()
    time.sleep(15)
    # message = browser.find_element(By.ID, "verify_message")
    #
    # assert "successful" in message.text

finally:
    browser.quit()