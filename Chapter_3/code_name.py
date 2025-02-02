import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    """
    Космические просторы, бескрайние и непредсказуемые. Ваш корабль потерпел крушение, и
    теперь весь ценный груз — кусочки урана — беспорядочно плавают в открытом космосе. Но
    у вас есть инструменты, чтобы помочь своей команде и вернуть уран обратно.

    Используя возможности Selenium, напишите скрипт, который найдет и "соберет" все кусочки
    урана, кликнув по ним. Как только последний кусочек урана будет собран, вы получите в
    alert секретный код. Этот код — ваш билет на базу. Найдите его и используйте.
    """

    browser.get('https://parsinger.ru/selenium/5.7/1/index.html')

    scroll_element = browser.find_element(By.XPATH, '//*[@id="floating-container"]/div')

    last_height = browser.execute_script("return arguments[0].scrollHeight", scroll_element)

    while True:
        browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_element)
        time.sleep(0.2)

        new_height = browser.execute_script("return arguments[0].scrollHeight", scroll_element)

        if new_height == last_height:
            break
        last_height = new_height

    uranium = browser.find_elements(By.CLASS_NAME, 'button-container')

    for element in uranium:
        element.click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

    time.sleep(3)


