f=open("turkmenistan.txt",'r',encoding="utf-8")
print(f.read())
## with open("turkmenistan.txt","a") as f:
    ##f.write("Nasiba")
try:
    f=open("Turkmen.txt","x",encoding="utf-8")
except FileExistsError:              
    print("file exists")

names=['eren', 'nasiba', 'guncha', 'gulsenem', 'ırmak']

with open("Turkmen.txt","w",encoding="utf-8") as yazma:
    for i in names:
        yazma.write(i+"\n")