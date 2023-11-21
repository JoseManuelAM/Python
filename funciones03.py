# Función Intercambiar: Recibe dos números como parámetros de entrada y 
#  devuelve los números ordenador de mayor a menor
# Parámetros de entrada: dos números
# Datos de salida: dos números

def Intercambiar(n1, n2):
    if n2>n1:
        return n2, n1
    else:
        return n1, n2

# Función CalcularMCD: Recibe dos números y devuelve el MCD utilizando el método 
# de Euclides. El método de Euclides es el siguiente:
#  * Se divide el número mayor entre el menor.
#  * Si la división es exacta, el divisor es el MCD.
#  * Si la división no es exacta, dividimos el divisor entre el resto obtenido y 
# se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
# Parámetros de entrada: dos números
# Dato devuelto: El MCD

def CalcularMCD(n1, n2):
    aux = 0
    while n2 != 0:
        aux = n2
        n2 = n1%n2
        n1 = aux
    return n1


# Función LeerFracion: Lee por teclado una fracción (numerador y denominador)
#  y lo devuelve como parámetro de entrada y salida.
# Esta función usa SimplificarFraccion para simplificar la fracción leída.
# Datos devueltos: numerador y denominador 



# Función SimplificarFracion: Recibe una fracción (numerador y denominador)
#  y lo devuelve la fracción simplificada como parámetro ed entrada y salida.
# Para simplificar hay que dividir numerador y dominador por el MCD del numerador 
# y denominador. 
# Datos devueltos: numerador y denominador 



# Función EscribirFracion: Recibe una fracción (numerador y denominador)
#  y lo muestra por pantalla. Muestra numerador partido por denominador. Si el
# denominador es 1 sólo muestra el numerador.
# Parámetros de entrada: numerador y denominador 


	
# Función SumarFracciones: Recibe dos fracciones (numerador y denominador)
#  y devuelve otra fracción que es la suma de la primera y la segunda.
# La suma de dos fracciones es otra fracción cuyo `numerador=n1*d2+d1*n2` 
# y `denominador=d1*d2`.
# Este Función usa SimplificarFraccion para simplificar la fracción calculada.
# Parámetros de entrada: numerador1 y denominador1, numerador2 y denominador2
# Datos devueltos: numerador y denominador de la fracción resultado



# Función RestarFracciones: Recibe dos fracciones (numerador y denominador)
#  y devuelve otra fracción que es la resta de la primera y la segunda.
# La resta de dos fracciones es otra fracción cuyo `numerador=n1*d2-d1*n2` 
# y `denominador=d1*d2`.
# Este Función usa SimplificarFraccion para simplificar la fracción calculada.
# Parámetros de entrada: numerador1 y denominador1, numerador2 y denominador2
# Datos devueltos: numerador y denominador de la fracción resultado



# Función MultiplicarFracciones: Recibe dos fracciones (numerador y denominador)
#  y devuelve otra fracción que es el producto de la primera y la segunda.
# La resta de dos fracciones es otra fracción cuyo `numerador=n1*n2` 
# y `denominador=d1*d2`
# Este Función usa SimplificarFraccion para simplificar la fracción calculada.
# Parámetros de entrada: numerador1 y denominador1, numerador2 y denominador2
# Datos devueltos: numerador y denominador de la fracción resultado



# Función DividirFracciones: Recibe dos fracciones (numerador y denominador)
#  y devuelve otra fracción que es la división de la primera y la segunda.
# La resta de dos fracciones es otra fracción cuyo `numerador=n1*d2` 
# y `denominador=d1*n2`
# Este Función usa SimplificarFraccion para simplificar la fracción calculada.
# Parámetros de entrada: numerador1 y denominador1, numerador2 y denominador2
# Datos devueltos: numerador y denominador de la fracción resultado



# Crear un programa que utilizando las funciones anteriores muestre un menú para 
# operar con fracciones.