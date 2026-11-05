def calcular_maximo(lista: list) -> int:
    maximo: int = lista[0]
    for valor in lista:
        if valor > maximo:
            maximo = valor
    return maximo

def calcular_minimo(lista: list) -> int:
    minimo: int = lista[0]
    for valor in lista:
        if valor < minimo:
            minimo = valor
    return minimo

def calcular_promedio(lista: list) -> float:
    acumulador: int = 0
    contador: int = 0
    promedio: float = 0.0
    for valor in lista:
        acumulador += valor
        contador += 1
    if contador!= 0:
        promedio = acumulador / contador
    return promedio

def contar_pares(lista: list) -> int:
    cantidad: int = 0
    for valor in lista:
        if valor % 2 == 0:
            cantidad += 1
    return cantidad

def extraer_columna_numerica(tabla: dict, nombre_columna: str) -> list:
    valores: list = []
    filas: list = tabla["filas"]
    for fila in filas:
        texto: str = fila[nombre_columna]
        numero: int = int(texto)
        valores.append(numero)
    return valores

def mostrar_estadisticas(tabla: dict) -> None:
    print("")
    print("--- ESTADISTICAS - Punto e ---")
    print("Columnas disponibles: ")
    columnas: list = tabla["columnas"]
    for columna in columnas:
        print("- " + columna)
    nombre_columna: str = input("Que columna numerica queres analizar? ")
    existe: bool = False
    for columna in columnas:
        if columna == nombre_columna:
            existe = True
    if existe == True:
        valores: list = extraer_columna_numerica(tabla, nombre_columna)
        maximo: int = calcular_maximo(valores)
        minimo: int = calcular_minimo(valores)
        promedio: float = calcular_promedio(valores)
        cantidad_pares: int = contar_pares(valores)
        print("")
        print("Columna analizada: " + nombre_columna)
        print("Maximo: " + str(maximo))
        print("Minimo: " + str(minimo))
        print("Promedio: " + str(promedio))
        print("Cantidad de pares: " + str(cantidad_pares))
    else:
        print("Esa columna no existe")