#3 Determinar si el primero de un conjunto de tres números dados, es menor que los otros dos.

nro1 = int(input('Ingrese n1 \n'))
nro2 = int(input('Ingrese n2 \n'))
nro3 = int(input('Ingrese n3 \n'))

if nro1 < nro2:
    if nro1 < nro3:
        print('El primer numero ingresado es el menor.\n')
    else:
        print('El primer numero ingresado no es menor que los otros dos.\n1')
elif nro1 < nro3:
    if nro1 < nro2:
        print('El primer numero ingresado es el menor. \n')
    else:
        print('El primer numero ingresado no es menor que los otros dos.\n1')
else:
    print('El primer numero ingresado no es menor que los otros dos.\n1')