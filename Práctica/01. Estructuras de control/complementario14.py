#14 Leer 2 números; si son iguales que los multiplique, 
#si el primero es mayor que el segundo que los reste y si no que los sume.

nro1 = int(input('Ingrese nro1 \n'))
nro2 = int(input('Ingrese nro2 \n'))

if nro1 == nro2:
    print(nro1*nro2)
elif nro1 > nro2:
    print(nro1-nro2)
else:
    print(nro1+nro2)

