from flask import Blueprint, jsonify
from app import db
from app.models import User, Appointment, Report

utl = Blueprint('util', __name__)


@utl.route('/generate/users', methods=['GET'])
def generate_users():
    db.session.execute("DELETE FROM user WHERE isAdmin = false;")
    db.session.commit()
    users = [{
        "name": "Glory Powley",
        "email": "gpowley0@noaa.gov",
        "password": "a8dQZpjEg",
        "morada": "2 Summer Ridge Place",
        "isAdmin": False,
        "image": "a.png",
        "contact": "983337960",
        "SSN": "148-93-5743"
    }, {
        "name": "Kele Jonsson",
        "email": "kjonsson1@redcross.org",
        "password": "78liTxLTt",
        "morada": "8 Kipling Point",
        "isAdmin": False,
        "image": "b.png",
        "contact": "977745104",
        "SSN": "739-07-7702",
    }, {
        "name": "Minnaminnie Darlison",
        "email": "mdarlison2@oaic.gov.au",
        "password": "L7H7yH",
        "morada": "055 Sherman Way",
        "isAdmin": False,
        "image": "c.png",
        "contact": "904443421",
        "SSN": "383-25-5052"
    }, {
        "name": "Novelia Ford",
        "email": "nford3@usda.gov",
        "password": "ddCodJiCIE2",
        "morada": "2662 Schmedeman Plaza",
        "isAdmin": False,
        "image": "d.png",
        "contact": "959577811",
        "SSN": "540-48-6840"
    }, {
        "name": "Bradney Andrioli",
        "email": "bandrioli4@gravatar.com",
        "password": "Jv0SvfT",
        "morada": "8065 Hagan Point",
        "isAdmin": False,
        "image": "e.png",
        "contact": "917514389",
        "SSN": "211-12-1538"
    }, {
        "name": "Katherine Geater",
        "email": "kgeater5@csmonitor.com",
        "password": "gLesmOzwA",
        "morada": "0994 Bultman Circle",
        "isAdmin": False,
        "image": "f.png",
        "contact": "909359893",
        "SSN": "785-98-7709"
    }, {
        "name": "Kerianne Diggar",
        "email": "kdiggar6@sun.com",
        "password": "OMS1yy0CuBZh",
        "morada": "5 Westport Park",
        "isAdmin": False,
        "image": "g.png",
        "contact": "946362219",
        "SSN": "174-24-9445"
    }, {
        "name": "Katharine Callacher",
        "email": "kcallacher7@baidu.com",
        "password": "j48nxuG9",
        "morada": "65365 Warbler Drive",
        "isAdmin": False,
        "image": "h.png",
        "contact": "991152914",
         "SSN": "669-33-8425"
    }, {
        "name": "Maribelle McGilroy",
        "email": "mmcgilroy8@msu.edu",
        "password": "saqZZwOi6ja",
        "morada": "6 Ridgeview Center",
        "isAdmin": False,
        "image": "i.png",
        "contact": "943233268",
        "SSN": "447-15-9336"
    }, {
        "name": "Ignacius MacCaffery",
        "email": "imaccaffery9@rambler.ru",
        "password": "6lmhKnR9",
        "morada": "807 Maywood Hill",
        "isAdmin": False,
        "image": "j.png",
        "contact": "948562298",
        "SSN": "701-22-6628"
    }, {
        "name": "Tadeas Joselovitch",
        "email": "tjoselovitch0@clickbank.net",
        "password": "btg9O1",
        "morada": "5098 Moland Drive",
        "isAdim": False,
        "image": "a.png",
        "contact": "920330455",
        "SSN": "356-30-6596"
    }, {
        "name": "Larisa Ashbolt",
        "email": "lashbolt1@archive.org",
        "password": "iYW18p4AJ7r",
        "morada": "9 Erie Pass",
        "isAdim": False,
        "image": "b.png",
        "contact": "946181414",
        "SSN": "606-75-0539"
    }, {
        "name": "Yul Luckin",
        "email": "yluckin2@amazon.co.uk",
        "password": "RRl4hDrfMra",
        "morada": "5995 Scott Center",
        "isAdim": False,
        "image": "c.png",
        "contact": "930655411",
        "SSN": "742-60-2083"
    }, {
        "name": "Filberte Ballach",
        "email": "fballach3@ucla.edu",
        "password": "btmaaJfRj",
        "morada": "3 Gale Drive",
        "isAdim": False,
        "image": "d.png",
        "contact": "931673617",
        "SSN": "621-13-0084"
    }, {
        "name": "Deanna Densumbe",
        "email": "ddensumbe4@gravatar.com",
        "password": "ps6WD4ij",
        "morada": "53 Jackson Court",
        "isAdim": False,
        "image": "g.png",
        "contact": "962137855",
        "SSN": "734-51-2216"
    }, {
        "name": "Tiffie Peattie",
        "email": "tpeattie5@house.gov",
        "password": "gvHzWU",
        "morada": "7 Little Fleur Trail",
        "isAdim": False,
        "image": "h.png",
        "contact": "906480555",
        "SSN": "686-32-0984"
    }, {
        "name": "Romona Paradine",
        "email": "rparadine6@creativecommons.org",
        "password": "SbJGTZ3H5Zn",
        "morada": "39861 Hansons Way",
        "isAdim": False,
        "image": "j.png",
        "contact": "997170237",
        "SSN": "152-55-4095"
    }, {
        "name": "Jessica Tharme",
        "email": "jtharme7@timesonline.co.uk",
        "password": "ozKGJiAjpe",
        "morada": "3 East Road",
        "isAdim": False,
        "image": "i.png",
        "contact": "999465788",
        "SSN": "155-19-9665",
    }, {
        "name": "Calv Pawelke",
        "email": "cpawelke8@indiatimes.com",
        "password": "k6JIske",
        "morada": "9153 Main Plaza",
        "isAdim": False,
        "image": "e.png",
        "contact": "963063612",
        "SSN": "497-73-6716",
    }, {
        "name": "Auberta Maliffe",
        "email": "amaliffe9@delicious.com",
        "password": "ljouXG0q5Y",
        "morada": "1 Northridge Drive",
        "isAdim": False,
        "image": "a.png",
        "contact": "967267984",
        "SSN": "778-48-5530"
    }]
    try:
        db.session.bulk_insert_mappings(User, users)
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        print(e)
        return jsonify({'success': False})


