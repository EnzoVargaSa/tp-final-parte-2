from paquete.estadistica import calcular_maximo, calcular_minimo, calcular_promedio, contar_pares
from paquete.validaciones import es_primo

continuar = True
print("Bienvenido al sistema de inicio de sesión.")
nombre_usuario_creado = input("Ingrese su nombre de usuario: ")
contra_creada = input("Ingrese su contraseña: ")

nombre_usuario_ingresado = input("Ingrese su nombre de usuario para iniciar sesión: ")
contra_ingresada = input("Ingrese su contraseña para iniciar sesión: ")

contador = 1
lista = []

while continuar and (nombre_usuario_ingresado != nombre_usuario_creado or contra_ingresada != contra_creada) and contador < 3:
    print("Nombre de usuario o contraseña incorrectos. Intente nuevamente.")
    nombre_usuario_ingresado = input("Ingrese su nombre de usuario para iniciar sesión: ")
    contra_ingresada = input("Ingrese su contraseña para iniciar sesión: ")
    contador += 1
    if contador == 3:
        print("Ha excedido el número máximo de intentos. Su cuenta ha sido bloqueada.")
        continuar = False
    else:
        print("iniciaste sesión")


opcion = ""

while opcion != "f" and continuar:
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
        print("Tablas")

    elif opcion == "c":
        print("Variables")

    elif opcion == "d":
        print("Mostrar")
        print(lista)

    elif opcion == "e":
        if len(lista) == 0:
            print("Lista vacia, carga numeros en a)")
        else:
            print("--- ESTADISTICAS ---")
            maximo = calcular_maximo(lista)
            print("Maximo: ", maximo)

            minimo = calcular_minimo(lista)
            print("Minimo: ", minimo)

            promedio = calcular_promedio(lista)
            print("Promedio: ", promedio)

            cant_pares = contar_pares(lista)
            print("Cant pares: ", cant_pares)

            prom_entero = int(promedio)
            es_prom_primo = es_primo(prom_entero)
            print("Promedio es primo: ", es_prom_primo)

    elif opcion == "f":
        print("Saliendo...")

    else:
        print("Opcion incorrecta")