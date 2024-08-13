import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    """
    Поход за сокровищами в Цифровом Лабиринте
    
    Привет, юные искатели данных и загадок! 
    Перед вами лежит миссия, которая проверит ваше умение внимательно "читать" 
    веб-страницы и извлекать из них нужную информацию. На таинственной странице 
    скрыты фрагменты артефакта — всего их 100. Они зашифрованы и размещены во вторых 
    абзацах каждого из 200 блоков текста. Ваша задача — собрать их и воссоздать артефакт.
    """

    browser.get('https://parsinger.ru/selenium/3/3.html')

    data_from_tag_p = browser.find_elements(By.XPATH, '//div[@class="text"]/p[2]')

    answer = 0

    for field in data_from_tag_p:
        answer += int(field.text)

    print(answer)
    time.sleep(3)
