import random
kurban_listesi=[]
kurtulanlar=[]
infaz_edilen=" "
for i in range(6):
    sec =input("secilecek mahkum adını oku")
    kurban_listesi.append(sec)
    print("{} sahneye çıkarıldı".format(sec))
silah_patladi=0 
sayac=1 #çünkü sayac indisi tutmuyor
r=random.randint(1,6)
print("ss subayı silahını çıkardı ve rus ruleti için hazırladı.")
while silah_patladi==False:
    if sayac==r:
        print(f"boom ..... {sayac}.kişi öldü")
        silah_patladi=True
        infaz_edilen=kurban_listesi[sayac-1]
    else:
        print(f"Tıkk {sayac}. kişi kurtuldu sıra {sayac+1}.Kişide")
        sayac+=1
if (sayac!=6):
    for i in range (len(kurban_listesi)):
        if kurban_listesi[i] == infaz_edilen:
            pass
        else:
            kurtulanlar.append(kurban_listesi[i])
