from trc import *
satır=0
for bilgi in bilgiler:          
    satır+=1
    print(satır)
    try:
        print(bilgi["status"])
    except KeyError:
        pass