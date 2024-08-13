import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    """
    Приветствую, будущие аналитики данных и веб-скрейперы! 
    Перед вами стоит задача, которая требует не только знаний в программировании, 
    но и внимания к деталям. Вам нужно "прочитать" секретный кодекс, спрятанный на веб-странице. 
    Кодекс разбит на 300 фрагментов и каждый из них хранится в отдельном теге <p>. 
    
    Ваша задача — собрать все эти фрагменты воедино.
    """

    browser.get('https://parsinger.ru/selenium/3/3.html')

    data_from_tag_p = browser.find_elements(By.TAG_NAME, 'p')

    answer = 0

    for field in data_from_tag_p:
        answer += int(field.text)

    print(answer)
    time.sleep(3)
