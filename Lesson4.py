from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import sin, log


def cal(x):
    return log(abs(12*sin(int(x))))


try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()

    browser.get(link)
    sleep(0.2)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print(x)
    print(cal(x))
    pa = cal(x)

    input = browser.find_element(By.ID, "answer")      ## Строка для значения
    input.send_keys(pa)
    sleep(0.3)

    browser.execute_script("window.scrollBy(0, 150);")

    checkbox = browser.find_element(By.ID, "robotCheckbox")       ## Чекбокс
    checkbox.click()
    sleep(0.3)


    radiobutton = browser.find_element(By.ID, "robotsRule")        ## Радиобаттон
    radiobutton.click()
    sleep(0.3)


    #browser.execute_script("window.scrollBy(0, 300);")


    button = browser.find_element(By.CLASS_NAME, "btn")         ## Кнопка отправить
    button.click()

finally:
    sleep(5)
    browser.quit()
