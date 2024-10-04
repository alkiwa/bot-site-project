import openpyxl
sheet = openpyxl.open("table.xlsx", read_only=True).active

group = {"CST 1": 4, "CST 2": 7, "CST 3": 10, 'CST 4': 16, "CST 5": 19, "CST 6": 22, "CST 7": 28, "CST 8": 31,
         "CST 9": 34} #ключи - инфа из бд от чела

def get_group_schedule(colon: int, day: str):
    lessons = [str(i).replace('-','').strip() for i in [sheet[i][colon].value for i in range(11, 73)]] #выявление нужных ячеек таблицы с расписанием
    classes = [str(i).replace('-','').strip() for i in [sheet[i][colon + 1].value for i in range(11, 73)]] #кабинеты соответствующих пар
    schedule = list(map(lambda x, y: x + "           " + y, lessons,classes))
    days = {"monday": [1, 8], "tuesday": [12, 18], "wednesday": [23, 31], "thursday": [34, 42], "friday": [45, 53],
            "sunday": [56, 64]}
    lessons_time = ["1) 8:00-9:20", "2) 9:30-10:50", "3) 11:10-12:30", "4) 13:00-14:20", "5) 14:40-16:00",
                    "6) 16:20-17:40", "7) 18:10-19:30", "8) 19:40-21:00"]

    result = schedule[days[day][0]:days[day][1]]
    return dict(zip(lessons_time, result))
{print(k, v) for k, v in get_group_schedule(group['CST 4'], "monday").items() if "None" not in v}