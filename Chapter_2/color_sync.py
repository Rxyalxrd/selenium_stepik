import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    """
    Операция "Цветовая Синхронизация"
    
    Здравствуйте, аспиранты автоматизации! Сегодня перед вами задача, которая 
    перенесёт нас в мир цветов, чисел и быстрых решений. Вас ждёт настоящий 
    квест на ловкость рук и точность кода. Сможете ли вы перенести данные так, 
    чтобы они заиграли новыми красками? На этот раз задание не только проверит 
    вашу скорость, но и научит работать с изменением стилей элементов на странице. 
    Скорость и точность — вот ваши лучшие союзники в этой миссии!
    """

    browser.get('https://parsinger.ru/selenium/5.5/4/1.html')

    all_boxes = browser.find_elements(By.CLASS_NAME, 'parent')

    for box in all_boxes:

        gray_textarea = box.find_element(By.XPATH, './/textarea[@color="gray"]')
        gray_text = gray_textarea.text

        blue_textarea = box.find_element(By.XPATH, './/textarea[@color="blue"]')
        blue_textarea.send_keys(gray_text)

        gray_textarea.clear()

        box.find_element(By.TAG_NAME, 'button').click()

    browser.find_element(By.ID, 'checkAll').click()

    print(browser.find_element(By.ID, 'congrats').text)

    time.sleep(3)
