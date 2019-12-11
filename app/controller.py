# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session
import json
from model import User
from utils.hash_verification import Hash
from utils.token_session import Token

app = Flask(__name__)
app.secret_key = 'mysecretkey'
token = Token()
#resp = make_response(render_template('account.html', user = user))
# User definition #
#dbgroldanNick: 12345
#gabNick: prueba
with open('docs/user.json') as json_file:
    data_users = json.load(json_file)

# Routes Configuration #
@app.route('/')
def index():
    exist_token = request.cookies.get('token')
    if 'nickname' in session:
        if exist_token is not None:
            if token.verify_token(exist_token, data_users):
                user = token.getUser()
                return render_template('account.html', user = user)
    return render_template('index.html')

@app.route('/login_user', methods = ['POST'])
def login_user():
    if request.method == 'POST':
        nick = request.form['nick']
        passwd = request.form['pass']
        session['nickname'] = nick
        for user in data_users:
            if user["nick"] == nick and Hash.verify_two_hash(user["hashed_passwd"], passwd):
                print(user["name"])
                user = User(user["name"], user["email"], user["nick"], user["hashed_passwd"])
                resp = make_response(render_template('account.html', user = user))
                resp.set_cookie("token", token.generate_token(nick, user.getEmail()))
                return resp
    flash('Invalid Login!')
    return redirect(url_for('index'))

@app.route('/log_out')
def log_out():
    session.pop('nickname', None)
    flash('Has gone out of your account!')
    return redirect(url_for('index'))
    #return respo

if __name__ == '__main__':
    app.run(port = 3000, debug = True)
