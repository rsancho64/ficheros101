#! /usr/bin/python3

fich_ent = open('entrada.txt', 'r')

numRegistros = 0
for linea in fich_ent:
    numRegistros += 1
    print(f"registro: {linea}")

print(f"numero de registros: {numRegistros}")
fich_ent.close()