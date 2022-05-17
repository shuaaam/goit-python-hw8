from datetime import datetime, timedelta

users = [
    {
        'name': 'Bill',
        'birthday': '16 May 2000'
    },
    {
        'name': 'Jill',
        'birthday': '17 May 2000'
    },
    {
        'name': 'Kim',
        'birthday': '15 May 2000'
    },
    {
        'name': 'Jan',
        'birthday': '20 May 2000'
    }
]

today = datetime.today()
interval = today + timedelta(days=7)

monday = []
tuesday = []
wednesday = []
thursday = []
friday = []
result = {}


def get_birthdays_per_week(users: list) -> dict:
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%d %B %Y")
        theday = datetime(today.year, birthday.month, birthday.day)
        if today <= theday.today() <= interval:
            day = theday.weekday()
            if day == 1:
                d = 'Tuesday'
            if day == 2:
                d = 'Wednesday'
            if day == 3:
                d = 'Thursday'
            if day == 4:
                d = 'Friday'
            if day in (0, 5, 6):
                d = 'Monday'
            for k, v in user.items():
                if v == user.get("name") and d == "Tuesday":
                    tuesday.append(v)
                    result.update({d: tuesday})
                if v == user.get("name") and d == "Wednesday":
                    wednesday.append(v)
                    result.update({d: wednesday})
                if v == user.get("name") and d == "Thursday":
                    thursday.append(v)
                    result.update({d: thursday})
                if v == user.get("name") and d == "Friday":
                    friday.append(v)
                    result.update({d: friday})
                if v == user.get("name") and d == "Monday":
                    monday.append(v)
                    result.update({d: monday})
    return result


print(get_birthdays_per_week(users))
