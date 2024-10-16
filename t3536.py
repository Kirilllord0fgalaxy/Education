
#35 задача

def true(num):
    return 'Четное' if num%2==0 else 'Нечетное'

#36 задача
# мы должны из собачего переводить в человечий, а не наоборот )
# Напишите программу, которая будет переводить человеческий возраст в  собачий с  учетом указанной выше логики. Это написано в задачнике
def doglife(age):
    if age<0:return 'Ошибка, число отрицательное'
    res=0
    if age<21:return res + age/10.5
    elif age-21>=0:
        res+=2
        age-=21
    return res + age/4

#Print 36зд

print(doglife(int(input())))

#Print 35зд

print(true(int(input('Цифра'))))
