edad=int(input("Ingrese su edad:"))

if edad>0 and edad<100:
    print ("Edad Correcta")
    if edad>=18:
        print("Usted es mayor de edad")
    if edad<18:
        print("Usted es menor de edad")
else:
    print("Edad Incorrecta")