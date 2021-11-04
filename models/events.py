from models.event import *
import datetime

event1 = Event(datetime.date(2020, 5, 17), "Rugby Riot", 18, "West Wing", "Rugby room")
event2 = Event(datetime.date(2020, 4, 23), "Joe's 40th", 60, "East Wing", "Party hall")
event3 = Event(datetime.date(2020, 9, 26), "Cafeteria", 50, "Main Lobby", "Place to eat!")

events = [event1, event2, event3]

def create_event(x):
    events.append(x)