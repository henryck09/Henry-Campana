import random
numero=random.randint(1, 10)
intentos=4
for i in range(intentos):
    intento=int(input("Bienvenido, adivina el numero:" ))
    if intento<numero:
        print("El numero es mayor")
    elif intento>numero:
        print("El numero es menor")
    else:
        print("Adivinaste")
        break
else:
    print(f"Incorrecto, el numero era {numero}")