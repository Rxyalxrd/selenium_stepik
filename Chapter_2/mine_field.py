import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    """
    Операция "Минное поле"
    
    Привет, будущие автоматизаторы! Сегодня у нас не просто задача, 
    а настоящий тайм-триал, испытание на скорость и точность! Мы 
    переносимся в мир, где каждое неверное движение может стать последним... 
    ну, или по крайней мере, приведёт к неудачному выполнению задания. Задача 
    симулирует реальную рабочую ситуацию, в которой на скорость выполнения 
    операций поставлен жесткий лимит.
    """

    browser.get('https://parsinger.ru/selenium/5.5/2/1.html')

    all_open_fields = browser.find_elements(By.XPATH, '//input[@data-enabled="true"]')

    for field in all_open_fields:
        field.clear()

    browser.find_element(By.ID, 'checkButton').click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

    time.sleep(3)
