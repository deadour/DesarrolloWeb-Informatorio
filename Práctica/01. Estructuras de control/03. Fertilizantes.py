#DESAFIO 3
#Para el uso de fertilizantes es necesario medir cuánto abarca un determinado compuesto en el
#suelo el cual debe existir en una cantidad de al menos 10% por hectárea
#y no debe existir vegetación del tipo MATORRAL.
#Escribir un programa que determine si es factible la utilización de fertilizantes.

matorral = str(input('¿Existe matorral en el suelo? S/N \n'))

if matorral == 'S':
    print('No es factible el uso de fertilizantes')
elif matorral == 'N':
     compuesto = int(input('Ingrese el numero de porcentaje que abarca el compuesto en el suelo por hectarea\n'))
     if compuesto >= 10:
         print('Es factible la utlización de fertilizantes.')
     else:
        print('No es factible el uso de fertilizantes')
else:
    print ('Valor inválido. Vuelva a ejecutar el programa.')
