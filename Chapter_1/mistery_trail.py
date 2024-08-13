import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    """
     Миссия "Загадочный След"
    
    Приветствую, будущие эксперты по web-парсингу! 
    Сегодня у нас на очереди не просто задача, а настоящая миссия, 
    которую можно было бы назвать "Загадочный След". Представьте себя 
    детективами в мире веб-страниц: вам предстоит найти ключ к решению 
    на странице, используя его для "отпирания" секретов выпадающего 
    списка, и в конце — раскрывать тайну последней загадки.
    """
    constant = ((12434107696 * 3) * 2) + 1

    browser.get('https://parsinger.ru/selenium/6/6.html')

    value = browser.find_element(
        By.XPATH, f"//option[text()='{str(constant)}']"
    ).click()

    submit = browser.find_element(By.ID, "sendbutton").click()

    print(browser.find_element(By.ID, 'result').text)

    time.sleep(3)
