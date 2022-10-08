#DESAFÍO 5

#La ciudad esta dividida en 2 secciones de recolección, sección A y B de acuerdo al nombre del barrio
#y el tipo del barrio (CÉNTRICO y NO CÉNTRICO)
#La sección A esta formada por los barrios céntricos cuyo nombre comienza con una letra anterior a M
#y los barrios no céntricos con nombre posterior a la M, y la sección B el resto.
#Debemos hacer un programa que dado el nombre del barrio y
#la ubicación, nos informe en que sección se encuentra.

#barrios: Seccion A: centricos (A-M) no centricos (M-Z); Seccion B: no centricos (A-M) centricos (M-Ze)

nombreBarrio = str(input('Ingrese el nombre del barrio \n'))
ubicacion = int(input('Ingrese ubicacion: \n 1.Centro \n 2.No centro \n'))

if nombreBarrio.lower() < 'm' and ubicacion == 1:
        print ('Su barrio pertenece a la sección A \n')

elif (nombreBarrio.lower() > 'm') and (ubicacion == 2):
    print ('Su barrio pertenece a la sección A \n')
elif nombreBarrio.lower() < 'm' and ubicacion == 2:
    print ('Su barrio pertenece a la sección B \n')
elif nombreBarrio.lower() > 'm' and ubicacion == 1:
    print ('Su barrio pertenece a la sección B \n')
else:
    print ('Ingrese valor válido')