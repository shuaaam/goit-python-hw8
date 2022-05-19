from datetime import datetime, timedelta

users = [
    {
        'name': 'Bill',
        'birthday': '19 May 2000'
    },
    {
        'name': 'Jill',
        'birthday': '26 May 2000'
    },
    {
        'name': 'Kim',
        'birthday': '20 May 2000'
    },
    {
        'name': 'Jan',
        'birthday': '22 May 2000'
    }
]

today = datetime.today()

monday = []
tuesday = []
wednesday = []
thursday = []
friday = []
result = {}


def get_birthdays_per_week(users: list) -> dict:
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%d %B %Y")
        birthday_intr = birthday.replace(year=today.year)
        interval = birthday_intr.date() - today.date()
        day = datetime.weekday(birthday_intr)
        if timedelta(1) <= interval <= timedelta(8):
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
                    result.update({d: ', '.join(tuesday)})
                if v == user.get("name") and d == "Wednesday":
                    wednesday.append(v)
                    result.update({d: ', '.join(wednesday)})
                if v == user.get("name") and d == "Thursday":
                    thursday.append(v)
                    result.update({d: ', '.join(thursday)})
                if v == user.get("name") and d == "Friday":
                    friday.append(v)
                    result.update({d: ', '.join(friday)})
                if v == user.get("name") and d == "Monday":
                    monday.append(v)
                    result.update({d: ', '.join(monday)})
    for k, v in result.items():
        print(k, ':', v)


get_birthdays_per_week(users)

