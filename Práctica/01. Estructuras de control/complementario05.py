#5 Diseñar un programa que lea las longitudes de los tres lados de un triángulo (L1,L2,L3) y determine qué tipo de triángulo es,
#de acuerdo a los siguientes casos. 
#Suponiendo que A determina el mayor de los tres lados y B y C corresponden con los otros dos, entonces:

#Si A>=B + C à No se trata de un triángulo

#Si A2 = B2 + C2 à Es un triángulo rectángulo

#Si A2 > B2 + C2 à Es un triángulo obtusángulo

#Si A2 < B2 + C2 à Es un triángulo acutángulo

A = int(input('Ingrese L1 o hipotenusa \n'))
B = int(input('Ingrese L2 \n'))
C = int(input('Ingrese L3 \n'))

if A >= (B + C):
    print('No se trata de un triangulo \n')
elif A**2 == (B**2 + C**2):
    print('Es un triángulo rectángulo \n')
elif A**2 > (B**2 + C**2):
    print('Es un triángulo obtusángulo \n')
elif A**2 < (B**2 + C**2):
    print('Es un triángulo acutángulo \n')