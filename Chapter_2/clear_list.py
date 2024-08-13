import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    """
    Операция "Чистый Лист"
    
    Приветствую, кодовые ниндзя! Сегодня перед вами стоит задача, 
    которую можно сравнить с миссией по деминированию — только 
    вместо бомб у нас текстовые поля, и взрывать ничего не будем. 
    Но задача не менее интригующая! Суть в том, чтобы научиться 
    быстро и эффективно взаимодействовать с элементами на 
    веб-странице. Ведь в реальных проектах скорость часто имеет решающее значение.
    """

    browser.get('https://parsinger.ru/selenium/5.5/1/1.html')

    fields = browser.find_elements(By.CLASS_NAME, 'text-field')

    for field in fields:
        field.clear()

    submit = browser.find_element(By.ID, 'checkButton')
    submit.click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

    time.sleep(3)
