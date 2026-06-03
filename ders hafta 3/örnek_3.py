from a import *
sayac=0
for i in ogrenciler:
    print(i)                       
for i in ogrenciler:
    if i["yas"]<20:
        #print(i)
        sayac=sayac+1
    print("******************")
    if i["yas"]<20 and i["cinsiyet"]=="Kadın":
        print(i)
print("***********************")
print("Toplamda ",sayac," öğrenci 20 yaşından küçük")
