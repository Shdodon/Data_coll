# Выполнить скрейпинг данных в веб-сайта http://books.toscrape.com/ и извлечь информацию
# о всех книгах на сайте во всех категориях: название, цену,
# количество товара в наличии (In stock (19 available)) в формате integer, описание.

# Затем сохранить эту информацию в JSON-файле.


import requests
from bs4 import BeautifulSoup
from pprint import pprint
import re
import json

headers = {
    "headers": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}
session = requests.session()

all_books = []
url = "http://books.toscrape.com/"
url_add = ""
end_page = True
while end_page:
    try:
        url_new = url + url_add
        response = session.get(url_new, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        try:
            url_add = soup.find('li', {'class': 'next'}).findChildren()[0].get('href')
            if 'catalogue' not in url_add:
                url_add = 'catalogue/' + url_add
        except:
            end_page = False
        books = soup.find_all('li', {'class': 'col-xs-6'})

        for book in books:
            book_info = {}
            name_info = book.find('h3').findChildren()[0]
            book_info['name'] = name_info.get('title')
            href = name_info.get('href')
            if 'catalogue' in href:
                book_info['url'] = url + href
            else:
                book_info['url'] = url + 'catalogue/' + href

            price_info = book.find('div', {'class': 'product_price'}).findChildren()[0].getText()[1:]
            book_info['price'] = [float(price_info[1:]),
                                  price_info[0]]

            response = session.get(book_info['url'], headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            avail_info = soup.find('p', {'class': 'instock availability'}).getText()
            book_info['avail'] = [int(re.findall('\d+', avail_info)[0]),
                                  re.sub("^\s+|\n|\r|\s+$", '', avail_info)]

            all_books.append(book_info)

            print(book_info['name'])
        if end_page:
            print(f"\nСтраница {url_add}")
    except:

        print()
        break

with open('book_j.json', 'w') as f:
    json.dump(all_books, f)