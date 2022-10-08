#19 Una distribuidora de libros vende a librerías y a particulares. Aplica bonificaciones por cantidad según el
#siguiente criterio:

#  i.      a librerías: hasta 24 unidades, el 20%; más de 24 unidades, el 25%.

#  ii.      a particulares: menos de 6 unidades, nada; desde 6 hasta 18 unidades, el 5% y más de 18 unidades, el 10%.

#El tipo de cliente está codificado así: 'L' para librerías, 'P' para particular.
# Dado el importe bruto de una compra de libros, el tipo de cliente de que se trata y
# la cantidad total pedida por el mismo, determinar el importe bruto bonificado.

tipo = str(input('Ingrese tipo de cliente: \n L - Librerias \n P - Particular \n'))

if tipo.lower() =='l' or 'p':
    importe = float(input('Ingrese importe bruto de la compra \n $'))
    unidades = int(input('Ingrese numero de unidades para vender \n'))

    if tipo.lower() == 'l':
        if unidades <= 24:
            total = (importe * 0.80)
        elif unidades > 24:
            total = (importe * 0.75)
    elif tipo.lower() == 'p':
        if unidades < 6:
            total = importe
        if (unidades >= 6) and (unidades <= 18):
            total = (importe * 0.95)
        if unidades > 18:
            total = (importe * 0.90)

    print ('El importe  bruto bonificado es de: $',format(total,'.2f'))

else:
    print('Ingrese tipo válido')