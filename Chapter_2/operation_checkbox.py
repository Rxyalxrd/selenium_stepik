import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    """
    Числовая Добыча: Операция 'Чекбокс'!

    Привет, исследователи данных и веб-магистры! Сегодня перед нами стоит задача,
    которая требует от нас не только технических навыков, но и умения быстро
    анализировать ситуацию на лету. Эта задача имитирует реальный сценарий, где
    не всё так просто, как кажется на первый взгляд. Нам нужно будет применить
    наши навыки веб-парсинга, чтобы выделить конкретные данные из большого массива.
    """

    browser.get('https://parsinger.ru/selenium/5.5/3/1.html')

    all_buttons = browser.find_elements(By.CLASS_NAME, 'parent')

    answer = 0

    for button in all_buttons:
        checkbox = button.find_element(By.CLASS_NAME, 'checkbox').is_selected()
        if checkbox:
            answer += int(button.find_element(By.TAG_NAME, 'textarea').text)

    print(answer)

    time.sleep(3)
