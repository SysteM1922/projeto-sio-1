from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app_sec.models import User
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile.profile'))
    else:
        return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user)
    return redirect(url_for('profile.profile'))


@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
