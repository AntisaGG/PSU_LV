print("Molim unesite prosjek")
while(1):
    temp = input()
    try:
        prosjek = float(temp)
        break
    except:
        print("Molim unesite broj")
    
if(prosjek<0.6 and prosjek >=0):
    print("F")
elif(prosjek>=0.6 and prosjek<0.7):
    print("D")
elif(prosjek>=0.7 and prosjek<0.8):
    print("C")
elif(prosjek>=0.8 and prosjek<0.9):
    print("B")
elif(prosjek>=0.9 and prosjek<=1):
    print("A")
else:
    print("Niste unjeli broj iz intervala 0.0-1.0")


