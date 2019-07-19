import datetime as dt
from flask import Flask, render_template, request, redirect, url_for
from flask_httpauth import HTTPBasicAuth
import json


app = Flask(__name__)

auth = HTTPBasicAuth()

user_f = open('login.json', 'r')
users = json.load(user_f)

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/')
@auth.login_required
def input():
    title = "ナッシュ均衡計算ページにようこそ %s" % auth.username()

    message = {}
    message['today'] = dt.date.today().strftime('%Y-%m-%d')

    # index.html をレンダリングする
    return render_template('input.html',
                           message=message, title=title)
