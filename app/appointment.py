from flask import Blueprint, render_template, flash,redirect, url_for, request, jsonify
from flask_login import login_required, current_user
from .models import Appointment, AppointmentSchema
from . import db

apt = Blueprint("apt", __name__)


@apt.route("/appointment", methods=["GET"])
@login_required
def appointment():
    return render_template("appointment.html")

@apt.route("/appointment", methods=["POST"])
@login_required
def appointment_post():
    print(request.form)
    subject = request.form.get("subject")
    description = request.form.get("description")
    date = request.form.get("date")
    time = request.form.get("time")
    patientId = current_user.id

    new_appointment = Appointment(subject=subject, description=description, date=date, time=time, patientId=patientId)
    try:
        db.session.add(new_appointment)
        db.session.commit()
        flash("Your appointment has been scheduled. Thank you!")
        return redirect(url_for("profile.profile"))
    except Exception as e:
        print(e)
        flash("There was an issue scheduling your appointment. Please try again.")
        return redirect(url_for("main.index"))

@apt.route("/appointments", methods=["GET"])
@login_required
def appointments():
    if current_user.isAdmin:
        appointments = Appointment.query.order_by(Appointment.date.desc()).limit(5).all()
        return render_template("appointments.html", appointments=appointments)
    else:
        appointments = Appointment.query.filter_by(patientId=current_user.id).all()
        return render_template("appointments.html", appointments=appointments)


class AlchemyEncoder:
    pass


@apt.route("/api/appointments", methods=["GET"])
@login_required
def api_appointments():
    page = request.args.get("page", 1, type=int)
    if current_user.isAdmin:
        appointments = Appointment.query.order_by(Appointment.date.desc()).paginate(page=page, per_page=5,error_out=False )
        appointments_schema = AppointmentSchema(many=True)
        output = appointments_schema.dump(appointments)
        if output:
            return jsonify(output)
        else:
            return jsonify([])
    else:
        appointments = Appointment.query.filter_by(patientId=current_user.id).paginate(page=page, per_page=5, error_out=False )
        appointments_schema = AppointmentSchema(many=True)
        output = appointments_schema.dump(appointments)
        if output:
            return jsonify(output)
        else:
            return jsonify([])