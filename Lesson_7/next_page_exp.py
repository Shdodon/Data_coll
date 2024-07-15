from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.example.com/movies")

next_button_locator = (By.XPATH, '//a[@class]="next"')

current_page = 1

while True:
    print (f"Scraping page {current_page}...")

    try:
        next_button = driver.find_element(*next_button_locator)
        next_button.click()
        current_page +=1
    except NoSuchElementException:
        break

driver.quit()


# В примере сценарий переходит на сайт, содержащий несколько страниц, а затем
# использует цикл while для нажатия кнопки Next и скрейпинга данных на каждой
# странице.
# 10
# next_button_locator определяется с помощью кортежа, который указывает метод By
# (в данном случае By.XPATH) и значение локатора (в данном случае выражение
# XPath //a[@class="next"]).
# Блок try-except пытается найти кнопку Next и нажать на нее. Если кнопка Next не
# найдена, значит, мы достигли последней страницы — сценарий выйдет из цикла.
