# Выберите веб-сайт, который содержит информацию, представляющую интерес для извлечения данных. Это может быть новостной сайт,
# платформа для электронной коммерции или любой другой сайт, который позволяет осуществлять скрейпинг (убедитесь в соблюдении условий обслуживания сайта).
# Используя Selenium, напишите сценарий для автоматизации процесса перехода на нужную страницу сайта.
# Определите элементы HTML, содержащие информацию, которую вы хотите извлечь (например, заголовки статей, названия продуктов, цены и т.д.).
# Используйте BeautifulSoup для парсинга содержимого HTML и извлечения нужной информации из идентифицированных элементов.
# Обработайте любые ошибки или исключения, которые могут возникнуть в процессе скрейпинга.
# Протестируйте свой скрипт на различных сценариях, чтобы убедиться, что он точно извлекает нужные данные.
# Предоставьте ваш Python-скрипт вместе с кратким отчетом (не более 1 страницы), который включает следующее:
# URL сайта. Укажите URL сайта, который вы выбрали для анализа. Описание.
# Предоставьте краткое описание информации, которую вы хотели извлечь из сайта.
# Подход. Объясните подход, который вы использовали для навигации по сайту, определения соответствующих элементов и извлечения нужных данных.
# Трудности. Опишите все проблемы и препятствия, с которыми вы столкнулись в ходе реализации проекта, и как вы их преодолели. Результаты.
# Включите образец извлеченных данных в выбранном вами структурированном формате (например, CSV или JSON).
# Примечание: Обязательно соблюдайте условия обслуживания сайта и избегайте чрезмерного скрейпинга, который может нарушить нормальную работу сайта.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup
import re
import csv
from selenium.common.exceptions import NoSuchElementException

TARGET_URL = 'https://www.litres.ru/'
SEARCH_STR = 'Жуков'
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"


def book_data(book_url):
    data = {'Author': None,
            'Name': None,
            'Price': None,
            'Rating': None,
            'Url': book_url,
            }
    response = requests.get(book_url, headers={'User-Agent': user_agent})
    page = BeautifulSoup(response.text, 'html.parser')
    try:
        data['Name'] = page.find(class_='ArtInfo_title__h_5Ay').text
    except ValueError:
        pass
    except AttributeError:
        pass
    try:
        data['Price'] = float(re.findall(r'\b\d+(?:.\d+)?',
                                         page.find(class_='ArtPriceFooter_ArtPriceFooterPrices__final__7AMj').text)[0])
    except ValueError:
        pass
    except AttributeError:
        pass
    try:
        data['Rating'] = float(re.findall(r'\b\d+(?:.\d+)?',
                                          page.find(class_='ArtRating_rating__ntve8').text
                                          .replace(',', '.'))[0])
    except ValueError:
        pass
    except AttributeError:
        pass
    try:
        data['Author'] = "; ".join([author.text for author in  # Если вдруг авторов несколько
                                    page.find(class_='ArtInfo_author__0W3GJ').find_all('div')])
    except ValueError:
        pass
    except AttributeError:
        pass
    return data

# csv
def my_save_to_csv(filename, local_data):

    with open(filename, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Author', 'Name', 'Price', 'Rating', 'Url'])
        for row in local_data:
            writer.writerow(row.values())

if __name__ == '__main__':

    print('Start')
    options = Options()
    options.add_argument(f'user-agent={user_agent}')
    # Запускаем браузер
    driver = webdriver.Chrome(options=options)
    driver.get(TARGET_URL)
    # Задаем поиск
    search_box = driver.find_element(By.CLASS_NAME, 'SearchForm_input__qDTKP')
    search_box.send_keys(SEARCH_STR)
    search_box.submit()

    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'body')))

    scroll_pause_time = 2
    last_height = driver.execute_script('return document.documentElement.scrollHeight')

    while True:
        driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight - 10);')
        time.sleep(scroll_pause_time)

        new_height = driver.execute_script('return document.documentElement.scrollHeight')
        if new_height == last_height:
            try:
                continue_button = driver.find_element(By.XPATH, "//li[@class='Paginator_arrow__SAzJS']/a/button[@class='Button_button__vpqEH Button_button_medium__m3Snt Button_button_tertiary__aotaW Paginator_button__8qU9e']" )
            except NoSuchElementException:
                continue_button = None
            if continue_button:
                continue_button.click()
            else:
                break
        last_height = new_height

    books_links = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(By.XPATH, '//a[@data-testid="art__title"]'))
    print(f'Finded {len(books_links)} links')
    result = [book_data(url.get_attribute('href')) for url in tqdm(books_links, '')]
    my_save_to_csv('litres.csv', result)
    driver.quit()
    print('Success')



