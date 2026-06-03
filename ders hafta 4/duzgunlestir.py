def duzgunlestir(arr):
    for i in arr:
        x=(i.split("-"))
        isim=''
        for parca in x:
            isim+=(parca.strip()) #boşluk siler.
        print("======")
        print(isim)


iller=['Anka- ra','istan- bul','iz- mir','bur - sa','kay- seri','çan -    kal - e','Bu - rak- kod -ladı ']
duzgunlestir(iller)