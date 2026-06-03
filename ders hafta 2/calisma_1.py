dizi = ['Ali','Eren','Metin','Burak']
print(len(dizi))                    #BURAK ŞAHİN TARAFINDAN KODLANDI
print("----------------------------")
try:
    sayac = 0
    while True:
        print(dizi[sayac])
        print(sayac)
        sayac+=1                
except:
    pass
def betik (listem):
    sayac = 0
    try:
        while True:
            x=listem[sayac]
            sayac+=1
    except:
        print(sayac)
print("-----------------------------")
betik(dizi)