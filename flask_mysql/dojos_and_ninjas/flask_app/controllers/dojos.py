from flask_app import app

from flask import render_template, redirect, request

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('index.html', all_dojos=dojos)

@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/')

@app.route('/dojo/<int:id>')
def  show_dojo(id):
    data = {
        'id' : id
    }
    return render_template('dojo_show.html', dojo = Dojo.get_dojo_with_ninjas(data))