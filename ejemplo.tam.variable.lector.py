#! /usr/bin/python3
"""
*** fichero "amigos" (ascii ~ txt)
lectura
    abro el fichero
    leo registros de tamaño variable, indicados con centinela
    cierro el fichero
"""    

file = open('amigos', 'r')

record = []
field = []
while True:
    char = file.read(1)
    if not char:  # EOF
        break
    if char == '#':
        print(record)
        # print("".join(field))
        print("#")
        record = []
    if char == '|':
        print(field) 
        # print("".join(field))
        print("|")
        field = []
    else:
        field.append(char)
        # print(char, end="")

file.close()
