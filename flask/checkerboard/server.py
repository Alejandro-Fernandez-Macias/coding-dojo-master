# 1. Have the /play route render a template with 3 blue boxes
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', row=8, col=8, color_1='red', color_2='black')

@app.route('/<int:i>')
def row(i):
    return render_template('index.html', row=i, col=8, color_1='red', color_2='black')

@app.route('/<int:i>/<int:j>')
def row_col(i, j):
    return render_template('index.html', row=i, col=j, color_1='red', color_2='black')

@app.route('/<int:i>/<int:j>/<string:first>')
def row_col_1(i, j, first):
    return render_template('index.html', row=i, col=j, color_1=first, color_2='black')


@app.route('/<int:i>/<int:j>/<string:first>/<string:second>')
def row_col_2(i, j, first, second):
    return render_template('index.html', row=i, col=j, color_1=first, color_2=second)

if __name__ =="__main__":
    app.run(debug=True)