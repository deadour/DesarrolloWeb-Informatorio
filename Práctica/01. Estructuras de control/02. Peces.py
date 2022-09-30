#DESAFIO N°2

#La contaminación del agua es cualquier cambio químico, físico o biológico en la calidad del
#agua que tiene un efecto dañino en cualquier cosa viva que consuma ese agua.
#Cuando seres humanos beben el agua contaminada tienen a menudo problemas de salud.
#La contaminación del agua se detecta en los laboratorios,
#donde pequeñas muestras de agua se analizan para diversos tipos de contaminantes.
#Los organismos vivos tales como pescados se pueden también utilizar para la 
#detección de la contaminación del agua. Los cambios en su comportamiento o crecimiento nos demuestran,
#que el agua en la que viven está contaminada.
#Para seguir colaborando en esta misión de salvar al planeta,
#necesitamos que elabores un programa en Python que dado el tamaño de un pez
#indique si su organismo está contaminado. Para ello tendremos 4 opciones:

#Tamaño Normal: Mensaje "Pez en buenas condiciones"
#Tamaño por debajo de lo Normal: Mensaje "Pez con problemas de nutrición"
#Tamaño un poco por encima de lo Normal: Mensaje "Pez con síntomas de organismo contaminado"
#Tamaño sobredimensionado: Mensaje "Pez contaminado"

rta = str(input('Desea iniciar el programa? S/N \n'))
print ('\n')

while rta == 'S':

    tamanio = int(input('Por favor, ingrese el tamaño del pez, de acuerdo a las siguientes opciones: \n 1.Tamaño Normal \n 2.Tamaño por debajo de lo normal \n 3.Tamaño un poco por encima de lo normal \n 4.Tamaño sobredimensionado \n'))
    print ('\n')

    if tamanio == 1:
        print ('Pez en buenas condiciones \n')
    elif tamanio == 2:
        print ('Pez con problemas de nutrición \n')
    elif tamanio == 3:
        print ('Pez con síntomas de organismo contaminado \n')
    elif tamanio ==4:
        print ('Pez contaminado \n')
    else:
        print ('Error. Valor inválido \n')

    rta = str(input('Ingresar otro valor? S/N \n'))

        
