import email
from flask_app import app
from flask import render_template, request, redirect, flash
from ..models.email import Email

@app.route('/')
def index():
    return render_template(['index.html'])

@app.route('/process', methods=['POST'])
def create_email():
    if not Email.validate_email(request.form):
        return redirect('/')
    data = {
        'email' : request.form['email']
    }
    Email.save(data)
    return redirect('/success')

@app.route('/success')
def results():
    print("Showing all emails submitted")
    email = Email.get_all()
    return render_template('results.html', emails = email)

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id': id
    }
    Email.destroy(data)
    return redirect('/success')
