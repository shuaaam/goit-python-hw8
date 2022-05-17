from datetime import date, datetime, timedelta

users = [
    {
        'name': 'Bill',
        'birthday': '16 May 2000'
    },
    {
        'name': 'Jill',
        'birthday': '15 May 2000'
    },
    {
        'name': 'Kim',
        'birthday': '20 May 2000'
    },
    {
        'name': 'Jan',
        'birthday': '20 May 2000'
    }
]
today = datetime.today()
interval = today + timedelta(days=7)
range_d = range(today, interval)


def get_birthdays_per_week(users):
    for i in users:
        birthday = datetime.strptime(i["birthday"], "%d %B %Y")
        theday = datetime(today.year, birthday.month, birthday.day)
        if theday.today in range_d:
            day = today.weekday()
            if day == 0:
                print("Monday: " + i['name'])
            if day == 1:
                print("Tuesday: ", + i['name'])
            if day == 2:
                print("Wednesday: " + i['name'])
            if day == 3:
                print("Thursday: " + i['name'])
            if day == 4:
                print("Friday: " + i['name'])
            if day in (5, 6):
                print('Next Monday: ' + i['name'])


get_birthdays_per_week(users)
