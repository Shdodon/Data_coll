from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.imdb.com/chart/top")

movie_titel_elements = driver.find_elements(By.CSS_SELECTOR, "a.ipc-title-link-wrapper")

rating_elements = driver.find_elements(By.XPATH, "//span/div/span/text()")


# метод text извлекает
# информацию из элементов и сохраняет ее в списках названий и оценок.
#это генератор списка в Python, который создает новый список titles, содержащий текст каждого
# элемента в списке movie_title_elements.
# Генератор списка — это лаконичный способ написать цикл for, который создает
# новый список. В этом случае генератор списка выполняет итерации по каждому
# элементу в movie_title_elements и извлекает текст из каждого элемента с помощью
# метода text. Полученный текст затем добавляется в список титров.
titles = [element.text for element in movie_titel_elements]
ratings = [element.text for element in rating_elements]

# Эквивалентный код с использованием цикла for
# titles = []
# for element in movie_title_elements:
# title = element.text
# titles.append(title)


for i in range(10):
    print("Rating {}: {} ({})".format(i+1), titles[i], ratings[i])

driver.quit()