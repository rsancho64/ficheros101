#! /usr/bin/python3

import random

def tirada() -> int :
    """Simula una tirada de dos dados"""
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2

def generar_fichero(nombre_fichero, num_tiradas):
    """Genera un fichero con tiradas de dados"""
    with open(nombre_fichero, "w") as fichero:
        for _ in range(num_tiradas):
            fichero.write(str(tirada()) + "\n")

# Generar el fichero entrada.txt con 20 tiradas de dados
generar_fichero("entrada.txt", 20)