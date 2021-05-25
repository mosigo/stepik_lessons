from selenium import webdriver


link = "http://suninjuly.github.io/cats.html"
browser = webdriver.Chrome()

try:
    browser.implicitly_wait(5)
    browser.get(link)

    button = browser.find_element_by_id("button")

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
