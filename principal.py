from paquete.estadistica import mostrar_estadisticas
from paquete.validaciones import pedir_entero, verificar_tabla
from paquete.tablas import crear_tabla, cargar_secuencial, cargar_distribuida, modificar_tabla
from paquete.visualizacion import mostrar_tabla

continuar = True
print("Bienvenido al sistema de inicio de sesión.")
nombre_usuario_creado = input("Ingrese su nombre de usuario: ")
contra_creada = input("Ingrese su contraseña: ")

nombre_usuario_ingresado = input("Ingrese su nombre de usuario para iniciar sesión: ")
contra_ingresada = input("Ingrese su contraseña para iniciar sesión: ")

contador = 1
lista = []
tabla = None

while continuar and (nombre_usuario_ingresado != nombre_usuario_creado or contra_ingresada != contra_creada):
    print("Nombre de usuario o contraseña incorrecto. Intente nuevamente.")
    nombre_usuario_ingresado = input("Ingrese su nombre de usuario para iniciar sesión: ")
    contra_ingresada = input("Ingrese su contraseña para iniciar sesión: ")
    contador += 1
    if contador == 3:
        print("Ha excedido el número máximo de intentos. Su cuenta ha sido bloqueada")
        continuar = False
else:
    if continuar:
        print("Iniciaste sesión")

opcion = ""

while opcion != "f" and opcion != "F" and continuar:
    print("")
    print("a) proyectos")
    print("b) tablas")
    print("c) variables")
    print("d) mostrar")
    print("e) estadisticas")
    print("f) salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "a" or opcion == "A":
        num = pedir_entero("Ingrese numero: ")
        lista.append(num)
        print(lista)

    elif opcion == "b" or opcion == "B":
        print("ENTRASTE A TABLAS")
        tabla = crear_tabla()
        print("1. Secuencial")
        print("2. Distribuida")
        tipo = pedir_entero("Elegi tipo de carga: ")
        if tipo == 1:
            cargar_secuencial(tabla)
        elif tipo == 2:
            cargar_distribuida(tabla)
        else:
            print("Opcion incorrecta")

    elif opcion == "c" or opcion == "C":
        if verificar_tabla(tabla):
            modificar_tabla(tabla)

    elif opcion == "d" or opcion == "D":
        if verificar_tabla(tabla):
            mostrar_tabla(tabla)

    elif opcion == "e" or opcion == "E":
        if verificar_tabla(tabla):
            mostrar_estadisticas(tabla)

    elif opcion == "f" or opcion == "F":
        print("Saliendo...")

    else:
        print("Opcion incorrecta")