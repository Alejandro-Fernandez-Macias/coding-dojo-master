from flask_app import app

from flask import render_template, redirect, request

from ..models.author import Author
from ..models.book import Book


@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def authors():
    authors = Author.get_all()
    print(authors)
    return render_template('index.html', all_authors=authors)


@app.route('/create/author', methods=['POST'])
def create_author():
    Author.save(request.form)
    return redirect('/')

@app.route('/author/<int:id>')
def view_author(id):
    data = {
        'id' : id
    }
    return render_template('show_author.html', author=Author.get_specified_author(data), unfavorited_books=Book.unfavorited_books(data))

@app.route('/join/book', methods=['POST'])
def join_book():
    data = {
        'author_id' : request.form['author_id'],
        'book_id' : request.form['book_id']
    }
    Book.add_to_favorites(data)
    return redirect(f"/author/{request.form['author_id']}")