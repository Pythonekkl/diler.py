def ihtimal(kisi):
    ihtimall=1/(7-kisi)
    for i in range(1,kisi):
        ihtimall*=(6-i)/(7-i)
    return ihtimall

for i in range (1,7,1):
    print(ihtimal(i))
def ihtimalkovan(kisi,kovan):
    ihtimall = 1 / (kovan+1 - kisi)
    for i in range(1, kisi):
        ihtimall *= (kovan - i) / (kovan+1 - i)
    return ihtimall
for i in range (1,6):
    print(ihtimalkovan(i,6))
"""def ihtimal2(kisi):
    if kisi==1:
        return 1/6
    elif kisi==2:
        return 1/(7-kisi)*5/6
    elif kisi==3:
        return 1/(7-kisi)*5/6*4/5
    elif kisi==4:
        return 1/(7-kisi)*5/6*4/5*3/4
    elif kisi==5:
        return 1/(7-kisi)*5/6*4/5*3/4*2/3
    elif kisi==6:
        return 1/(7-kisi)*5/6*4/5*3/4*2/3*1/2"""