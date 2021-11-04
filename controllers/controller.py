from flask import render_template, request, redirect
from app import app
from models.events import Event
from models.events import events, create_event
import datetime

@app.route('/')
def greeting():
    return "Welcome to our Events!"

@app.route('/events')
def list_all():
    return render_template('index.html', title="Event List", events=events)

@app.route('/events_planner')
def index():
    return render_template('events_planner.html', title="Create Event")

@app.route('/events_planner', methods=['POST'])
def create(): 
    print(request.form)
    event_date = request.form['date']
    event_name_of_event = request.form['name_of_event']
    event_number_of_guests = request.form['number_of_guests']
    event_room_location = request.form['room_location']
    event_description = request.form['description']
    new_event = Event(event_date, event_name_of_event, event_number_of_guests, event_room_location, event_description)
    create_event(new_event)
    return redirect('/events')
