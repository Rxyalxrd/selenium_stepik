import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_3/')

    scroll_elements = browser.find_elements(By.XPATH, '//*[contains(@id, "scroll-container")]')

    for scroll_element in scroll_elements:
        last_height = browser.execute_script("return arguments[0].scrollHeight", scroll_element)

        while True:
            browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_element)
            time.sleep(0.2)

            new_height = browser.execute_script("return arguments[0].scrollHeight", scroll_element)

            if new_height == last_height:
                break
            last_height = new_height

    span_tags = browser.find_elements(By.TAG_NAME, 'span')
    answer = 0

    for num in span_tags:
        text = num.text
        if text.isdigit():
            answer += int(text)

    print(f"Сумма всех чисел на странице: {answer}")
    time.sleep(3)
