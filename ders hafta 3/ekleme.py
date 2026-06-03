#BURAK ŞAHİN TARAFINDAN KODLANDI
from a import *
try:
    f=open("ogrenciler.txt","x",encoding="utf-8")
except FileExistsError:                 
    print("ogrenciler txt dosyası var")
with open ("ogrenciler.txt","w",encoding="utf-8") as yazma:
    for i in ogrenciler:
        yazma.write(i["isim"]+" "+i["cinsiyet"]+" "+ str(i["yas"])+"\n")