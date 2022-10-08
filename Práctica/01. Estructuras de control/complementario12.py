#12 Hacer un programa que imprima el nombre de un artículo, clave, precio original y su precio con descuento.
#El descuento lo hace en base a la clave, si la clave es 01 el descuento es del 10% y si la clave es 02
# el descuento en del 20% (solo existen dos claves).

nombre = str(input('Ingrese el nombre del articulo \n'))
clave = int(input('Ingrese la clave del producto. \n 1. Clave 01 \n 2. Clave 02 \n'))

if clave <= 2: 
    precio = float(input('Ingrese el precio del producto.\n'))
    if clave == 1:
        descuento = (precio * 0.90)
    elif clave == 2:
        descuento = (precio * 0.80)
    
    print('El nombre del articulo es:', nombre, '\n La clave es: ',clave, '\n El precio original es de: $',precio, '\n El precio con descuento es de: $',format(descuento, '.2f'))

elif clave > 2:
    print ('Ingrese valor del clave válido \n')



