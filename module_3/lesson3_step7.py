import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    x_element = browser.find_element_by_id('treasure')
    x = int(x_element.get_attribute('valuex'))
    y = calc(x)

    print('y=', y)

    answer_elem = browser.find_element_by_id('answer')
    answer_elem.send_keys(str(y))

    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_tag_name('button').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
