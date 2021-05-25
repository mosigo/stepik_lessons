import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)
    y = calc(x)

    print('y=', y)

    answer_elem = browser.find_element_by_id('answer')
    answer_elem.send_keys(str(y))

    browser.find_element_by_id('robotCheckbox').click()
    robots_rule = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robots_rule)
    robots_rule.click()

    button = browser.find_element_by_tag_name('button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()