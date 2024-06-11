#!/usr/bin/python3
"""handles the business logic of my web app"""
import os
from models import storage
from models.business_user import BusinessUser
from models.business import Business
from models.service import Service
from models.location import Location
from dynamic import app
import secrets
from PIL import Image
from dynamic.forms import (RegistrationForm, LoginForm,
                           BusinessForm, UpdateAccountForm)
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user


@app.route('/')
@app.route('/home')
def home():
    businesses = storage.all(Business)
    return render_template('home.html', businesses=businesses)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """register a new business user"""
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    form1 = BusinessForm()
    if form.validate_on_submit() and form1.validate_on_submit():
        user = BusinessUser(email=form.email.data,
                            password=form.password.data,
                            first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            phone=form.phone.data)
        storage.new(user)

        location = Location(address=form1.address.data,
                            city=form1.city.data,
                            state=form1.state.data,
                            country=form1.country.data,
                            zip_code=form1.zip_code.data)
        storage.new(location)

        business = Business(name=form1.name.data,
                            description=form1.description.data,
                            business_user_id=user.id,
                            location_id=location.id)
        storage.new(business)

        service = Service(name=form1.service_name.data,
                          description=form1.servicedescription.data,
                          business_id=business.id)
        storage.new(service)

        storage.save()
        flash('Account created successfully', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register',
                           form=form, form1=form1)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = storage.get_user_by_email(form.email.data)
        if user and user.verify_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page\
                else redirect(url_for('account'))
        else:
            flash('Login Unsuccessful. Please check email and password',
                  'danger')
    return render_template('login.html', form=form, title='Login')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    """logic for saving business user profile picture"""
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics',
                                picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    # delete old profile picture
    old_pic = os.path.join(app.root_path, 'static/profile_pics',
                           current_user.profile_pic)
    if os.path.exists(old_pic) and current_user.profile_pic != 'default.jpg':
        os.remove(old_pic)

    return picture_fn


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    businesses = current_user.businesses
    if form.validate_on_submit():
        if form.profile_pic.data:
            picture_file = save_picture(form.profile_pic.data)
            current_user.profile_pic = picture_file
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        current_user.phone = form.phone.data
        current_user.save()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
        form.phone.data = current_user.phone
    profile_pic = url_for('static',
                          filename='profile_pics/' + current_user.profile_pic)
    return render_template('account.html', title='Account',
                           profile_pic=profile_pic, form=form,
                           businesses=businesses)


@app.route("/business/<string:business_id>", methods=['GET', 'POST'])
@login_required
def business(business_id):
    business = storage.get(Business, business_id)
    if not business or business.business_user_id != current_user.id:
        abort(403)
    location = storage.get(Location, business.location_id)
    service = storage.get_service(business.id)

    form = BusinessForm()

    if form.validate_on_submit():
        location.address = form.address.data
        location.city = form.city.data
        location.state = form.state.data
        location.country = form.country.data
        location.zip_code = form.zip_code.data
        location.save()

        business.name = form.name.data
        business.description = form.description.data
        business.save()

        service.name = form.service_name.data
        service.description = form.servicedescription.data
        service.save()
        flash('Business has been updated!', 'success')
        return redirect(url_for('business', business_id=business.id))
    elif request.method == 'GET':
        form.name.data = business.name
        form.description.data = business.description
        form.address.data = location.address
        form.city.data = location.city
        form.state.data = location.state
        form.country.data = location.country
        form.zip_code.data = location.zip_code
        form.service_name.data = service.name
        form.servicedescription.data = service.description
    profile_pic = url_for('static',
                          filename='profile_pics/' + current_user.profile_pic)
    return render_template('business.html', title='Business Details',
                           form=form, business=business,
                           profile_pic=profile_pic)


@app.route("/register_business", methods=['GET', 'POST'])
@login_required
def register_business():
    form = BusinessForm()
    if form.validate_on_submit():
        location = Location(address=form.address.data,
                            city=form.city.data,
                            state=form.state.data,
                            country=form.country.data,
                            zip_code=form.zip_code.data)
        storage.new(location)

        business = Business(name=form.name.data,
                            description=form.description.data,
                            business_user_id=current_user.id,
                            location_id=location.id)
        storage.new(business)

        service = Service(name=form.service_name.data,
                          description=form.servicedescription.data,
                          business_id=business.id)
        storage.new(service)

        storage.save()
        flash('Your business has been registered!', 'success')
        return redirect(url_for('account'))
    profile_pic = url_for('static',
                          filename='profile_pics/' + current_user.profile_pic)
    return render_template('register_business.html', title='Register Business',
                           form=form, profile_pic=profile_pic)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()
