import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    browser.find_element_by_tag_name('button').click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)
    y = calc(x)

    answer_elem = browser.find_element_by_id('answer')
    answer_elem.send_keys(str(y))

    button = browser.find_element_by_tag_name('button')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
