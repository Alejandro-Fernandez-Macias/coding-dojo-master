from flask_app import app
from flask import render_template, redirect, request, session, flash
from..models.user import User
from..models.message import Message

@app.route('/wall/user')
def show_messages():
    messages = Message.get_all_with_users()
    print(messages)
    return render_template('wall.html', messages=messages)

@app.route('/create_message', methods=['POST'])
def create_message():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'sender_id' : request.form['sender_id'],
        'receiver_id' : request.form['receiver_id'],
        'content' : request.form['content']
    }
    Message.save_message(data)
    return redirect('/dashboard')

@app.route('/delete/message/<int:id>')
def destroy(id):
    data = {
        'id' : id
    }
    Message.destroy(data)
    return redirect('/dashboard')

