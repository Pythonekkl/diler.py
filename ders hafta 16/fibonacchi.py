def fibonacci(sayi):
    if sayi <=1:
        return 1
    else:
        return fibonacci(sayi-1)+fibonacci(sayi-2)
print(fibonacci(19))
def fibo2(sayi)
    yeni=1
    eski=0
    sayi+=1
    for i in range(2,sayi):
        print(f"{i-1}. Değeri:{yeni}")
        c=yeni
        yeni+=eski
        eski=c
    return yeni
print(fibo2(20))