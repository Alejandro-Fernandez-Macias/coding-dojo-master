from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)
app.secret_key='ninja gold'

def datetime_activity(process, gold, area):
    time = datetime.datetime.now()
    return '%s %d gold from the %s! (%s)' % (process, gold, area, time)

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        print(session['gold'])
    if 'activity' not in session:
        session['activity'] = []
        print(session['activity'])
    return render_template("index.html", gold=session['gold'], activity=session['activity'])

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form.get('process') == 'at_farm':
        gold_earned = random.randint(10,20)
        session['gold'] += gold_earned
        session['activity'].insert(0, ['earned', datetime_activity('Earned', gold_earned, 'farm')],)
        print(session['gold'])

    elif request.form.get('process') == "at_cave":
        gold_earned = random.randint(5,10)
        session['gold'] += gold_earned
        session['activity'].insert(0, ['earned', datetime_activity('Earned', gold_earned, 'cave')],)
        print(session['gold'])

    elif request.form.get('process') == "at_house":
        gold_earned = random.randint(2,5)
        session['gold'] += gold_earned
        session['activity'].insert(0, ["earned", datetime_activity('Earned', gold_earned, 'house')],)
        print(session['gold'])

    elif request.form.get('process') == "at_casino":
        gold_earned = random.randint(-50,50)
        session['gold'] += gold_earned
        if gold_earned > 0:
            session['activity'].insert(0, ['earned', datetime_activity('Earned', gold_earned, 'casino')],)
        else:
            session['activity'].insert(0, ['earned', datetime_activity('lost', -gold_earned, 'casino')],)
        print(session['gold'])
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)