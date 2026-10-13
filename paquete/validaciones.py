def validar_rango(valor: float, minimo: float = 1, maximo: float = 10) -> bool:
    validez: bool = True
    if valor < minimo or valor > maximo:
        validez = False
    return validez

def es_par(valor: int) -> bool:
    validez: bool = False
    if valor % 2 == 0:
        validez = True
    return validez

def es_primo(valor: int, divisor: int = 2) -> bool:
    validez: bool = True
    if valor < 2:
        validez = False
    elif divisor * divisor > valor:
        validez = True
    elif valor % divisor == 0:
        validez = False
    else:
        validez = es_primo(valor, divisor + 1)
    return validez

def es_multiplo(valor1: int, valor2: int) -> bool:
    validez: bool = False
    if valor2!= 0:
        if valor1 % valor2 == 0:
            validez = True
    return validez

def validar_nota(valor: float) -> bool:
    validez: bool = False
    if valor >= 1 and valor <= 10:
        validez = True
    return validez