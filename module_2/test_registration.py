from selenium import webdriver
from sys import argv
import time

script_name, link = argv

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector("div.first_block input.first")
    second_name = browser.find_element_by_css_selector("div.first_block input.second")
    email = browser.find_element_by_css_selector("div.first_block input.third")
    for input in [first_name, second_name, email]:
        input.send_keys("Qqq qqq qqq")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы (закомментировала этот sleep тоже, так как в критериях
    # написано, что убрать нужно вообще все sleep-ы из программы
    # time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()