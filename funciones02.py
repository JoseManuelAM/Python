# Función Convertir_A_Segundos: Recibe una cantidad de horas, minutos y segundos 
# y calcula a cuantos segundos corresponde.
# Parámetros de entrada: hora, minutos y segundos
# Dato devuelto: Segundos totales

def Convertir_A_Segundos(hh, mm, ss):
    horaSegundo = hh*3600
    minutoSegundo = mm*60
    segundosTotales = horaSegundo+minutoSegundo+ss
    return segundosTotales

# Función Convertir_A_HMS: Recibe una cantidad de segundos y debe calcular a 
# que hora, minutos y segundos corresponde 
# Parámetros de entrada: segundos
# Valores de salida: hora,minutos y segundos

def Convertir_A_HMS(segundos):
    horas = 0
    minutos = 0
    while segundos>=3600:
        horas+=1
        segundos-=3600
    while segundos>=60:
        minutos+=1
        segundos-=60
    return horas, minutos, segundos

# Escribe un programa principal con un menú donde se pueda elegir la opción de 
# convertir a segundos, convertir a horas,minutos y segundos o salir del programa.

while True:
    print("\n********************** MENÚ **********************")
    print("1. Convertir a segundos")
    print("2. Convertir a horas, minutos y segundos")
    print("0. SALIR")
    opcion = (int)(input("Introduzca una opción: "))

    if opcion==1:
        horas = (int)(input("Introduzca las horas: "))
        minutos = (int)(input("Introduzca los minutos: "))
        segundos = (int)(input("Introduzca los segundos: "))
        conversionSegundos = Convertir_A_Segundos(horas, minutos, segundos)
        print("Tiempo en segundos:", conversionSegundos)
    elif opcion==2:
        segundos = (int)(input("Introduzca los segundos: "))
        conversionHoras, conversionMinutos, conversionSegundos = Convertir_A_HMS(segundos)
        print("Son", conversionHoras, "horas,", conversionMinutos,"minutos y", conversionSegundos, "segundos")
    elif opcion==0:
        break
    else:
        print("La opción introducida no es correcta.")