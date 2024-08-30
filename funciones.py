def sumar (num1=3, num2=4):
    resultado=num1+num2
    return resultado
print(sumar(3, 4))

def saludar():
    print ("Hola")
saludar()

def multiplicar(n1, n2):
    resultado=n1*n2
    return resultado
print(multiplicar(8,5))

def calcularIMC(peso, altura):
    imc=peso/(altura**2)
    return imc
print(calcularIMC(80, 1.80))

def Calcularmaxmin(lista):
    return(max(lista), min(lista))
valmax, valmin=Calcularmaxmin([5,1,3,6,4,2,7,8,9])
print("El valor maximo es", valmax)
print("El valor minimo es", valmin)

def Arec(lado,altura):
    return lado*altura
print("El area es:", Arec(5,10))
   


