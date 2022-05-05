from flask import Flask, render_template, session, redirect, request
import random

app=Flask(__name__)
app.secret_key='number game'

@app.route('/')
def index():
    if "number" not in session:
        session['number']= random.randint(1,100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    if 'guess' in session:
        print(session['guess'])
        print(session['number'])
    return redirect('/')

@app.route('/play_again')
def play_again():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)