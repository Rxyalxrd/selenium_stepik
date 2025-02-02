import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.7/4/index.html')

    scroll = browser.find_element(By.ID, 'main_container')

    last_height = browser.execute_script('return arguments[0].scrollHeight', scroll)

    while True:
        browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scroll)
        time.sleep(1)
        new_height = browser.execute_script('return arguments[0].scrollHeight', scroll)

        if last_height == new_height:
            break

        last_height = new_height

    even_checkboxes = browser.find_elements(By.XPATH, '//input[number(@value) mod 2 = 0]')

    for even_checkbox in even_checkboxes:
        even_checkbox.click()

    alert_button = browser.find_element(By.CLASS_NAME, 'alert_button')
    alert_button.click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

    time.sleep(3)
