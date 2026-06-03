import random
a=random.randint(1,10)
b=random.randint(1,10)
if a%2==0 and b%2==0:
    print("Tüm Sayılar Çift")
elif a%2!=0 and b%2!=0:
    print("Tüm Sayılar Tektir")    
elif a%2==0 and b%2!=0:            
    print("A Çift B Tektir")
elif a%2!=0 and b%2==0:
    print("A Tek B Çifttir")
else:
    print("ÖnGörülmeyenSonuç")
//bazarbayew
