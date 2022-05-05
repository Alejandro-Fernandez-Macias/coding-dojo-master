from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "dojo survey"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    print("Showing the User Info from the Form")
    print(request.form)
    return render_template("result.html", name_on_temp=session['name'], location_on_temp=session['location'], language_on_temp=session['language'], comment_on_temp=session['comment'])

if __name__ == "__main__":
    app.run(debug=True)