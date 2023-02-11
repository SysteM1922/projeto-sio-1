from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app_sec.models import User
from app_sec import db
from werkzeug.security import generate_password_hash, check_password_hash
import os

prof = Blueprint('profile', __name__)

@prof.route('/profile')
@login_required
def profile():
	user = User.query.filter_by(id=current_user.id).first()
	return render_template('profile.html', user=user)

@prof.route('/edit_profile/')
@login_required
def edit_page():
	user = User.query.filter_by(id=current_user.id).first()
	return render_template('edit_profile.html', user=user)

@prof.route('/edit_profile', methods=['POST'])
@login_required
def edit_profile():
	email = request.form.get('email')
	address = request.form.get('address')
	contact = request.form.get('contact')
	image = request.files.get('image')
	if image and not image.filename.endswith('.png') and not image.filename.endswith('.jpeg'):
		flash('Please upload a png or jpeg image.')
		return redirect(url_for('profile.edit_profile'))
	
	password = request.form.get('password')
	user = User.query.filter_by(id=current_user.id).first()
	SpecialSym = "~`! @#$%^&*()_-+={[}]|\:;\"'<,>.?/"
	
	if password and check_password_hash(current_user.password,password):
		new_password = request.form.get('new_password')
		if new_password:
			confirm_new_password = request.form.get('confirm_new_password')
			if new_password == confirm_new_password:
				if len(new_password) < 8:
					flash('length should be at least 8')
					return redirect(url_for('profile.edit_profile'))
				elif not any(char.isdigit() for char in new_password) :
					flash('Password should have at least one numeral')
					return redirect(url_for('profile.edit_profile'))
				elif not any(char.isupper() for char in new_password):
					flash('Password should have at least one uppercase letter')
					return redirect(url_for('profile.edit_profile'))
				elif not any(char.islower() for char in new_password):
					flash('Password should have at least one lowercase letter')
					return redirect(url_for('profile.edit_profile'))
				elif not any(char in SpecialSym for char in new_password):
					flash('Password should have at least one of the  special symbols')
					return redirect(url_for('profile.edit_profile'))
				else: 
					user.password = generate_password_hash(new_password)
			elif new_password == password:
				flash('New password and old password do match')
				return redirect(url_for('profile.edit_profile'))
			else:
				flash('The new passwords and Confirm password do not match.')
				return redirect(url_for('profile.edit_profile'))

		if email:
			user.email = email
		if address:
			user.morada = address
		if contact:
			user.contact = contact
		if image:
			user.image = image.filename
			image.save(os.path.join("app_sec/static/pictures",image.filename))
		db.session.commit()
	else:
		flash('Wrong password.')
		return redirect(url_for('profile.edit_profile'))
	
	flash('Updated successfully.')
	return redirect(url_for('profile.profile'))
