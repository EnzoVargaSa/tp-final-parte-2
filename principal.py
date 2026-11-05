from paquete.estadistica import calcular_maximo, calcular_minimo, calcular_promedio, contar_pares, mostrar_estadisticas
from paquete.validaciones import es_primo, pedir_entero
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
    print("iniciaste sesión")

opcion = ""

while opcion != "f" and continuar:
    print("")
    print("a) proyectos")
    print("b) tablas")
    print("c) variables")
    print("d) mostrar")
    print("e) estadisticas")
    print("f) salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "a":
        num = int(input("Ingrese numero: "))
        lista.append(num)
        print(lista)

    elif opcion == "b":
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

    elif opcion == "c":
        if tabla is None:
            print("Primero tenes que crear una tabla en b)")
        else:
            modificar_tabla(tabla)

    elif opcion == "d":
        if tabla is None:
            print("Primero tenes que crear una tabla en b)")
        else:
            mostrar_tabla(tabla)

    elif opcion == "e":
        if tabla is None:
            print("Primero tenes que crear una tabla en b)")
        else:
            mostrar_estadisticas(tabla)

    elif opcion == "f":
        print("Saliendo...")

    else:
        print("Opcion incorrecta")