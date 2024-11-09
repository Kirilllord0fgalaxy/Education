import datetime
import calendar

def work(stvac,endvac,holidays):
    workdays=0
    td = stvac - datetime.timedelta(days=1)
    for _ in range(stvac.day,endvac.day+1):
        td += datetime.timedelta(days=1)
        if td not in holidays and td.weekday() < 5:
            workdays+=1
        print(td)
    return workdays



stvac = datetime.datetime.strptime(input('дд.мм.гггг'), '%d.%m.%Y').date()
endvac = datetime.datetime.strptime(input('дд.мм.гггг'), '%d.%m.%Y').date()
holidays = [datetime.date(2024, 11, 4),datetime.date(2024, 12, 31),datetime.date(2024, 5, 9),datetime.date(2024, 3, 8)]
print(work(stvac,endvac,holidays))