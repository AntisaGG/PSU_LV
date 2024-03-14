numarr = []
counter=0
suma=0
while(1):
    var = input()
    if(var=='Done'):
        break
    elif(var.isdigit() != True):
        print("Niste unjeli broj.")
        break
    else:
        numarr.append(float(var))
        suma+=float(var)
        counter+=1


numarr.sort()
print(numarr)
print("Srednja vrijednost je :",suma/counter)
print("Maksimalna vrijednost je: ",max(numarr))
print("Minimalna vrijednost je: ",min(numarr))