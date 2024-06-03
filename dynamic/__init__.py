#!/usr/bin/python3
"""Initializes lookup flask web app"""
from flask import Flask
from flask_login import LoginManager
from models import storage


app = Flask(__name__)
app.config['SECRET_KEY'] =\
    '5c1c3a70c8d77982bb25f35303a456a16fe3133562403dd1c5888166052ce70a'
app.config['WTF_CSRF_ENABLED'] = True

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(user_id):
    return storage.get_user_by_id(user_id)


from dynamic import routes
