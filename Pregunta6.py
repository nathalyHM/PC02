def fibonacci(maximo):
    numero1,numero2 = 0, 1
    serie_fibonacci = [numero1]

    while numero2 <= maximo:
        serie_fibonacci.append(numero2)
        numero1, numero2 = numero2, numero1+numero2
    return serie_fibonacci   

serie_hasta_50 = fibonacci(50)

print("Serie de fibonacci hasta 50:")
print(serie_hasta_50)