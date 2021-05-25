from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_xpath("//input[@name='firstname']")
    second_name = browser.find_element_by_xpath("//input[@name='lastname']")
    email = browser.find_element_by_xpath("//input[@name='email']")
    for input in [first_name, second_name, email]:
        input.send_keys("Qqq qqq qqq")

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'dummy.txt')
    browser.find_element_by_id('file').send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()