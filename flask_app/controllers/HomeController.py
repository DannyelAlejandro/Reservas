from flask_app import app
from flask import render_template, url_for, redirect, session
from flask_app.models.Reservation import Reservation
from flask_app.models.Field import Field

@app.route('/')
def index():
    if "user" in session:
        if session['user'][1] == 'admin':
            #classrooms = mongo.db.classrooms.find()
            #nUsers = mongo.db.users.count_documents({})
            #nStudets = mongo.db.students.count_documents({})
            #nCalendars = mongo.db.calendars.count_documents({})
            #nClassrooms = mongo.db.classrooms.count_documents({})
            #return render_template('index.html', classrooms = classrooms, nUsers = nUsers, nStudets = nStudets, nCalendars = nCalendars, nClassrooms = nClassrooms)
            return render_template('pages/home/admin/index.html')
        if session['user'][1] == 'user':
            fields = Field.get()
            return render_template('pages/home/user/index.html', reservations = Reservation.getByUser(session['user'][0]), fields = fields)
    else:
        return redirect(url_for("login"))