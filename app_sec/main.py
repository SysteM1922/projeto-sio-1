from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app_sec import db
from app_sec.models import User
from werkzeug.security import generate_password_hash

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')