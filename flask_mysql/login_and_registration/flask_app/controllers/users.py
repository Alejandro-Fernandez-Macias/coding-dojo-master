from flask_app import app
from flask import render_template, redirect, request, session, flash
from..models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : pw_hash
    }
    user_id = User.save(data)
    user_in_db=User.get_by_email(data)
    session['user_id'] = user_id
    session['first_name'] = user_in_db.first_name
    session['last_name'] = user_in_db.last_name
    session['email'] = user_in_db.email
    return redirect('/success')

@app.route('/success/user')
def success():
    return render_template('success.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect ('/')

@app.route('/login/user', methods=['POST'])
def login():
    data = {
        'email' : request.form['email'],
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash('Invalid Email/Password')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Emal/Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name
    session['last_name'] = user_in_db.last_name
    session['email'] = user_in_db.email
    return redirect('/success/user')
