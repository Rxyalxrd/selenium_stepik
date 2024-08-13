import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    """
    Операция: Кодовый Замок 
    
    Добро пожаловать, агенты! Сегодня перед нами стоит задача не просто 
    извлечь данные, но и взаимодействовать с интерфейсом веб-сайта, чтобы 
    добраться до скрытой информации. Представьте, что перед вами замок с 
    комбинацией в виде чек-боксов.
    """

    browser.get('https://parsinger.ru/selenium/4/4.html')

    boxes = browser.find_elements(By.CLASS_NAME, 'check')

    for box in boxes:
        box.click()

    input_box = browser.find_element(By.CLASS_NAME, 'btn')
    input_box.click()

    print(browser.find_element(By.ID, 'result').text)

    time.sleep(3)
