import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from constants.const_for_junior_vortuoso import COOKIES

with webdriver.Chrome() as browser:
    """
    Кодовое имя: Операция "Младший Виртуоз".

    Информация, которая вам доступна, позволяет нам сделать вывод: вам необходимо найти
    и завербовать младшего и наиболее перспективного хакера из противоборствующей группы.
    Этот человек уникален — он знает больше всего языков программирования среди своих
    соратников. После того, как вы его обнаружите, вам нужно извлечь "value" из его
    cookie и вставить это значение в поле для ответов на степик.
    """

    browser.get('https://parsinger.ru/selenium/5.6/1/index.html')

    result = None
    val_age = 2881337
    val_skills_list = -2281337

    for cookie in COOKIES:

        browser.delete_all_cookies()
        browser.add_cookie(cookie)
        browser.refresh()
        time.sleep(0.3)

        try:
            age = int(browser.find_element(By.ID, 'age').text.split(':')[-1])
            skills_list = browser.find_element(By.ID, 'skillsList').text.split()
        except:
            pass

        if '(ASM)' in skills_list:
            skills_list.remove('(ASM)')

        len_skills_list = len(skills_list)

        if age <= val_age and len_skills_list > val_skills_list:
            val_age = age
            val_skills_list = len_skills_list
            result = cookie.get('value')

    print(result)
    time.sleep(3)
