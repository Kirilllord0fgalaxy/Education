def figures(lines):
    if lines<=2 or lines>10:return 'Нет'
    nm510=['Пяти','Шести','Cеми','Восьми','Девяти','Десяти']
    if lines<5 and lines>=3:
        return 'Треугольник' if lines==3 else 'Прямоугольник/квадрат'
    else:
        return nm510[lines-5]+'гранник'
    
print(figures(int(input('Кол-во сторон'))))


"""
как запутанно получилось)
создать интевал всего для двух значений - lines<5 and lines>=3 -)
к тому же, написать там первым число бОльшее )
"""