from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

try:
    link = "https://suninjuly.github.io/file_input.html"
    file_path = "/Users/nnefedov/Documents/Nikita/Python/Site/Selenuim Kyrs/new.txt"
    browser = webdriver.Chrome()
    browser.get(link)
    sleep(0.2)

    firstNameinput = browser.find_element(By.CSS_SELECTOR, "[name=firstname]")
    firstNameinput.send_keys("Ivan")
    sleep(0.2)

    lastnameinput = browser.find_element(By.CSS_SELECTOR, "[name=lastname]")
    lastnameinput.send_keys("Kireev")
    sleep(0.2)

    emailinput = browser.find_element(By.CSS_SELECTOR, "[name=email]")
    emailinput.send_keys("Ivank@mail.com")
    sleep(0.2)

    fileDOWN = browser.find_element(By.CSS_SELECTOR, "[type=file]")
    fileDOWN.send_keys(file_path)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    sleep(5)

    browser.quit()