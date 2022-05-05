from flask_app import app

from flask import render_template, redirect, request

from flask_app.models.user import User

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template('index.html', users = users)

@app.route('/add_user')
def add_user():
    return render_template("add_user.html")

@app.route('/create_user', methods=['POST'])
def create_user():
    User.save(request.form)
    return redirect('/')

@app.route("/delete/<int:user_id>/user")
def destroy(user_id):
    data = {
        "id" : user_id
    }
    User.destroy(data)
    return redirect('/')

@app.route('/show/<int:user_id>/user')
def show(user_id):
    user = User.get_one(user_id)
    return render_template('show.html', user=user)

@app.route('/edit/<int:user_id>/user', methods=['GET'])
def edit(user_id):
    user= User.get_one(user_id)

    return render_template('edit.html', user = user)

@app.route('/update/<int:user_id>/user', methods=['POST'])
def update(user_id):
    User.update(request.form, user_id)
    return redirect('/')