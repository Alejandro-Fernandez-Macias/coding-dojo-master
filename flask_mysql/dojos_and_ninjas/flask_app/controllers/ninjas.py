from flask_app import app

from flask import render_template, redirect, request

from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninja')
def ninja():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('ninja.html', dojos=dojos)

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    Ninja.save(request.form)
    return redirect('/')