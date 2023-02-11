from flask import Blueprint, render_template, flash,redirect, url_for, request
from flask_login import login_required, current_user
from flask import render_template,make_response
import pdfkit

from app_sec.models import User, Report
tst = Blueprint("tst", __name__)

@tst.route("/test/<user_id>/", methods=["GET"])
def test(user_id=None):
    user = User.query.filter_by(id=user_id).first()
    report = Report.query.filter_by(patientId=user_id).first()
    if report is None or user is None:
        return render_template("404.html", user=user, report=None)
    html = render_template("report.html", report=report, user=user)
    pdf = pdfkit.from_string(html, False)
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "inline; filename=output.pdf"
    return response

@tst.route("/tests", methods=["GET"])
def tests():
    return render_template("tests.html")

@tst.route("/test", methods=["POST"])
def generate_link():
    code = request.form.get("code")
    report = Report.query.filter_by(code=code).first()
    if report is None:
        return "No report found"
    elif report.patientId != current_user.id:
        return "You are not the owner of this report"
    else:
        return "Your link has been generated. Click <a href='/test/"+str(report.patientId)+"/'>here</a> to view your report."
