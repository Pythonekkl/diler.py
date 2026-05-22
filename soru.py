#hava fuzesini algılama ve vurdu vurulmadı tesp etmek
# random ile hava fuzesini yazdırma 
# ve her yerde görülmesi
# ve her ateş atması 
# ve 3 ateşten sonra vurulması
import random
import time 
import sys

def yavas_yaz(metin, hiz=0.05):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(hiz)
    sys.stdout.write("\n")
    sys.stdout.flush()

pozisyonlar = ["kuzey", "güney", "doğu", "batı", "merkez", "kuzeydoğu", "kuzeybatı", "güneydoğu", "güneybatı"]
ates_sayisi = 0
vuruldu = False
onceki_konum = None

for i in range(5):
    # her seferinde farklı konum seçsin
    konum = random.choice([p for p in pozisyonlar if p != onceki_konum])
    onceki_konum = konum

    yavas_yaz(f"Fuze {konum} bölgesinde tespit edildi! ({i+1}. adım)")
    time.sleep(1)
    ates_sayisi += 1

    if ates_sayisi >= 3:
        vurus_bolgesi = random.choice(pozisyonlar)  # vurma bölgesi de rastgele
        yavas_yaz(f"Ates edildi! Hedef bölge: {vurus_bolgesi}")
        time.sleep(2)
        vuruldu = random.choice([True, False])
        if vuruldu:
            yavas_yaz(f"Fuze {vurus_bolgesi} bölgesinde vuruldu! Tehdit engellendi.")
            break
        else:
            yavas_yaz(f"Iskalandi! Fuze {vurus_bolgesi} bölgesinden kaçtı, devam ediyor.")
            time.sleep(1)
            ates_sayisi = 0

if not vuruldu:
    son_konum = random.choice(pozisyonlar)
    yavas_yaz(f"Fuze {son_konum} bölgesine ulasti! Tehdit engellenemedi.")