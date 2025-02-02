import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

with webdriver.Chrome() as browser:
    """
    Десант в глубину: Поиск сокровищ среди скрытых элементов.
    
    Добро пожаловать в мир загадочных данных, где информация не
    так просто дается в руки исследователей. В этой задаче, схожей
    с пещеролазанием в глубины веба, вам предстоит использовать
    Selenium и дополнительный инструментарий ActionChains для
    автоматизации глубокого скроллинга. Цель? Собрать все числа из 
    недр этой цифровой пещеры и скомпоновать их в одну общую сумму.
    """

    browser.get('https://parsinger.ru/infiniti_scroll_2/')

    scroll_element = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')

    while True:
        try:
            ActionChains(browser).move_to_element(scroll_element).scroll_by_amount(0, 600).perform()

            last_element = browser.find_element(By.CLASS_NAME, 'last-of-list')

        except NoSuchElementException:
            continue

        if last_element:
            break

    numbers = browser.find_elements(By.TAG_NAME, 'p')

    answer = 0

    for num in numbers:
        text = num.text

        if text.isdigit():
            answer += int(text)

    print(answer)

    time.sleep(3)