@utl.route('/generate/admin', methods=['GET'])
def generate_admin():
    db.session.execute("DELETE FROM user WHERE isAdmin = True;")
    db.session.commit()

    admin = User(name="Admin", email="admin@admin.com", password="admin", isAdmin=True)
    try:
        db.session.add(admin)
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        print(e)
        return jsonify({'success': False})


@utl.route('/generate/appointments', methods=['GET'])
def generate_appointments():
    users = User.query.all()
    if len(users) < 10:
        return jsonify({'success': False, 'message': 'Not enough users to generate appointments'})

    db.session.execute("DELETE FROM appointment;")
    appointments = [{
        "patientId": 3,
        "subject": "Appointment 1",
        "time": "10:00:00",
        "date": "9/9/2022",
        "description": "Spontaneous abortion, complicated by delayed or excessive hemorrhage, unspecified",
        "code": "8536425261"
    }, {
        "patientId": 7,
        "subject": "Appointment 1",
        "time": "10:00:00",
        "date": "2/17/2022",
        "description": "Old bucket handle tear of medial meniscus",
        "code": "6280159361"
    }, {
        "patientId": 1,
        "subject": "Appointment 1",
        "time": "10:00:00",
        "date": "9/11/2022",
        "description": "Open wound(s) (multiple) of unspecified site(s), without mention of complication",
        "code": "4127982381"
    }, {
        "patientId": 4,
        "subject": "Appointment 1",
        "time": "10:00:00",
        "date": "6/6/2022",
        "description": "Obstruction by abnormal pelvic soft tissues during labor, delivered, with or without mention of antepartum condition",
        "code": "0877142262"
    }, {
        "patientId": 8,
        "subject": "Appointment 1",
        "time": "10:00:00",
        "date": "10/27/2022",
        "description": "Other motor vehicle nontraffic accident while boarding and alighting injuring passenger in motor vehicle other than motorcycle",
        "code": "4171699363"
    }, {
        "patientId": 2,
        "subject": "Appointment 1",
        "time": "10:00:00",
        "date": "11/19/2021",
        "description": "Acute nonparalytic poliomyelitis, poliovirus type I",
        "code": "0148986021"
    }, {
        "patientId": 4,
        "subject": "Appointment 1",
        "time": "10:00:00",
        "date": "4/1/2022",
        "description": "Unspecified surgical operations and procedures causing abnormal patient reaction, or later complication, without mention of misadventure at time of operation",
        "code": "5709499218"
    }, {
        "patientId": 3,
        "subject": "Appointment 1",
        "time": "10:00:00",
        "date": "6/22/2022",
        "description": "Acute myocardial infarction of anterolateral wall, subsequent episode of care",
        "code": "6960288371"
    }, {
        "patientId": 10,
        "subject": "Appointment 1",
        "time": "10:00:00",
        "date": "5/26/2022",
        "description": "Open fracture of subtrochanteric section of neck of femur",
        "code": "1223488934"
    }, {
        "patientId": 2,
        "subject": "Appointment 1",
        "time": "10:00:00",
        "date": "5/23/2022",
        "description": "Subacute myeloid leukemia, without mention of having achieved remission",
        "code": "7553929948"
    }]
    try:
        db.session.bulk_insert_mappings(Appointment, appointments)
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        print(e)
        return jsonify({'success': False})

