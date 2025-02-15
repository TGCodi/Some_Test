from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin

def calc(numba):
    return str(log(abs(12 * sin(int(x)))))

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()

    browser.get(link)
    time.sleep(1)

    x_line = browser.find_element(By.TAG_NAME, "img")
    x_element = x_line.get_attribute("valuex")
    x = x_element
    y = calc(x)

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)
    time.sleep(0.25)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    button = browser.find_element(By.TAG_NAME,"button")
    button.click()

finally:
    time.sleep(5)

    browser.quit()


