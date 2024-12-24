import pandas

def temp():
    cel=[]
    far=[]
    for i in range(1,102,10):
        if i > 1: 
            cel.append(i-1)
            far.append((i-1)*9/5+32)
    p = pandas.Series(far,cel)
    return p

print(temp())