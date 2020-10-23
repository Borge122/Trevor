NAME = "George"
CALENDER = "Lectures"
with open(r"{0}\{1}.ics".format(NAME, CALENDER), "r") as file:
    events = file.read().split("STATUS:CONFIRMED")[1:]
    for event in events:
        print(event)
