import random

numerointentos=0
nummin=1
nummax=10

print("Cual es su nombres?: ")
username=input()

number= random.randint(nummin, nummax)
print("Hola, " + username + ". Estoy pensando en un numero del "  + str(nummin) +  " and " + str(nummax))

while numerointentos < 4:
    print("Adivina:")
    guess= input()
    guess=int(guess)

    numerointentos= numerointentos + 1

    if guess < number:
        print("Tu numero es bajo")
    if guess > number:
        print("Tu numero es alto")
    if guess == number:
        break

if guess == number:
    numerointentos= str(numerointentos)
    print("Buen trabajo " +  username + " Has adivinado el numero en " + numerointentos + " intentos")

if guess!= number:
    number=str(number)
    print("No, el numero que pense era"+ number)