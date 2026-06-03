from calisma_1 import *
diziler=[['Ali','Veli','Hasan','Cemal','Sıla','Damla'],        
['Hasan','Cemal','Ali'],['Sıla','Damla'],['Ali','Veli','Hasan','Ali','Veli','Hasan','Cemal','Sıla'],['Ali','Veli','Hasan','Cemal','Damla'],['Ali']]
print("**************************")
def betik2(listem):
    sayac=0
    try:
        while True:
            x=listem[sayac]
            sayac+=1
    except:
        pass
    return sayac
#print(betik2(dizi2))
def trade(deger):
    if deger<=1:
        print("LOT ALIMI YAPILDI")
    elif deger>=7:
        print("LOT SATIMI YAPILDI")
    elif deger>1 and deger<7:
        print("BEKLE")
    else:
        print("Geçerli Değer Değil")
for i in diziler:
    deger=int(betik2(i))
    trade(deger)