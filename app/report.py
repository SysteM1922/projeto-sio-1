import pdfkit
from flask import Blueprint, request, render_template, make_response
from flask_login import login_required

from app.models import Report, User

rpt = Blueprint("rpt", __name__)

@rpt.route("/report/<user_id>/", methods=["GET"])
@login_required
def test(user_id=None):
    user = User.query.filter_by(id=user_id).first()
    report = Report.query.filter_by(patientId=user_id).first()
    if report is None:
        return render_template("404.html", user=user, report=None)
    html = render_template("report.html", report=report, user=user)
    pdf = pdfkit.from_string(html, False)
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "inline; filename=output.pdf"
    return response


