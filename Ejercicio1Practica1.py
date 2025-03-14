print("programa_1")
edad=input()
faltan_100=100-int(edad)
if 0<=faltan_100<=100 :  
    print("Te faltan " + str(int(faltan_100)) + " anios para cumplir 100 anios")
else:
    print("¡Ya cumpliste 100 anios!")
