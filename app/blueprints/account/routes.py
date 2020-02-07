from app import db
from app.models import User
from flask import render_template, redirect, url_for, flash
from app.forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user
from app.blueprints.account import account

@account.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    context = {
        'form': form
    }
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("You've used the wrong email or password,\ntry again!", "danger")
            return redirect(url_for('account.login'))

        flash("You have logged in successfully!", "success")
        login_user(user)
        return redirect(url_for('account.login'))
    return render_template('login.html', **context)

@account.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        u = User(name=form.name.data, email=form.email.data)
        u.generate_password(form.password.data)
        db.session.add(u)
        db.session.commit()
        flash("You have registered successfully!", 'success')
        return redirect(url_for('account.login'))
        
    context = {
        'form': form
    }
    return render_template('register.html', **context)

@account.route('/logout')
def logout():
    logout_user()
    flash("You have logged out", "danger")
    return redirect(url_for('account.login'))