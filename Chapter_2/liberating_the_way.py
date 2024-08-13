import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    """
    Кодовое имя: Операция "Освобождение Пути"

    В вашем пути к завершению задачи на курсе внезапно возникла преграда: элемент, 
    который вам необходимо кликнуть, оказался перекрыт другим элементом. Вы столкнулись с ошибкой,
    
    selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted: 
    Element <button class="btn" onclick="clicks()">...</button> is not clickable at point (135, 179). 
    Other element would receive the click: <div class="block2"></div>
    
    и теперь вашей задачей является обойти это препятствие. 
    Необходимо научиться получать фокус нужного элемента, даже 
    если он перекрыт другими объектами на странице.
    """

    browser.get('https://parsinger.ru/scroll/4/index.html')

    all_buttons = browser.find_elements(By.CLASS_NAME, 'visibility')

    answer = 0

    for button in all_buttons:
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
        answer += int(browser.find_element(By.ID, 'result').text)

    print(answer)

    time.sleep(3)