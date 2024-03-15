def omitir_vocales(cadena):
    cadena_sin_vocales = cadena.replace('a' , '').replace('e' ,'').replace('i' ,'').replace('o' ,'').replace('u' ,'')
    cadena_sin_vocales = cadena_sin_vocales.replace('A' , '').replace('E' , '').replace('I' , '').replace('O' , '').replace('U' , '')
    return cadena_sin_vocales

texto_original = input("Ingrese una cadena de texto:")

texto_modificado = omitir_vocales(texto_original)
print("Texto con las vocales omitidas:",texto_modificado)