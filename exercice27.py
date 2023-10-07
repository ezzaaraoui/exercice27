nombre=int(input("Donner un nombre SVP : "))

while nombre<=0 :
    nombre=int(input("Donner un nombre SVP (positif non null): "))

somme=0

for i in range(1,nombre+1):
    if nombre % i ==0 :
        print(i)
    
