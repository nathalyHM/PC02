numero_divisibles = []
for numero in range(1500,2701):
    if numero % 7 == 0 and numero % 5 == 0:
        numero_divisibles.append(numero)

        print("los numeros divisibles por 7 y multiplos de 5, en el rango de 1500 a 2700 son:")
        print(numero_divisibles)
        
