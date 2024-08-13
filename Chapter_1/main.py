import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    """
    Представьте себя в роли охотника за сокровищами в мире интернета. 
    Ваша задача проста: найти загадочную ссылку с текстом 16243162441624 на указанной странице. 
    Звучит легко, правда? Однако, есть одна особенность — найти эту ссылку нужно автоматически, 
    без ручного поиска. Так вы проверите свои навыки в автоматизации и сможете использовать их для 
    более сложных задач в будущем.

    Вторая задачка тоже довольна проста. 
    Вспоминаем метод By.PARTIAL_LINK_TEXT или By.LINK_TEXT, который ищет ссылку по частичному или 
    полному совпадению текста.
    """

    browser.get('https://parsinger.ru/selenium/2/2.html')
    input_form = browser.find_element(By.LINK_TEXT, '16243162441624')
    input_form.click()
    answer_field = browser.find_element(By.ID, 'result')
    print(answer_field.text)
    time.sleep(3)
