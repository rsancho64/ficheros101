#! /usr/bin/python3

fich_ent = open('entrada.txt', 'r')

numRegistrosOK = 0
numRegistrosBAD = 0
actual = 0
lista_enteros = []

for linea in fich_ent:
    actual += 1 
    try:
        lista_enteros.append(int(linea))
        numRegistrosOK += 1
    except ValueError:
        numRegistrosBAD += 1 
        print(f"registro {actual} corrupto: {linea}")
        continue

print(f" registrosOK: {numRegistrosOK}")
print(f"registrosBAD: {numRegistrosBAD}")
print(lista_enteros)

fich_ent.close()


