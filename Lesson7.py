from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import log, sin

def sume(x):
    return log(abs(12*sin(int(x))))

try:
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    sleep(0.4)

    button = browser.find_element(By.CSS_SELECTOR, ".trollface.btn")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    result = sume(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(result)
    sleep(0.4)

    subm_but = browser.find_element(By.CLASS_NAME, "btn")
    subm_but.click()

finally:
    sleep(5)

    browser.quit()


