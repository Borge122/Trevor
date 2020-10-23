import datetime
from subroutines import *


def obtain(user):
    todays_date = datetime.datetime.now()
    # #Get Lectures
    calendar = get_calender(user, "Lectures")
    # #Get Tutorials
    calendar += get_calender(user, "Tutorials")
    for event in calendar:
        if "Start" in event.keys():
            if todays_date.weekday() == event["Start"].weekday():
                print(event)
obtain("George")

