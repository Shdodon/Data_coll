import requests
from lxml import html
from pymongo import MongoClient
import time

def scrape_page_data(url):
    response = requests.get(url)
    tree = html.fromstring(response.content)

    table_rows = tree.xpath("//table[@class='records-table']/tbody/tr")

    data = []

    for row in table_rows:
        columns = row.xpath(".//td/text()")

        data.append({
            'rank': columns[0].strip(),
            'mark': columns[1].strip(),
            'competitor': row.xpath(".//td[4]/a/text()")[0].strip(),
            'dob': columns[4].strip(),
            'nat': columns[6].strip(),
            'pos': columns[7].strip(),
            'venue': columns[8].strip(),
            'date': columns[9].strip(),
            'resultscore': columns[10].strip()


            })

    return data



def save_data_to_mongo(data):
    client = MongoClient("localhost", 27017)
    db = client['world_athletics']
    collection = db['sprints_60_metres']
    collection.insert_many(data)


def main():
    base_url = 'https://www.worldathletics.org/records/toplists/sprints/60-metres/indoor/women/senior/2023?page='
    for page in range(1, 5):
        print(f"Scraping page {page}...")
        url = base_url + str(page) # формируем полный URL для доступа к странице
        data = scrape_page_data(url) # извлекаем данные из страницы
        save_data_to_mongo(data)
        time.sleep(1)

if __name__ == "__main__":
    main()