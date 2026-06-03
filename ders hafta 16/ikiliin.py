def ikilinn(sayi):
    if sayi==0: 
        return  0
    else:
        return sayi+ikilinn(sayi-2)
print(ikilinn(100))