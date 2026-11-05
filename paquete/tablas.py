from paquete.validaciones import pedir_entero, pedir_texto_no_vacio

def crear_tabla() -> dict:
    print("")
    print("--- CREAR TABLA - Punto b ---")
    cantidad_columnas: int = pedir_entero("Cuantas columnas tiene la tabla? ")
    columnas: list = []
    contador: int = 0
    while contador < cantidad_columnas:
        nombre: str = pedir_texto_no_vacio("Nombre de la columna: ")
        columnas.append(nombre)
        contador = contador + 1
    tabla: dict = {}
    tabla["columnas"] = columnas
    tabla["filas"] = []
    return tabla

def cargar_secuencial(tabla: dict) -> None:
    cantidad: int = pedir_entero("Cuantas filas queres cargar? ")
    contador_filas: int = 0
    while contador_filas < cantidad:
        print("")
        print("Fila numero ", contador_filas + 1)
        fila: dict = {}
        columnas: list = tabla["columnas"]
        contador_columnas: int = 0
        while contador_columnas < len(columnas):
            nombre_columna: str = columnas[contador_columnas]
            valor: str = pedir_texto_no_vacio(nombre_columna + ": ")
            fila[nombre_columna] = valor
            contador_columnas = contador_columnas + 1
        tabla["filas"].append(fila)
        contador_filas = contador_filas + 1

def cargar_distribuida(tabla: dict) -> None:
    cantidad: int = pedir_entero("Cuantas filas queres cargar? ")
    columnas: list = tabla["columnas"]
    contador_crear: int = 0
    while contador_crear < cantidad:
        fila_vacia: dict = {}
        contador_columnas: int = 0
        while contador_columnas < len(columnas):
            nombre_columna: str = columnas[contador_columnas]
            fila_vacia[nombre_columna] = ""
            contador_columnas = contador_columnas + 1
        tabla["filas"].append(fila_vacia)
        contador_crear = contador_crear + 1
    contador_columnas: int = 0
    while contador_columnas < len(columnas):
        nombre_columna: str = columnas[contador_columnas]
        print("")
        print("Cargando columna ", nombre_columna)
        contador_filas: int = 0
        while contador_filas < cantidad:
            valor: str = pedir_texto_no_vacio("Fila " + nombre_columna + ": ")
            tabla["filas"][contador_filas][nombre_columna] = valor
            contador_filas = contador_filas + 1
        contador_columnas = contador_columnas + 1

def modificar_tabla(tabla: dict) -> None:
    print("")
    print("1. Modificar una columna entera")
    print("2. Modificar una fila entera")
    opcion: int = pedir_entero("Elegi: ")
    if opcion == 1:
        columna_a_modificar: str = pedir_texto_no_vacio("Que columna queres modificar? ")
        existe: bool = False
        contador: int = 0
        while contador < len(tabla["columnas"]):
            if tabla["columnas"][contador] == columna_a_modificar:
                existe = True
            contador = contador + 1
        if existe == True:
            contador_filas: int = 0
            while contador_filas < len(tabla["filas"]):
                nuevo_valor: str = pedir_texto_no_vacio("Nuevo valor para " + columna_a_modificar + ": ")
                tabla["filas"][contador_filas][columna_a_modificar] = nuevo_valor
                contador_filas = contador_filas + 1
        else:
            print("Esa columna no existe")
    elif opcion == 2:
        numero_fila: int = pedir_entero("Que numero de fila? Empezando en 1: ")
        indice: int = numero_fila - 1
        if indice >= 0 and indice < len(tabla["filas"]):
            contador_columnas: int = 0
            while contador_columnas < len(tabla["columnas"]):
                nombre_columna: str = tabla["columnas"][contador_columnas]
                nuevo_valor: str = pedir_texto_no_vacio(nombre_columna + ": ")
                tabla["filas"][indice][nombre_columna] = nuevo_valor
                contador_columnas = contador_columnas + 1
        else:
            print("Fila inexistente")
    else:
        print("Opcion incorrecta")