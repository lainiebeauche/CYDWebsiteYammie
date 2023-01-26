from flask import Flask, render_template, request, redirect, url_for
from database import delete_all_messages, get_all_messages, add_message

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('Final_Ank.html')

@app.route('/info')
def info():
    return render_template('Ank_info.html')

@app.route('/comment', methods=['GET', 'POST', 'DELETE'])
def comment():
    if request.method == "POST":
        text = request.form['text']
        username = request.form['username']
        add_message(username, text)
    elif: request.method == "DELETE"
        delete_all_messages()
    return render_template('Ank_comm.html', messages=get_all_messages())

if __name__ == '__main__':
    delete_all_messages()
    app.run(debug=True)
