import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    """
    Охота на Скрытые Сокровища!
    
    Здравствуйте, искатели сокровищ во вселенной веб-страниц! 
    На этот раз перед вами стоит задача, которая напоминает 
    охоту за сокровищем. Но вместо того, чтобы копать ямы или 
    искать клады на необитаемых островах, вы будете "копать" 
    информацию на веб-странице. Эта задача проверит вашу 
    способность быть настойчивыми и терпеливыми, потому что 
    "сокровище" появляется довольно редко.
    """

    browser.get('https://parsinger.ru/methods/1/index.html')

    while True:
        answer = browser.find_element(By.ID, 'result').text
        if not answer.isdigit():
            browser.refresh()
        else:
            print(answer)
            break

    time.sleep(3)
