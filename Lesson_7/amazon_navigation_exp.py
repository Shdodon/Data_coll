from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://amazon.com") # Переходим на страницу Amazon

search_box = driver.find_element(By.ID, 'twotabsearchtextbox') # Находим на странице поле поиска
search_box.send_keys("laptops") # Вводим в поле поиска поисковой запрос "laptops"
search_box.submit() # Запускаем поиск с помощью метода submit для элемента окна поиска

assert  "laptops" in driver.title #Проверяем, что страница с результатами поиска загрузилась,
#Проверяя появление слова laptops в заголовке страницы