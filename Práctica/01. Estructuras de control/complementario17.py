#17 Determinar y exhibir si la estatura de una persona adulta dada,
#es mayor que la estatura media de las personas adultas de su sexo, siendo:


#- estatura media de mujeres adultas: 1,65 m.

#- estatura media de varones adultos: 1,72 m.

sexo = str(input('Ingrese sexo (M/F) \n'))

if sexo.lower() == ('m' or 'f'):
    estatura = int(input('Ingrese estatura (en centimetros) \n'))

    if (sexo.lower() == 'm') and (estatura > 172):
     print ('Es mayor que el promedio')
    elif (sexo.lower() == 'f') and (estatura > 165):
     print ('Es mayor que el promedio')
    else:
     print ('Es menor que el promedio.')

else:
    print ('Ingrese sexo válido.')