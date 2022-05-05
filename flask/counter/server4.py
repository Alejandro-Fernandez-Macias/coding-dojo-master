from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'counter key'


# Have the root route render a template that displays the number of times the client has visited this site. Refresh the page several times to ensure the counter is working.
@app.route('/')
def counter():
    if "counter" not in session:
        session["counter"] = 1
    return render_template('counter.html')

@app.route('/add')
def add():
    session["counter"] += 1
    return redirect("/")

# NINJA BONUS: Add a +2 button underneath the counter and a new route that will increment the counter by 2
@app.route('/add2')
def add2():
    session["counter"] += 2
    return redirect("/")

# Add a "/destroy_session" route that clears the session and redirects to the root route. Test it.
@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)