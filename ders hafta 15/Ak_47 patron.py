import random
Mahkum=[]
olen=""
duygu_durumu=["Üzgün","Korkmuş","Umursamaz","Ağlamış","Pişman"]
for i in range(6):
    kisi=input(f"{i+1}. Mahkum Adını Gir")
    Mahkum.append(kisi)
Kurtulanlar=Mahkum
revolver=random.randint(1,6)
print(revolver)
patlama=0
deneme=0
while patlama!=True:
    duygu=random.randint(0,4)
    print(f" {Mahkum[deneme]} {duygu_durumu[duygu]} görünüyor")
    if (deneme+1 == revolver):
        print(f"BoooM... {Mahkum[deneme]} Öldü")
        patlama=1 #Burak Şahin Tarafından Kodlandı
        olen=Mahkum[deneme]
        Kurtulanlar.remove(Mahkum[deneme])
    elif (deneme+1 != revolver):
        print(f"{Mahkum[deneme]} kişisi kurtuldu sıra {deneme+1}. kişiye geçti")
    deneme+=1
for i in range(len(Kurtulanlar)):
    print(Kurtulanlar[i])
print(f"{olen} Kişisi Öldü")
