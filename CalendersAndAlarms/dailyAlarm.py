import datetime
from subroutines import *
daysofweek = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]


def obtain_today_events(user):
    todays_date = datetime.datetime.now()
    # #Get Lectures
    calendar = get_calender(user, "Lectures")
    # #Get Tutorials
    calendar += get_calender(user, "Tutorials")
    for event in calendar:
        if "Rule" in event.keys():
            if daysofweek[todays_date.weekday()] in event["Rule"].split(";BYDAY=")[1]:
                print(event)

obtain_today_events("George")

