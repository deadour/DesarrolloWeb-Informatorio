#13 En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento
#dependiendo de un número que se escoge al azar.
# Si el numero escogido es menor que 74 el descuento es del 15% sobre el total de la compra,
# si es mayor o igual a 74 el descuento es del 20%. Obtener cuánto dinero se le descuenta.

numero = int(input('Ingrese nro \n'))
importe = float(input('Ingrese importe de la compra \n'))

if numero >= 74:
    descuento = (importe * 0.20)
elif numero < 74:
    descuento = (importe * 0.15)

print('Se le descontó un total de: $',descuento)
