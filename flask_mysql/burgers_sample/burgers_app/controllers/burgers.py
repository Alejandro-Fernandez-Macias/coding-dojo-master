from burgers_app import app

from flask import render_template, redirect, request

from burgers_app.models.burger import Burger

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create/burger', methods=['POST'])
def burger():
    Burger.save(request.form)
    return redirect('/')