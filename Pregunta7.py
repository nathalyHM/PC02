def es_primo(numero):
    if numero <= 1:
        return False
    
    for divisor in range(2, numero // 2+1):
        if numero % divisor == 0:
            return False
    return True

numero = int(input("Ingrese un numero para verificar si es primo:"))

if es_primo(numero):
    print(f"{numero} es un numero primo.")
else:
    print(f"{numero} no es un numero primo.")    
