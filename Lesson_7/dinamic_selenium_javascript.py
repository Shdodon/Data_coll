# Пример того, как выполнить JavaScript в Selenium:

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.example.com")
# Выполнение JavaScript для взаимодействия со страницей
result = driver.execute_script("return document.title")
print(result)
driver.quit()
#
# В примере мы создаем экземпляр webdriver, переходим на сайт, а затем выполняем
# код JavaScript "return document.title", который возвращает значение заголовка
# страницы. Результат выполнения сохраняется в переменной result, которую мы
# можем использовать по мере необходимости.

# Другой мощный инструмент — ожидание загрузки элементов на странице. Он
# полезен для извлечения данных со страниц, которые требуют времени для
# загрузки.
# Некоторые элементы могут загружаться дольше, чем другие, и нам нужно
# дождаться их полной загрузки, прежде чем пытаться извлечь из них данные. Для
# ожидания загрузки элементов мы можем использовать класс WebDriverWait в
# Selenium, который позволяет дождаться наступления определенного условия,
# прежде чем приступить к работе.
# Пример Python-кода, который позволяет дождаться загрузки элемента:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/page/1/")
16
# ожидание загрузки элемента
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
".quote")))
# извлечение данных из элемента
quote = element.text
driver.quit()

# В примере мы сначала инициализируем веб-драйвер Chrome и переходим на
# нужный URL. Затем создаем экземпляр класса WebDriverWait и указываем
# максимальное время ожидания — 10 секунд. Метод until используется для
# ожидания, пока нужный элемент не появится на странице. В этом случае мы ищем
# элемент с CSS-классом quote. Когда элемент присутствует, мы извлекаем текст из
# элемента и сохраняем его в переменной. Наконец, мы закрываем драйвер.

# Взаимодействие с динамическими элементами (выпадающим меню или
# модальными окнами) с помощью Selenium может быть непростым. Эти элементы
# часто изменяют структуру страницы и требуют дополнительного взаимодействия с
# пользователем, чтобы стать видимыми.
# # Пример Python-кода для взаимодействия с выпадающим меню с помощью
# Selenium:
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get("https://www.example.com/dropdown-menu")
# Найдите выпадающее меню и выберите нужную опцию
dropdown = driver.find_element(By.ID, "dropdown-menu")
select = Select(dropdown)
select.select_by_visible_text("Option 2")
driver.quit()
# В коде мы сначала переходим на целевой сайт, содержащий выпадающее меню.
# Затем используем метод find_element, чтобы найти выпадающее меню на странице.
# Далее создаем элемент Select.
# Объект Select в коде — это объект Selenium, который позволяет взаимодействовать
# с выпадающими меню на веб-странице. Объект Select предоставляет методы для
# выбора опций из выпадающего меню и для проверки выбранной опции. Объект
# Select инициализирует WebElement, представляющий выпадающее меню, и
# предоставляет такие методы, как select_by_index, select_by_value и
# select_by_visible_text для выбора опций из выпадающего меню.
# Это позволяет нам взаимодействовать с выпадающим меню, как если бы оно было
# обычным элементом HTML <select>. Наконец, мы используем метод
# select_by_visible_text для выбора нужной опции