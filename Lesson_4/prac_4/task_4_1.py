# Задание 1
# Семинар 4. Парсинг HTML. XPath
# Напишите сценарий на языке Python, который выполняет
# следующие задачи:
# - отправляет HTTP GET-запрос на целевой URL и получает
# содержимое веб-страницы.
# - выполняет парсинг HTML-содержимого ответа с помощью
# библиотеки lxml.
# - используя выражения XPath, извлеките данные из первой
# строки таблицы.
# - выведите извлеченные данные из первой строки таблицы в
# консоль.


import requests
from lxml import html
import pandas as pd
import csv

url="https://worldathletics.org/records/toplists/sprints/60-metres/indoor/women/senior/2023?page=1"

resp = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'})

tree = html.fromstring(html = resp.content)

table_rows =tree.xpath("//table[@class='records-table']/tbody/tr")

data_list = []

for rows in table_rows:
    data = {}
    colums = rows.xpath(".//td/text()")
    data["rank"] = int(colums[0].strip())
    data["mark"] = float(colums[1].strip())
    data["WIND"] = colums[2].strip() if colums[2].strip() else "0"
    data["Competitor"] = rows.xpath(".//td/a/text()")[0].strip()
    data["DOB"] = colums[5].strip()
    data["Nat"] = colums[7].strip()
    data["Pos"] = colums[8].strip()
    data["Venue"] = colums[9].strip()
    data["Date"] = colums[10].strip()
    data["Results Score"] = float(colums[11].strip())

    data_list.append(data)

for data in data_list:
    print(data)

df = pd.DataFrame(data_list)
# print(df)
df.to_csv('data.csv', index=False)


# columns = table_rows[0].xpath(".//td/text()")
#
# for col in columns:
#     print(col)
#
# col_names = tree.xpath("//table[@class='records-table']/thead/tr/th/text()")
# for col_name in col_names:
#     print(col_name.strip())
