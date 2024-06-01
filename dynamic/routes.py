#!/usr/bin/python3
"""handles the business logic of my web app"""
from models import storage
from models.business_user import BusinessUser
from models.business import Business
from models.service import Service
from models.location import Location
from dynamic import app
from dynamic.forms import RegistrationForm, LoginForm, BusinessForm
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """register a new business user"""
    form = RegistrationForm()
    if form.validate_on_submit():
        user = BusinessUser(email=form.email.data,
                            password=form.password.data,
                            first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            phone=form.phone.data)
        storage.new(user)
        storage.save()
        flash('Account created successfully', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = storage.get_user_by_email(form.email.data)
        if user and user.verify_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('profile'))
        flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()
