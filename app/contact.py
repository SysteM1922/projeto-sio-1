from flask import Blueprint, request, flash, redirect, url_for, render_template
from flask_login import login_required, current_user
from . import db

ctc = Blueprint('ctc', __name__)


@ctc.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')


@ctc.route('/contact', methods=['POST'])
def contact_post():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    try:
        db.session.execute("INSERT INTO contact (name, email, message) VALUES ('"+name+"', '"+email+"', '"+message+"');")
        db.session.commit()
        flash('Your message has been sent. Thank you!')
        return redirect(url_for('main.index'))
    except Exception as e:
        flash('There was an issue sending your message. Please try again.')
        print(e)
        return redirect(url_for('main.index'))


@ctc.route('/contacts', methods=['GET'])
@login_required
def contacts():
    if current_user.isAdmin:
        contacts = db.session.execute("SELECT * FROM contact;").fetchall()
        return render_template('contacts.html', contacts=contacts)
    else:
        flash('You do not have permission to view this page.')
        return redirect(url_for('main.index'))