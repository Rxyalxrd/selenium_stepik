import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_1/')

    scroll_element = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
    total_sum = 0

    while True:
        last_element = browser.find_elements(By.CLASS_NAME, 'last-of-list')

        if last_element:
            break

        ActionChains(browser).move_to_element(scroll_element).scroll_by_amount(0, 600).perform()
        time.sleep(1)

    elements = browser.find_elements(By.TAG_NAME, 'span')

    for element in elements:

        text = element.text
        if text.isdigit():
            total_sum += int(text)

    print('Сумма всех чисел:', total_sum)
