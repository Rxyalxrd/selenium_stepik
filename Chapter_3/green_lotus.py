import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


with webdriver.Chrome() as browser:
    """
    🕰️ Представьте себе момент, когда время замирает, и все вокруг зависает
    в ожидании вашего действия. Вы стоите перед четырьмя кнопками, каждая
    из которых — ваш шанс изменить ход событий. Но в этой задаче важно не
    только нажать, но и удерживать. Да-да, вы не ослышались. 

    Чтобы пройти эту задачу, вам нужно приручить каждую кнопку, удерживая
    соответствующую её до тех пор, пока она не станет зелёной. Значение
    value="3.3" каждой кнопки указывает на минимальное время в секундах
    (float()), которое необходимо выдержать.

    🔮 Как только все кнопки обретут изумрудный оттенок, ваше терпение будет
    вознаграждено: появится сообщение в alert, скрывающее в себе ключ к
    следующему испытанию. Этот ключ нужно вставить в поле ответа на Stepiк,
    чтобы продвинуться дальше по курсу.
    """

    browser.get('https://parsinger.ru/selenium/5.7/5/index.html')
    action = ActionChains(browser)

    fields = browser.find_elements(By.CLASS_NAME, 'timer_button')

    for field in fields:
        field.click()
        hold_time = float(field.text)
        action.click_and_hold(field).pause(hold_time).release(field).perform()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

    time.sleep(3)
