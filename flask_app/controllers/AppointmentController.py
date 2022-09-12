from crypt import methods
from flask_app import app
from flask_app.models.Appointment import Appointment
from flask import Response, session, request, session, render_template, url_for, redirect, jsonify

@app.route('/appointments', methods = ['GET'])
def indexAppointments():
    appointments = Appointment.getByUser(session['user_id'])
    return render_template('appointments/index.html', appointments = appointments)

@app.route('/appointments', methods = ['POST'])
def storeAppointments():
    data = { 
        "user_id": session['user_id'],
        "appointment_status": request.form['appointment_status'],
        "title": request.form['title'],
        "date_end": request.form['date_end']
    }
    Appointment.create(data)
    return redirect(url_for('indexAppointments'))

@app.route('/appointments/create', methods = ['GET'])
def createAppointments():
    return render_template('appointments/create.html')

@app.route('/appointments/edit/<id>', methods = ['GET'])
def editAppointments(id):
    data = Appointment.find(id)
    return render_template('appointments/edit.html', data = data[0], id = id)

@app.route('/appointments/update/<id>', methods = ['POST'])
def updateAppointments(id):
    data = {
        "appointment_status": request.form['appointment_status'],
        "title": request.form['title'],
        "date_end": request.form['date_end']
    }
    Appointment.update(id, data)

    return redirect(url_for('indexAppointments'))

@app.route('/appointments/delete/<id>', methods = ['GET'])
def deleteAppointments(id):
    Appointment.delete(id)
    return redirect(url_for('indexAppointments'))