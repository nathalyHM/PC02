def obtener_mes_numero(mes):
    meses ={
        "Enero": "01","Febrero": "02","Marzo": "03","Abril": "04","Mayo": "05","Junio": "06","Julio": "07","Agosto": "08","Septiembre": "09","Octubre": "10","Noviembre": "11","Diciembre": "12"
    }
    return meses.get(mes.capitalize())

def convertir_fecha (fecha):
    if ',' in fecha:
     mes, dia_anio = fecha.split()
     dia, anio = dia_anio[:-1], dia_anio[-1]
     mes = obtener_mes_numero[mes]
    else:
        mes, dia, anio = fecha.split('/')


        mes = f"{ int(mes):02}"   
        mes = f"{int(dia):02}"

        return f"{anio} - {mes} - {dia}"

fecha_input = input("Ingrese la fecha (mes dia, AAAA o MM/DD/AAAA):")

fecha_convertida = convertir_fecha(fecha_input)
print("fecha convertida:", fecha_convertida)