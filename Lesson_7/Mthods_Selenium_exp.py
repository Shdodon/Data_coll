# 1. Метод click - для перехода к опеределенному URL. Пример кода для перехода на домашнюю старницу Google
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.google.com")

# 2. Методы back и forward - для навигации назад и вперед в истории браузера. Например, если вы перешли на несколько страниц,
# вы можете вернуться на предыдущую:
driver.back()

# 3. Метод refresh - для обновления текущей старницы. Пример:
driver.refresh()

# 4. Атрибут title - возвращает заголовок текущей страницы. Пример:
print(driver.title)

# 5. Атрибут current_url - возвращает URL текущей старницы. Например:
print(driver.current_url)


# Метод text поможет извлечь текстовое содержимое. Пример: Если есть элемент div с тексотм "Hello world", его можно извлечь

# Метод get_attribute поможет получить значение определенного атрибута элемента.

# Для примера рассмотрим HTML-код:
# <html>
#     <body>
#         <div id="my-div">Hello World!!!v</div>
#         <input type="text" name="username" value="johndoe">
#     </body>
# </html>

# Можно извлечь текст из элемента div и значение поля ввода «имя пользователя» с
# помощью кода:
# driver = webdriver.Chrome()
# driver.get("https://www.example.com")
# div_element = driver.find_element(By.ID, "my-div")
# print(div_element.text)
# username_element = driver.find_element(By.NAME, "username")
# print(username_element.get_attribute("value"))
#
#
#
#
#