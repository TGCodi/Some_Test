from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    """Данные"""
    Site_link = ("https://suninjuly.github.io/find_link_text")
    browser = webdriver.Chrome()

    """Переход на сайт"""
    browser.get(Site_link)
    time.sleep(3)

    """Переход по ссылке"""
    link = browser.find_element(By.LINK_TEXT, "224592")
    link.click()
    time.sleep(0.25)

    """Ввод имени"""
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    time.sleep(0.10)

    """Ввод фамилии"""
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Ivanov")
    time.sleep(0.10)

    """Ввод города"""
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")
    time.sleep(0.10)

    """Ввод страны"""
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    time.sleep(0.10)

    """Клик по кнопке"""
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()