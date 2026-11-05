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

def pedir_entero(mensaje: str) -> int:
    texto: str = input(mensaje)
    validez: bool = True
    if texto == "":
        validez = False
    else:
        i: int = 0
        while i < len(texto):
            caracter: str = texto[i]
            if caracter < "0" or caracter > "9":
                if i == 0 and caracter == "-":
                    validez = True
                else:
                    validez = False
            i = i + 1
    if validez == True:
        numero: int = int(texto)
        return numero
    else:
        print("Error, tenes que ingresar un numero entero.")
        return pedir_entero(mensaje)

def pedir_texto_no_vacio(mensaje: str) -> str:
    texto: str = input(mensaje)
    validez: bool = False
    if texto != "":
        validez = True
    if validez == True:
        return texto
    else:
        print("Error, no podes dejar vacio.")
        return pedir_texto_no_vacio(mensaje)

def verificar_tabla(tabla) -> bool:
    if tabla is None:
        print("Primero tenes que crear una tabla en b)")
        return False
    return True