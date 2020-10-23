import datetime


def string_to_datetime(dt):
    print(dt)
    return datetime.datetime.strptime(dt, "%Y%m%d:%H%M%S")


def getcalender(folder, calender_name):
    pythonised_calender = []
    with open(r"{0}\{1}.ics".format(folder, calender_name), "r") as file:
        events = file.read().split("STATUS:CONFIRMED")[1:]
        for event in events:
            pythonised_calender.append({})
            for information in event.split("\n"):
                if "SUMMARY" in information:
                    pythonised_calender[-1]["SUMMARY"] = information[information.find(":")+1:]
                elif "DESCRIPTION" in information:
                    pythonised_calender[-1]["DESCRIPTION"] = information[information.find(":")+1:]
                elif "DTSTART" in information:
                    pythonised_calender[-1]["Start"] = string_to_datetime(information[information.find(":")+1:].replace("T", ":").replace("Z", ""))
                elif "DTEND" in information:
                    pythonised_calender[-1]["End"] = string_to_datetime(information[information.find(":")+1:].replace("T", ":").replace("Z", ""))
                elif "RRULE" in information:
                    pythonised_calender[-1]["Rule"] = information[information.find(":")+1:]
    return pythonised_calender
