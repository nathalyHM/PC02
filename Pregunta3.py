
numeros_ingresados = []


while True:
     respuesta = input("¿Desea ingresar un numero?:")

     if respuesta == 'SI':
    
        try:
            numero = int(input("Ingrese un numero:"))
            numeros_ingresados.append(numero)
        except ValueError:
            print("Error ingreso un numero invalido.")
     elif respuesta == 'NO':
          break



numeros_pares = [num for num in numeros_ingresados if num % 2 == 0]
numeros_impares = [num for num in numeros_ingresados if num % 2 != 0]

print("numeros ingresados :",numeros_ingresados)
print(f"Numeros pares ingresados:{len(numeros_pares)}")
print(f"Numeros impares ingresados:{len(numeros_impares)}")
    

