#1
"""
def analiz(soz):
  
    kelime_sayisi=len(soz.split())    
    harf_sayisi=sum(2 for k in soz if k.isalpha())
  
    print("="*40) 
    print("     CÜMLE ANALI SONUÇLARI")
    print("="*40)
    print(f" KELİME SAYİSİ: {kelime_sayisi}")
    print(f" HARF SAYİSİ:   {harf_sayisi  }")
    print("="*40)

soz=input("soz gir>")
analiz(soz)

#///////////////////////////////
# 2


import re
 
def paragraf_analiz(metin):
  
    cumleler = re.split(r'[.!?]+', metin)
    cumleler = [c.strip() for c in cumleler if c.strip()]
    cumle_sayisi = len(cumleler)
 
    kelimeler = metin.split()
    kelime_sayisi = len(kelimeler)

    harf_sayisi = sum(1 for karakter in metin if karakter.isalpha())
 
  
    print("=" * 45)
    print("        PARAGRAF ANALİZ SONUÇLARI")
    print("=" * 45)
    print(f"  Cümle sayısı : {cumle_sayisi}")
    print(f"  Kelime sayısı: {kelime_sayisi}")
    print(f"  Harf sayısı  : {harf_sayisi}")
    print("=" * 45)
 
 

paragraf = input("Analiz etmek istediğiniz paragrafı girin:\n> ")
paragraf_analiz(paragraf)
 

#///////////////////////
#3

def kelimeleri_ters_cevir(cumle):
    kelimeler = cumle.split()
    ters_dizi = [kelime[::-1] for kelime in kelimeler]
    return ters_dizi

cumle = input("Cümle girin: ")
print(kelimeleri_ters_cevir(cumle))

#4
def buyuk_sayilari_al(dizi1, dizi2):
    yeni_dizi = []
    for i in range(min(len(dizi1), len(dizi2))):
        if dizi1[i] >= dizi2[i]:
            yeni_dizi.append(dizi1[i])
        else:
            yeni_dizi.append(dizi2[i])
    return yeni_dizi

dizi1 = [1, 9, 3]
dizi2 = [4, 2, 8]
print(buyuk_sayilari_al(dizi1, dizi2))

#5
from datetime import datetime

def selamla(mesaj):
    saat = datetime.now().hour

    if mesaj.lower() == "merhaba":
        if 5 <= saat < 12:
            return "Günaydın 😊"
        elif 12 <= saat < 18:
            return "Tünaydın 😊"
        elif 18 <= saat < 22:
            return "İyi akşamlar 😊"
        else:
            return "İyi geceler 🌙"
    else:
        return "Lütfen 'merhaba' yazınız."

# Kullanım örneği
kullanici_mesaji = input("Mesajınızı yazın: ")
print(selamla(kullanici_mesaji))
#6
def ascii_karsilik(kelime):
    dizi = [ord(harf) for harf in kelime]
    return dizi

kelime = input("Kelime girin: ")
print(ascii_karsilik(kelime))
#7
def uc_harf_otele(cumle):
    sonuc = []
    for karakter in cumle:
        if karakter.isalpha():
            if karakter.islower():
                yeni = chr((ord(karakter) - ord('a') + 3) % 26 + ord('a'))
            else:
                yeni = chr((ord(karakter) - ord('A') + 3) % 26 + ord('A'))
            sonuc.append(yeni)
        else:
            sonuc.append(karakter)
    return sonuc

cumle = input("Cümle girin: ")
print(uc_harf_otele(cumle))
#8
def ortalama_karsilastir(dizi):
    ortalama = sum(dizi) / len(dizi)
    print(f"Ortalama: {ortalama:.2f}")
    for sayi in dizi:
        if sayi > ortalama:
            print(f"{sayi} --> ortalamanın ÜSTÜNDE")
        elif sayi < ortalama:
            print(f"{sayi} --> ortalamanın ALTINDA")
        else:
            print(f"{sayi} --> ortalamaya EŞİT")

dizi = [10, 20, 30, 40, 50]
ortalama_karsilastir(dizi)
#9
def en_kucuk_bul(dizi):
    en_kucuk = dizi[0]
    for sayi in dizi:
        if sayi < en_kucuk:
            en_kucuk = sayi
    print(f"En küçük eleman: {en_kucuk}")

dizi = [5, 3, 8, 1, 9]
en_kucuk_bul(dizi)
#10
def en_buyuk_bul(dizi):
    en_buyuk = dizi[0]
    for sayi in dizi:
        if sayi > en_buyuk:
            en_buyuk = sayi
    return en_buyuk

dizi = [5, 3, 8, 1, 9]
print(f"En büyük eleman: {en_buyuk_bul(dizi)}")
#11
import re

def url_kontrol(cumle):
    kelimeler = cumle.split()
    url_dizisi = []
    for kelime in kelimeler:
        if re.match(r'https?://[^\s]+', kelime):
            url_dizisi.append(kelime)
    return url_dizisi

cumle = input("Cümle girin: ")
print(url_kontrol(cumle))
#12import re

def en_uzun_en_kisa(paragraf):
    cumleler = re.split(r'[.!?]+', paragraf)
    cumleler = [c.strip() for c in cumleler if c.strip()]
    en_uzun = max(cumleler, key=len)
    en_kisa = min(cumleler, key=len)
    print(f"En uzun cümle: {en_uzun}")
    print(f"En kısa cümle: {en_kisa}")

paragraf = input("Paragraf girin: ")
en_uzun_en_kisa(paragraf)

#13

def gecenleri_kaydet(ogrenciler):
    ortalamalar = []
    for ad, soyad, vize, final in ogrenciler:
        ort = vize * 0.4 + final * 0.6
        ortalamalar.append(ort)

    genel_ort = sum(ortalamalar) / len(ortalamalar)

    with open("gecenler.txt", "w", encoding="utf-8") as dosya:
        for i, (ad, soyad, vize, final) in enumerate(ogrenciler):
            ort = ortalamalar[i]
            if ort >= genel_ort:
                dosya.write(f"{ad} {soyad} - Ortalama: {ort:.2f}\n")

    print("gecenler.txt oluşturuldu.")

ogrenciler = [
    ("Ali", "Yılmaz", 70, 80),
    ("Ayşe", "Kaya", 40, 50),
    ("Mehmet", "Demir", 90, 95),
]
gecenleri_kaydet(ogrenciler)
"""
#14

import random

def dns_bul(dosya_adi):

    dns_dizisi = []

    try:
        with open(dosya_adi, "r", encoding="utf-8") as dosya:

            for satir in dosya:

                sayi = random.randint(1, 255)

                if "şifre bu satır nolu sayıdadır." in satir:

                    dns_url = f"dns://{sayi}.{sayi}.{sayi}.{sayi}"
                    dns_dizisi.append(dns_url)

    except FileNotFoundError:
        print("Dosya bulunamadı!")

    return dns_dizisi


s=dns_bul(
    r"C:\Users\student\Desktop\sınıf 2\Betikdiller\anlayana.txt"
)
print(s)


sonuc = dns_bul(
    r"C:\Users\student\Desktop\sınıf 2\kodlarım\betikdiler\Bettikdiller_Python"
)

print(sonuc)

