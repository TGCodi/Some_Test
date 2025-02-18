from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def sum_f(x,y):
    return str(int(x) + int(y))

try:
    """Данные"""
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    """Открыть сайт"""
    browser.get(link)
    time.sleep(0.10)
    """Элемент х"""
    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text
    """Элемент у"""
    y_element = browser.find_element(By.ID, "num2")
    y = y_element.text

    xy = sum_f(x,y)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(xy)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()



finally:
    time.sleep(7)
    browser.quit()
