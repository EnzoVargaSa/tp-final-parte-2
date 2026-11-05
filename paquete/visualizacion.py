def completar_con_espacios(texto: str, ancho: int) -> str:
    resultado = texto
    while len(resultado) < ancho:
        resultado = resultado + " "
    return resultado

def calcular_ancho_columna(tabla: dict, nombre_columna: str) -> int:
    ancho_maximo: int = len(nombre_columna)
    contador_filas: int = 0
    while contador_filas < len(tabla["filas"]):
        valor: str = str(tabla["filas"][contador_filas][nombre_columna])
        if len(valor) > ancho_maximo:
            ancho_maximo = len(valor)
        contador_filas = contador_filas + 1
    return ancho_maximo

def mostrar_tabla(tabla: dict) -> None:
    columnas: list = tabla["columnas"]
    filas: list = tabla["filas"]
    anchos: list = []
    contador: int = 0
    while contador < len(columnas):
        anchos.append(calcular_ancho_columna(tabla, columnas[contador]))
        contador = contador + 1

    encabezado: str = "| "
    contador = 0
    while contador < len(columnas):
        nombre_columna: str = columnas[contador]
        encabezado = encabezado + completar_con_espacios(nombre_columna, anchos[contador]) + " | "
        contador = contador + 1
    print(encabezado)

    separador: str = ""
    contador = 0
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
            valor: str = str(filas[contador_filas][nombre_columna])
            linea = linea + completar_con_espacios(valor, anchos[contador_columnas]) + " | "
            contador_columnas = contador_columnas + 1
        print(linea)
        contador_filas = contador_filas + 1