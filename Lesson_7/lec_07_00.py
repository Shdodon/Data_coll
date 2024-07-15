from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By # используется для определения местоположения элементов в документе

driver = webdriver.Chrome() #
driver.get("www.example.com") #осуществляет переход на страницу заданну в url. Будет ждать полную загрузку старницы
#прежде чем вернуть управление заданному сценарию


product = driver.find_element(By.XPATH, "//") # для поиска элемента на странице, для поиска нескольких элементов find_elements
product.click() #метод click используется для перехода по странице
# Класс By нужен, чтобы указать, какой атрибут используется для расположения элементов на странице.


add_to_cart = driver.find_element(By.XPATH, "//button[text()='Добавить в корзину']")
add_to_cart.click()

cart_items = driver.find_elements(By.XPATH, "//td[@class='cart-item-name']")
assert len(cart_items) == 1, "В корзине должен быть только один товар"
assert cart_items[0].text == "Рубашка", "В корзину добавлен не правильный товар"

driver.quit()