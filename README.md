# ficheros 101

Empezamos a ver el concepto de **fichero**.

material majo de [ficheros con python](https://www2.eii.uva.es/fund_inf/python/notebooks/10_Ficheros/Ficheros.html)

## jerarquia clásica de volumen de informacion en computacion

**bit** (binary digit)
    **byte** (octeto) (de bits) ~ sucesion de 8 bits
        **campo** ~ palabra ~ aspecto de i ~ sucesion de bytes
            **registro** ~ sucesion de campos
                **fichero** ~ sucesion de registros

## Terminologia

EOT: END OF Text/Transmission (a char)
EOF: END OF FILE (a char)

## ejercicios

1. hacer que el generador admita como parametro en linea de comando el numero de tiradas, que no sean siempre 20

2. programar un procesador que partiendo de la lista ([]) indique los valores máximo, minimo, medio y modal

- [ ] moda está en un paquete estadistico de python?
- [ ] existe un paquete estadistico de python?

3. programa de registros y campos de tamaño variable.

- [ ] 2: escritura:
    creo el fichero
    meto tres registros de tamaño variable, indicados con centinela
    cierro el fichero

datos en "amigos"

- [ ] 1: lectura
    abro el fichero
    leo registros de tamaño variable, indicados con centinela
    cierro el fichero
