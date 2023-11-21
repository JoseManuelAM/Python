# Función Login: Recibe un nombre de usuario y una contraseña, y devuelve un
# valor lógico: verdadero si se ha introducido el nombre y la contraseña adecuadas (usuario1,asdf).
# Además devuelve el numero de internos 
# Parámetros de entrada: nombre y contraseña, y el número de intentos actual
# Datos devueltos: Valor lógico indicando si ha hecho login, e intentos

def login(nombre, password, intentos):
    if nombre == "usuario1" and password == "asdf":
        return True, intentos
    else:
        return False, intentos


# Crear un programa principal donde se pida un nombre de usuario y una contraseña 
# y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.

intentos = 0
print("Dispone de 3 intentos para iniciar sesión.")

while True:
    intentos+=1
    nombre = input("Introduzca el nombre de usuario: ")
    password = input("Introduzca la contraseña: ")
    estadoLogin, intentos = login(nombre, password, intentos)
    print(login(nombre, password, intentos))
    if estadoLogin == False:
        print("Acceso denegado. Intentos restantes: ", 3-intentos)
    if intentos>=3 or estadoLogin == True:
        break
    
if estadoLogin == True:
    print("Acceso permitido") 