import time
from selenium import webdriver

with webdriver.Chrome() as browser:
    """
    Кодовое имя: Следопыт Чётных Печеньек.
    
    Вы — киберархеолог. Ваша миссия — раскопать древние и загадочные "печеньки" (cookies) 
    на таинственном веб-сайте. Но не просто так. Ваша задача собрать только особые 
    печеньки — те, что имеют чётные числа после символа "_". Суммируйте числовые значения 
    этих "печенек" и используйте их как ключ к следующему уровню этого цифрового лабиринта.
    
    Пример cookie:

    cookie = {
        'domain': 'parsinger.ru',
        'httpOnly': False,
        'name': 'secret_cookie_15',
        'path': '/methods/3',
        'sameSite': 'Lax',
        'secure': False, 
        'value': '27300'
    }
    """

    browser.get('https://parsinger.ru/methods/3/index.html')
    all_cookies = browser.get_cookies()

    values = 0

    for cookie in all_cookies:
        if int(cookie['name'].split('_')[-1]) % 2 == 0:
            values += int(cookie['value'])

    print(values)

    time.sleep(3)
