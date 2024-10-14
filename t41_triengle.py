def tri(lines):
    lines = list(map(int,lines.split()))
    if len(set(lines))==3:return 'Разносторонний'
    return 'Равносторонние' if len(set(lines))==1 else 'Равнобедренный'
print(tri(input()))