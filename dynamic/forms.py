#!/usr/bin/python3
"""forms for my web application"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from models import storage
from wtforms import (StringField, PasswordField, SubmitField,
                     BooleanField, TextAreaField, FloatField)
from wtforms.validators import (DataRequired, Email, EqualTo, Length,
                                ValidationError)
from flask_login import current_user


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    phone = StringField('Phone')
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        """validates if email is already used by another user"""
        user = storage.get_user_by_email(email.data)
        if user:
            raise ValidationError('email already in use')


class UpdateAccountForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    phone = StringField('Phone')
    profile_pic = FileField('Update Profile Picture',
                            validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_email(self, email):
        """validates if email is already used by another user"""
        if email.data != current_user.email:
            user = storage.get_user_by_email(email.data)
            if user:
                raise ValidationError('email already in use')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class BusinessForm(FlaskForm):
    name = StringField('Business Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    zip_code = StringField('Zip Code', validators=[DataRequired()])
    services = StringField('Services (comma separated)',
                           validators=[DataRequired()])
    servicedescription = TextAreaField('Descript Your Service',
                                       validators=[DataRequired()])
    submit = SubmitField('Create Business')
