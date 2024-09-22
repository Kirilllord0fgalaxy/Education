
#35 задача

def true(num):
    return 'Четное' if num%2==0 else 'Нечетное'

#36 задача

def doglife(age):
    res=0
    if age>0:
        if age<10.5:return res + age/10.5
        if age-21<0 and age-21>=10.5:
            res+=1
            age-=10.5
        elif age-21>=0:
            res+=2
            age-=21
    elif age<0:return'-'
    return res + age/4

#Print 36зд

print(doglife(int(input())))

#Print 35зд

print(true(int(input('Цифра'))))
