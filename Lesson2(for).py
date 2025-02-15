from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/huge_form.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(0.25)

    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("text")

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    time.sleep(10)

    browser.quit()

