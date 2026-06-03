import random
kurban_listesi=['a','b','c','d','e','f']
kl=kurban_listesi
kurban_listesi=kurban_listesi
def rus_ruletimiz(kl=6,sayac=1,r=random.randint(1,6)):
    print("ss subayı silahını çıkardı ve rus ruleti için hazırladı.")
    print(f"{sayac}. kişinin o an ölme ihtimali={1/kl}")
    print(f"{sayac}. kişinin genel ölme ihtimali={1/kl*kl/6}'di")
    
    if r==sayac:
        print(f"boom ..... {sayac}.kişi öldü")
        return sayac
    #yoksa rus_ruleti()
    else:
        print(f"Tıkk {sayac}. kişi kurtuldu sıra {sayac + 1}.Kişide")
        return rus_ruletimiz(kl-1,sayac+1,r)
rus_ruletimiz()




