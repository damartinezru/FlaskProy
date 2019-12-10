# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, flash
import hashlib, binascii, os
from model import User

app = Flask(__name__)

app.secret_key = 'mysecretkey'

#User definition
def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    passwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                salt, 100000)
    passwdhash = binascii.hexlify(passwdhash)
    return (salt + passwdhash).decode('ascii')

def verify_password(stored_passwd, provided_passwd):
    salt = stored_passwd[:64]
    stored_passwd = stored_passwd[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_passwd.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_passwd
user_p = User(0, "Nombre", "Email@mail.com", "Nickname", hash_password("12345"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login_user', methods = ['POST'])
def login_user():
    if request.method == 'POST':
        nick = request.form['nick']
        passwd = request.form['pass']
        if nick == user_p.getNick() and verify_password(user_p.getPass(),passwd): #passwd == user_p.getPass():
            user = user_p
            return render_template('account.html', user = user)
    flash('Invalid Login!')
    return redirect(url_for('index'))

@app.route('/log_out')
def log_out():
    flash('Has gone out of your account!')
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(port = 3000, debug = True)
