def dmonth(month):
    months={'Январь':1,'Март':3,'Апрель':4,'Май':5,'Июнь':6,'Июль':7,'Август':8,'Сентябрь':9,'Октябрь':10,'Ноябрь':11,'Декабрь':12}
    if month=='Февраль':return '28,29'
    return 31 if months[month] % 2 == 0 else 30

print(dmonth(input()))