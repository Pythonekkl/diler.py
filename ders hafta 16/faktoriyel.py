def faktor(sayi):
    if sayi == 1:
        return sayi
    else:
        return sayi * faktor(sayi - 1)
def faktor2(sayi):
    faktor=1       
    for i in range(sayi,0,-1):
        faktor=faktor*i
    return faktor
print(faktor(6))
print(faktor2(6))

