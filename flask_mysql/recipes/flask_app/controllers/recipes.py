from flask_app import app
from flask import render_template, redirect, session, request, flash
from..models.user import User
from..models.recipe import Recipe

@app.route('/create')
def create_form():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id' : session['user_id']
    }
    user = User.get_one(data)
    return render_template('create.html', user = user)

@app.route('/recipe/new', methods = ["POST"])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect('/create')
    data = {
        'name' : request.form['name'],
        'under30' : int(request.form['under30']),
        'description' : request.form['description'],
        'instructions' : request.form['instructions'],
        'date_made' : request.form['date_made'],
        'user_id' : session['user_id']
    }
    Recipe.save(data)
    return redirect('/dashboard')

@app.route('/recipe/<int:recipe_id>')
def get_one(recipe_id):
    data = {
        'id' : recipe_id
    }
    recipe = Recipe.get_one(data)
    return redirect('/dashboard', recipe = recipe)

@app.route('/recipe/<int:recipe_id>/delete')
def delete(recipe_id):
    data = {
        'id' : recipe_id
    }
    Recipe.destroy(data)
    return redirect('/dashboard')

@app.route('/recipe/update', methods = ['POST'])
def update():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect('/create')
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'under30': int(request.form['under30']),
        'date_made': request.form['date_made'],
        'id': request.form['id'],
    }
    Recipe.update(data)
    return redirect('/dashboard')

@app.route('/recipe/edit/<int:id>')
def edit_form(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id' : id
    }
    user_data = {
        "id" : session['user_id']
    }
    recipe = Recipe.get_one(data)
    user = User.get_one(user_data)
    return render_template('edit.html', recipe = recipe, user = user)

@app.route('/recipe/view/<int:id>')
def view(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id' : id
    }
    user_data = {
        'id': session['user_id']
    }
    recipe = Recipe.get_one(data)
    user = User.get_one(user_data)
    return render_template('view_recipe.html', recipe = recipe, user = user)


@app.route('/recipe/delete/<int:id>')
def destroy_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id' : id
    }
    Recipe.destroy(data)
    return redirect('/dashboard')
