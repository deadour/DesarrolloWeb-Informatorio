#16 Hacer un programa que calcule el total a pagar por la compra de camisas.
#Si se compran tres camisas o mas se aplica un descuento del 20% sobre el total de la compra y
#si son menos de tres camisas un descuento del 10%.

print ('Bienvenidos, el precio de todas las camisas es de $5000. \n')
compra = str(input('Desea comprar una camisa? S/N. \n'))
camisa = 5000
cont = 0

while compra == 'S':
    cont = (cont + 1)
    print ('Ha añadido ',cont,'camisas al carrito, con un total de: $',cont*camisa)
    compra = str(input('Desea comprar otra camisa? S/N. \n'))

if cont >= 3:
    total = ((camisa * cont) * 0.80)
else:
    total = ((camisa * cont) * 0.90)

print ('El total a pagar es de: $', total)
