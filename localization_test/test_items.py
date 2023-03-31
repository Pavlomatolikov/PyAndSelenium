from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_is_present(browser):
    browser.get(link)
    try:
        add_to_basket_button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        is_button_visible = add_to_basket_button.is_displayed()
    except NoSuchElementException:
        is_button_visible = False
    assert is_button_visible, "Add to basket button not displayed"
        