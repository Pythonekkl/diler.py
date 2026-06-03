import random
A=int(input("Sayıyı giriniz "))
B=input("İkinci Sayıyı Giriniz ")
print(type(A))
print(type(B))
B=int(B)
C=A-B
if  C>0:
    print("A büyük Bden")
elif C<0:
    print("B büyük Adan")
elif C==0:
    print("Sayılar Eşittir")
else:
    print("HataLı sayi Girdiniz")
print("-----------------------------------------------------")
A=random.random()
B=random.random()
C=A-B
print(A)
print(B)
if  C>0:
    print("A büyük Bden")
elif C<0:
    print("B büyük Adan")
elif C==0:
    print("Sayılar Eşittir")
else:
    print("HataLı sayi Girdiniz")