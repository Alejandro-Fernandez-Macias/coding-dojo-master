from flask_app import app
from flask import render_template, redirect, request, flash, session
from ..models.dojo import Dojo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def submit_form():
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    data = {
        'name' : request.form['name'],
        'location' : request.form['location'],
        'language' : request.form['language'],
        'comment' : request.form['comment']
    }
    Dojo.save(data)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/results')

@app.route('/results')
def results():
    print("Showing the User Info from the Form")
    print(request.form)
    return render_template('results.html', name_on_temp=session['name'], location_on_temp=session['location'], language_on_temp=session['language'], comment_on_temp=session['comment'])