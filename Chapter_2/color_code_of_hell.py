import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    """
    Квест "Ад Цветовых Шифров"
    
    Приветствую, фанаты автоматизации и парсинга! Сегодня у нас не просто 
    задание, а настоящий квест. Перед вами полотно веб-страницы, и ваша 
    задача — расшифровать его, как настоящие криптографы цветов. Используя 
    Selenium, вам нужно будет пройти через лабиринт элементов, собрать все 
    цветовые коды и применить их для различных задач на странице.
    """

    browser.get('https://parsinger.ru/selenium/5.5/5/1.html')

    all_div_style_blocks = browser.find_elements(By.XPATH, '//div[@style]')
    all_div_style_blocks = all_div_style_blocks[1::]

    for div_block in all_div_style_blocks:
        hex_color = div_block.find_element(By.XPATH, './/span').text

        select_color = div_block.find_element(
            By.XPATH, f'.//option[text()="{hex_color}"]'
        )
        select_color.click()

        color = div_block.find_element(
            By.XPATH, f'.//button[@data-hex="{hex_color}"]'
        )
        color.click()

        checkbox = div_block.find_element(
            By.XPATH, './/input[@type="checkbox"]'
        )
        checkbox.click()

        input_field = div_block.find_element(
            By.XPATH, './/input[@type="text"]'
        )
        input_field.send_keys(hex_color)

        submit = div_block.find_element(
            By.XPATH, '//button[text()="Проверить"]'
        )
        submit.click()

    submit_out_divs = browser.find_element(
        By.XPATH, '//button[text()="Проверить все элементы"]'
    )
    submit_out_divs.click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

    time.sleep(5)
