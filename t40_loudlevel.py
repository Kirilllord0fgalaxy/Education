def loudlevel(loud):
    thingsl=[['Тихая комната',40],['Будильник',70],['Газовая газонокосилка',106],['Отбойный молоток',130]]
    for i in range(0,len(thingsl)):
        if thingsl[i][1]==loud:return f'Уровень шума соответствует {thingsl[i][0]}'
        elif loud>thingsl[i][1] and loud<thingsl[i+1][1]: return f'Шум больше {thingsl[i][0]},но меньше {thingsl[i+1][0]}'
        else:
            if loud<thingsl[0][1]:return f'Шум меньше {thingsl[0][0]}'
            else:return f'Шум больше {thingsl[-1][0]}'
print(loudlevel(40))