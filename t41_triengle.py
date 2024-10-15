def tri(lines):
    lines = list(map(int,lines.split()))
    if len(set(lines))==3:return 'Разносторонний'
    return 'Равносторонние' if len(set(lines))==1 else 'Равнобедренный'
print(tri(input()))


"""
а что мы тут спрашиваем?

Напишите программу, которая будет запрашивать у пользователя дли-
ны всех трех сторон треугольника 
"""