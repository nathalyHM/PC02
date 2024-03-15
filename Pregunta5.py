def contar_digitos(numero,digito):
    str_numero = str(numero)
    cantidad = str_numero.count(str(digito))
    return cantidad

numero_ingresado = int(input("Ingrese un numero entero:"))
digito_ingresado = int(input("Ingrese un digito a contar:"))

cantidad_digitos = contar_digitos(numero_ingresado,digito_ingresado)

print(f"Cantidad de veces {digito_ingresado} en el numero {numero_ingresado}: {cantidad_digitos} ")
