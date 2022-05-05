from flask_app import app

from flask import render_template, redirect, request

from flask_app.models.book import Book
from flask_app.models.author import Author

@app.route('/books')
def all_books():
    books = Book.get_all()
    print(books)
    return render_template('books.html', all_books=books)

@app.route('/create/book', methods=['POST'])
def add_book():
    Book.save(request.form)
    return redirect('/books')

@app.route('/book/<int:id>')
def view_book(id):
    data = {
        'id' : id
    }
    return render_template('show_book.html', book=Book.get_specified_book(data), unfavorited_authors=Author.unfavorited_authors(data))

@app.route('/join/author', methods=['POST'])
def join_author():
    data = {
        'author_id' : request.form['author_id'],
        'book_id' : request.form['book_id']
    }
    Author.add_to_favorites(data)
    return redirect(f"/book/{request.form['book_id']}")