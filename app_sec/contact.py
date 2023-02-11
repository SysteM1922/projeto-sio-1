from flask import Blueprint, request, flash, redirect, url_for, render_template
from flask_login import login_required, current_user
from app_sec.models import Contact
from app_sec import db

ctc = Blueprint('ctc', __name__)


@ctc.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')


@ctc.route('/contact', methods=['POST'])
def contact_post():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    new_contact = Contact(name=name, email=email, message=message)
    try:
        db.session.add(new_contact)
        db.session.commit()
        flash('Your message has been sent. Thank you!')
        return redirect(url_for('main.index'))
    except:
        flash('There was an issue sending your message. Please try again.')
        return redirect(url_for('main.index'))


@ctc.route('/contacts', methods=['GET'])
@login_required
def contacts():
    if current_user.isAdmin:
        contacts = Contact.query.all()
        return render_template('contacts.html', contacts=contacts)
    else:
        flash('You do not have permission to view this page.')
        return redirect(url_for('main.index'))