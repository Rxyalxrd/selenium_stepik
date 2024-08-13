import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    """
    Операция "Выпадающие списки"
    
    Приветствую, агенты-разработчики! Сегодня наша миссия — "Операция 'Выпадающие списки'".
    В этой операции мы сталкиваемся с нечто большим, чем просто чек-боксы или текстовые поля.
    Мы имеем дело с выпадающим списком, содержащим ключи к секретному хранилищу данных.
    """

    browser.get('https://parsinger.ru/selenium/7/7.html')

    all_values = browser.find_elements(By.TAG_NAME, 'option')

    sum_values = 0

    for value in all_values:
        sum_values += int(value.text)

    input_sum = browser.find_element(By.ID, 'input_result')
    input_sum.send_keys(sum_values)

    submit = browser.find_element(By.CLASS_NAME, 'btn')
    submit.click()

    print(browser.find_element(By.ID, 'result').text)

    time.sleep(3)
