def chess(coo):
    strcoo={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
    return 'белая' if strcoo[coo[0]]%2==0 and int(coo[1])%2!=0 or strcoo[coo[0]]%2!=0 and int(coo[1])%2==0 else 'чёрная'

print(chess(input()))