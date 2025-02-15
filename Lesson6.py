from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import log, sin

def somef(x):
    return log(abs(12*sin(int(x))))

try:
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    sleep(0.3)

    button1 = browser.find_element(By.CSS_SELECTOR, "[type=submit].btn")
    button1.click()

    alert = browser.switch_to.alert
    alert.accept()
    sleep(0.3)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    result = somef(x)

    answer = browser.find_element(By.CSS_SELECTOR, ".form-control#answer")
    answer.send_keys(result)

    finbutton = browser.find_element(By.CLASS_NAME, "btn")
    finbutton.click()

finally:
    sleep(5)

    browser.quit()