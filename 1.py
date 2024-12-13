#! /usr/bin/python3

fich_ent = open('entrada.txt', 'r')

numRegistros = 0
lista_enteros = []

for linea in fich_ent:
    numRegistros += 1
    try:
        lista_enteros.append(int(linea))
    except ValueError:
        print("detectada corrupcion en el fichero")
        exit()
    # print(f"registro: {linea}")

print(f"numero de registros: {numRegistros}")
print(lista_enteros)

fich_ent.close()


