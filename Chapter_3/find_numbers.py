import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    """
    Поиск чисел.
    
    Добро пожаловать в удивительный мир веб-скрапинга, где информация
    иногда прячется в самых неожиданных местах! Ваша задача сегодня —
    вычислить и собрать числа, которые могут появиться на веб-странице.
    Они могут быть ключами к более сложным задачам или даже просто 
    интересным головоломкам.
    """

    browser.get('https://parsinger.ru/scroll/2/index.html')

    time.sleep(0.2)

    all_div_items = browser.find_elements(By.CLASS_NAME, 'item')

    answer = 0

    for div_item in all_div_items:

        checkbox = div_item.find_element(By.CLASS_NAME, 'checkbox_class')
        checkbox.click()
        try:
            answer += int(div_item.find_element(By.TAG_NAME, 'span').text)

        except:
            pass

    print(answer)

    time.sleep(3)
