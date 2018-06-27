from app import app
from flask import render_template, redirect, url_for, flash#flashes a message
from app.forms import LoginForm, RegisterForm
#look within app itself

@app.route('/') #still performs index function if this is included
@app.route('/index', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()#class we just created, but now need to pass form variable into BooleanField
    if login_form.validate_on_submit():#if form comes back true, form is submited correctly, anything in this will be executed
        flash('Thankyou for logging in {}!' .format(login_form.email.data))
        return redirect(url_for('login'))
    return render_template('index.html', form=login_form)

@app.route('/redirect')
def goaway():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()#class we just created, but now need to pass form variable into BooleanField
    if register_form.validate_on_submit():#if form comes back true, form is submited correctly, anything in this will be executed
        flash('Thanks {} for registering with us!'.format(register_form.username.data))
        return redirect(url_for('index'))
    return render_template('register.html', form=register_form)
