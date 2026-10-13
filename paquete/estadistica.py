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