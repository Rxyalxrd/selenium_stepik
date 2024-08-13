import time
from selenium import webdriver

with webdriver.Chrome() as browser:
    """
    Кодовое имя: "Секретные печеньки"

    Представьте себя хакером-белой шляпы, вооруженным навыками веб-скрапинга и автоматизации.
    Ваша миссия, если вы её примете, — раскрывать секреты веб-сайтов, чтобы обеспечить их
    безопасность и устойчивость. Не просто кодером, вы — кибердетектив. 
    И вот ваше следующее задание:

    Цель: Получить все секретные "cookies" с заданного веб-сайта и суммировать их числовые 
    значения. Эти "cookies" могут хранить важную информацию, например, ключи для доступа к 
    секретным данным. Ваши навыки веб-парсинга здесь будут более чем полезны.
    """

    browser.get('https://parsinger.ru/methods/3/index.html')

    time.sleep(0.2)

    all_cookies = browser.get_cookies()

    secrets_cookies = [
        cookie for cookie in all_cookies if 'secret_cookie_' in cookie.get('name')
    ]

    answer = 0

    for secrets_value in secrets_cookies:
        if secrets_value.get('value') is not None:
            answer += int(secrets_value.get('value'))

    print(answer)
    time.sleep(3)
