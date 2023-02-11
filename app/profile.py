from flask import Blueprint, render_template, redirect, url_for, request, flash, Flask
from flask_login import login_required, current_user
from .models import User
from . import db
import os
from werkzeug.security import generate_password_hash


prof = Blueprint('profile', __name__)

@prof.route('/profile')
@login_required
def profile():
	user = User.query.filter_by(id=current_user.id).first()	
	return render_template('profile.html', user=user)

@prof.route('/edit_profile/<id>', methods=['GET'])
@login_required
def edit_page(id):
	user = User.query.filter_by(id=id).first()
	return render_template('edit_profile.html', user=user)

@prof.route('/edit_profile/<id>', methods=['Post'])
@login_required
def edit_profile(id):
	email = request.form.get('email')
	address = request.form.get('address')
	contact = request.form.get('contact')
	image = request.files.get('image')
	new_password = request.form.get('new_password')
	confirm_new_password = request.form.get('confirm_new_password')

	user = User.query.filter_by(id=id).first()
	if new_password:
		if new_password == confirm_new_password:
			user.password = generate_password_hash(new_password)
		else:
			flash('Passwords do not match.')
			return render_template('edit_profile.html', user=user)
	
	if email:
		user.email = email
	if address:
		user.morada = address
	if contact:
		user.contact = contact
	if image:
		user.image = image.filename
		image.save(os.path.join("app/static/pictures",image.filename))
	
	db.session.commit()
	return redirect(url_for('profile.profile'))