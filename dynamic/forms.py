#!/usr/bin/python3
"""forms for my web application"""
from flask_wtf import FlaskForm
from models import storage
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    phone = StringField('Phone')
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        """validates if email is already used by another user"""
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
    description = TextAreaField('Description')
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    zip_code = StringField('Zip Code', validators=[DataRequired()])
    latitude = FloatField('Latitude')
    longitude = FloatField('Longitude')
    services = StringField('Services (comma separated)',
                           validators=[DataRequired()])
    submit = SubmitField('Create Business')
