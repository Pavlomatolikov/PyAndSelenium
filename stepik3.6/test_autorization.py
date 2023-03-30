import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import math

answer = math.log(int(time.time()))


# @pytest.mark.parametrize('address', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
@pytest.mark.parametrize('address', ["236895"])
def test_user_can_login(browser, address):
    link = f"https://stepik.org/lesson/{address}/step/1"
    browser.get(link)

    login_button = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ember33")))
    login_button.click()

    email = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
    email.send_keys("pavlomatolikov@gmail.com")

    password = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
    password.send_keys("gFxTjP0Eoimbko2s")

    submit = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader ")
    submit.click()
    print("Waiting for pop-up hidding")
    WebDriverWait(browser, 15).until(EC.invisibility_of_element((By.ID, "ember98")))
    print("Pop-up is hide")

    state = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-type="string-quiz"]')))
    if state.get_attribute("data-state") == "wrong":
        print("IF statement")
        answer_field = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))
        answer_field.clear()
        print("Cleared")

        again = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "again-btn")))
        again.click()

        confirm = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[text()='OK']")))
        # time.sleep(3)
        # confirm = browser.find_element(By.CSS_SELECTOR, '[data-ember-action-103="103"]')
        confirm.click()
        time.sleep(15)

    else:
        print("Else statement")

        answer_field = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))
        answer_field.clear()
        my_answer = math.log(int(time.time()))

        print("Typing text")
        answer_field.send_keys(my_answer)
        print(my_answer, type(my_answer))
        send = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
        send.click()
        feedback = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
        feedback_text = feedback.text
        assert feedback_text == "Correct!"









