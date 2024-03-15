def calcular_factorial(x):
    fact=1
    for i in range(1,x+1):
        fact *=i
    return fact

numero = int(input("Ingrese un numero entero no negativo:"))

if numero < 0:
    print("El numero debe ser no negativo.")
else:
    fact = calcular_factorial(numero)
    print(f"El factorial de {numero} es {fact}")
    