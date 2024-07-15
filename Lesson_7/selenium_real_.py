import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()

browser.get("http://quotes.toscrape.com/page/1/")

# Инициализация пустого списка для хранения цитат
quotes = []

while True:
    #
    quote_elements = browser.find_elements(By.XPATH, '//div[@class="quote"]')
    #
    for quote_element in quote_elements:
        quote = quote_element.find_element(By.XPATH, './/span[@class="text"]').text
        author = quote_element.find_element(By.XPATH,
                                            './/span/small[@class="author"]').text
        quotes.append({"quote": quote, "author": author})

        next_button = browser.find_elements(By.XPATH, '//li[@class="next"]/a')
        if not next_button:
            break

        next_button[0].click()

        time.sleep(1)

driver.close()

with open("quotes.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["quote", "author"])
    writer.writeheader()
    writer.writerows(quotes)

# for quote in quotes:
#     print(quote["quote"], "by", quote["author"])
