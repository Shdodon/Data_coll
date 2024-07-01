from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client["les_3_db"]
collect = db["books_lib"]

#поиск количесвта книг, певрая буква названия которых содержит "А"
def find():
    query = {"name" : {"$gte": "A", "$lt" : "B"}}

    projection = {"_id" : 0, "name":1}


    books = db.books_lib.find(query, projection)

    num_books = 0
    for i in books:
        print(i)
        num_books +=1

    print('Число книг: %d' % num_books)

    for a in books:
        print(a)

if __name__ == '__main__':
    find()


