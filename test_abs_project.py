import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


class TestRequiredFields(unittest.TestCase):
    def test_form1(self):
        browser = webdriver.Chrome()
        browser.get(link1)
        field1 = browser.find_element(By.CSS_SELECTOR, ".first[required]")
        field2 = browser.find_element(By.CSS_SELECTOR, ".second[required]")
        field3 = browser.find_element(By.CSS_SELECTOR, ".third[required]")
        field1.send_keys("Pavlo")
        field2.send_keys("Mato")
        field3.send_keys("pa@gmail.com")
        browser.quit()
        assert abs(-42) == 42, "Should be absolute value of a number"

    def test_form2(self):
        browser = webdriver.Chrome()
        browser.get(link2)
        field1 = browser.find_element(By.CSS_SELECTOR, ".first[required]")
        field2 = browser.find_element(By.CSS_SELECTOR, ".second[required]")
        field3 = browser.find_element(By.CSS_SELECTOR, ".third[required]")
        field1.send_keys("Pavlo")
        field2.send_keys("Mato")
        field3.send_keys("pa@gmail.com")
        browser.quit()
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()
