import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    """
    Кодовое имя: Операция "Бессмертный Печенюшка"
    
    Ваша задача как кибердетектива — найти "Бессмертный Печенюшка" среди 
    лабиринта из 42 разных ссылок. Этот мифический печенюшка не прост; он 
    обладает самым долгим сроком жизни среди всех остальных на этих страницах.
    Ваши средства — мощные инструменты языка программирования, которые не 
    оставят ему шанса скрыться от нас. Ваш ход, детектив.
    """

    browser.get('https://parsinger.ru/methods/5/index.html')
    links = []
    all_links = browser.find_elements(By.CLASS_NAME, 'urls')

    for link in all_links:
        links.append(link.find_element(By.TAG_NAME, 'a').get_attribute('href'))

    max_expiry, answer = -1, None

    for link in links:
        browser.get(link)
        expiry_time = browser.get_cookie('foo2')['expiry']

        if max_expiry < expiry_time:
            max_expiry = expiry_time
            answer = browser.find_element(By.ID, 'result').text

    print(answer)
    time.sleep(3)
