import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    op1 = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    # op2 = int(browser.find_element(By.CSS_SELECTOR, "#num2").text)
    sum_value = calc(op1)

    field = browser.find_element(By.CSS_SELECTOR, "#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", field)
    field.send_keys(sum_value)

    # x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    # x = x_element.text
    # y = calc(value)

    # field = browser.find_element(By.CSS_SELECTOR, "#answer")
    # field.send_keys(y)
    #
    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()
    #
    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()
    #
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
