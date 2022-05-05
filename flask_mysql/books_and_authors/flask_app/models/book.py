from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import author


class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors_who_favorited = []

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO books ( title, num_of_pages ) VALUES ( %(title)s, %(num_of_pages)s);"
        result =connectToMySQL('books_schema').query_db(query,data)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_schema').query_db(query)
        books = []
        for b in results:
            books.append(cls(b))
        return books

    @classmethod
    def get_book(cls, id):
        query = "SELECT * FROM books WHERE id = %(id)s;"
        result = connectToMySQL('books_schema').query_db(query, {"id" : id})
        return cls(result[0])

    @classmethod
    def get_specified_book(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON authors.id = favorites.author_id WHERE books.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db(query, data)
        book = cls(results[0])
        for row in results:
            if row['authors.id'] == None:
                break
            data = {
                'id' : row['authors.id'],
                'name' : row['name'],
                'created_at' : row['authors.created_at'],
                'updated_at' : row['authors.updated_at']
            }
            book.authors_who_favorited.append(author.Author(data))
        return book

    @classmethod
    def unfavorited_books(cls, data):
        query = " SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM favorites WHERE author_id = %(id)s);"
        books = []
        results = connectToMySQL('books_schema').query_db(query, data)
        for row in results:
            books.append(cls(row))
        return books

    @classmethod
    def add_to_favorites(cls, data):
            query = "INSERT INTO favorites ( author_id, book_id ) VALUES (%(author_id)s ,%(book_id)s;)"
            result = connectToMySQL('books_schema').query_db(query, data)
            print(result)
            return result