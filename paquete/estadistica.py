def calcular_maximo(tabla: dict):
    maximo = None
    contador_filas: int = 0
    while contador_filas < len(tabla["filas"]):
        contador_columnas: int = 0
        while contador_columnas < len(tabla["columnas"]):
            nombre_columna: str = tabla["columnas"][contador_columnas]
            valor: str = tabla["filas"][contador_filas][nombre_columna]
            numero: int = int(valor)
            if maximo is None or numero > maximo:
                maximo = numero
            contador_columnas = contador_columnas + 1
        contador_filas = contador_filas + 1
    return maximo

def calcular_minimo(tabla: dict):
    minimo = None
    contador_filas: int = 0
    while contador_filas < len(tabla["filas"]):
        contador_columnas: int = 0
        while contador_columnas < len(tabla["columnas"]):
            nombre_columna: str = tabla["columnas"][contador_columnas]
            valor: str = tabla["filas"][contador_filas][nombre_columna]
            numero: int = int(valor)
            if minimo is None or numero < minimo:
                minimo = numero
            contador_columnas = contador_columnas + 1
        contador_filas = contador_filas + 1
    return minimo

def calcular_promedio(tabla: dict):
    suma: int = 0
    cantidad: int = 0
    contador_filas: int = 0
    while contador_filas < len(tabla["filas"]):
        contador_columnas: int = 0
        while contador_columnas < len(tabla["columnas"]):
            nombre_columna: str = tabla["columnas"][contador_columnas]
            valor: str = tabla["filas"][contador_filas][nombre_columna]
            numero: int = int(valor)
            suma = suma + numero
            cantidad = cantidad + 1
            contador_columnas = contador_columnas + 1
        contador_filas = contador_filas + 1
    if cantidad == 0:
        return 0
    return suma / cantidad

def contar_pares(tabla: dict):
    cantidad_pares: int = 0
    contador_filas: int = 0
    while contador_filas < len(tabla["filas"]):
        contador_columnas: int = 0
        while contador_columnas < len(tabla["columnas"]):
            nombre_columna: str = tabla["columnas"][contador_columnas]
            valor: str = tabla["filas"][contador_filas][nombre_columna]
            numero: int = int(valor)
            if numero % 2 == 0:
                cantidad_pares = cantidad_pares + 1
            contador_columnas = contador_columnas + 1
        contador_filas = contador_filas + 1
    return cantidad_pares

def mostrar_estadisticas(tabla: dict):
    print("Maximo: ", calcular_maximo(tabla))
    print("Minimo: ", calcular_minimo(tabla))
    print("Promedio: ", calcular_promedio(tabla))
    print("Cantidad de pares: ", contar_pares(tabla))