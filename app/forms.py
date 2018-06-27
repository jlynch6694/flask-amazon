from flask_wtf import FlaskForm #flask form class all forms will inherit this
from wtforms import StringField, PasswordField, BooleanField, SubmitField#importing different types of fields to allow us to easily create input fields
from wtforms.validators import DataRequired, EqualTo, Email#validations make sure passwords are equal, correct email, etc

class LoginForm(FlaskForm):
    email = StringField('Email (phone used for mobile accounts)', validators=[DataRequired(), Email()])
    submit1 = SubmitField('Continue')
    submit2 = SubmitField('Create Your Amazon Account')
    #created a class of login form-need to implement into routes

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Retype Password:', validators=[DataRequired(), EqualTo('password')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Create Your Account')
