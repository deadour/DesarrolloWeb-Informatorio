#7 Un comercio ofrece un descuento del 15% sobre el total de la compra si esta supera los $1000.
# Obtenga para determinado cliente cuánto deberá pagar finalmente por su compra y el descuento obtenido,
# si es que corresponde.

importe = float(input('Ingrese importe total \n'))

if importe > 1000:
    descuento = (importe * 0.85)
    print ('Se le ha aplicado un descuento del 15% por lo que el total a pagar será de: $',descuento)
else:
    print('No hay descuentos disponibles, el total a pagar es de: $',importe)