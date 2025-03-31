import math
import random

def derivada(lista: list, paso: float):
    """
    Función que calcula la derivada numerica de una lista de números
    ________________________________________________________________
    Parametros:

    * lista: Lista de numeros que representa la función matemática
    
    * paso: tamaño de paso entre dos valores consecutivos de la lista
    """
    d = []
    d.append((lista[1] - lista[0]) / paso)
    for i in range(1, len(lista) - 1):
        d.append((lista[i + 1] - lista[i - 1]) / (2 * paso))
    d.append((lista[-1] - lista[-2]) / paso)
    
    return d

def muestra(inf, sup, n):
    return random.sample(list(range(inf, sup)), n)