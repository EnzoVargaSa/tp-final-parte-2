def calcular_ancho_columna(tabla: dict, nombre_columna: str) -> int:
    ancho_maximo: int = len(nombre_columna)
    contador_filas: int = 0
    while contador_filas < len(tabla["filas"]):
        valor: str = tabla["filas"][contador_filas][nombre_columna]
        if len(valor) > ancho_maximo:
            ancho_maximo = len(valor)
        contador_filas = contador_filas + 1
    return ancho_maximo

def mostrar_tabla(tabla: dict) -> None:
    columnas: list = tabla["columnas"]
    filas: list = tabla["filas"]
    anchos: list = []
    contador_columnas: int = 0
    while contador_columnas < len(columnas):
        nombre_columna: str = columnas[contador_columnas]
        ancho: int = calcular_ancho_columna(tabla, nombre_columna)
        anchos.append(ancho)
        contador_columnas = contador_columnas + 1
    encabezado: str = "| "
    contador: int = 0
    while contador < len(columnas):
        nombre_columna: str = columnas[contador]
        encabezado = encabezado + nombre_columna
        espacios: int = anchos[contador] - len(nombre_columna)
        contador_espacios: int = 0
        while contador_espacios < espacios:
            encabezado = encabezado + " "
            contador_espacios = contador_espacios + 1
        encabezado = encabezado + " | "
        contador = contador + 1
    print(encabezado)
    separador: str = ""
    contador: int = 0
    while contador < len(encabezado):
        separador = separador + "-"
        contador = contador + 1
    print(separador)
    contador_filas: int = 0
    while contador_filas < len(filas):
        linea: str = "| "
        contador_columnas: int = 0
        while contador_columnas < len(columnas):
            nombre_columna: str = columnas[contador_columnas]
            valor: str = filas[contador_filas][nombre_columna]
            linea = linea + valor
            espacios: int = anchos[contador_columnas] - len(valor)
            contador_espacios: int = 0
            while contador_espacios < espacios:
                linea = linea + " "
                contador_espacios = contador_espacios + 1
            linea = linea + " | "
            contador_columnas = contador_columnas + 1
        print(linea)
        contador_filas = contador_filas + 1