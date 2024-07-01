import json
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client["les_3_db"]
collect = db["books_lib"]

with open('book_j.json', 'r', encoding='utf-8') as file:
    try:
        data = json.load(file)
    except Exception as e:
            print(f"Error: {e}")

collect.insert_many(data)

print('Data_load')

data[0]

client.close()