@utl.route('/generate/reports', methods=['GET'])
def generate_reports():
    db.session.execute("DELETE FROM report;")
    reports = [{
        "patientId": 3,
        "date": "9/9/2022",
        "description": "Spontaneous abortion, complicated by delayed or excessive hemorrhage, unspecified",
        "code": "8536425261"
    }, {
        "patientId": 7,
        "date": "2/17/2022",
        "description": "Old bucket handle tear of medial meniscus",
        "code": "6280159361"
    }, {
        "patientId": 1,
        "date": "9/11/2022",
        "description": "Open wound(s) (multiple) of unspecified site(s), without mention of complication",
        "code": "4127982381"
    }, {
        "patientId": 4,
        "date": "6/6/2022",
        "description": "Obstruction by abnormal pelvic soft tissues during labor, delivered, with or without mention of antepartum condition",
        "code": "0877142262"
    }, {
        "patientId": 8,
        "date": "10/27/2022",
        "description": "Other motor vehicle nontraffic accident while boarding and alighting injuring passenger in motor vehicle other than motorcycle",
        "code": "4171699363"
    }, {
        "patientId": 2,
        "date": "11/19/2021",
        "description": "Acute nonparalytic poliomyelitis, poliovirus type I",
        "code": "0148986021"
    }, {
        "patientId": 4,
        "date": "4/1/2022",
        "description": "Unspecified surgical operations and procedures causing abnormal patient reaction, or later complication, without mention of misadventure at time of operation",
        "code": "5709499218"
    }, {
        "patientId": 3,
        "date": "6/22/2022",
        "description": "Acute myocardial infarction of anterolateral wall, subsequent episode of care",
        "code": "6960288371"
    }, {
        "patientId": 10,
        "date": "5/26/2022",
        "description": "Open fracture of subtrochanteric section of neck of femur",
        "code": "1223488934"
    }, {
        "patientId": 2,
        "date": "5/23/2022",
        "description": "Subacute myeloid leukemia, without mention of having achieved remission",
        "code": "7553929948"
    }]

    try:
        db.session.bulk_insert_mappings(Report, reports)
        db.session.commit()

        return jsonify({'success': True})
    except Exception as e:
        print(e)
        return jsonify({'success': False})
