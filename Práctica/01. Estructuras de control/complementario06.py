#6 Un equipo de fútbol ha tenido una buena campaña y desea premiar a sus jugadores con un aumento del salario
#para la siguiente campaña. Los sueldos deben ajustarse de la siguiente forma:

#Sueldo Actual (en $)   | Aumento

#0 – 6000				|   15%

#6000 – 7900			|   10%

#7900 – 12000			|	 6%

#Más de 12000			|	 0%

#Diseñar un programa que lea el salario de un jugador, y que a continuación muestre el 
#tanto por ciento de aumento, el sueldo actual y el sueldo aumentado.

sueldo = float(input('Ingrese el sueldo \n'))

if sueldo <= 6000:
    sueldonuevo = (sueldo * 1.15)
    print('Vas a tener un aumento del 15%, tu sueldo actual es de: $',sueldo,'y el sueldo nuevo va a ser de: $',format(sueldonuevo, '.2f'))
elif (sueldo > 6000) and (sueldo <= 7900):
    sueldonuevo = (sueldo * 1.10)
    print('Vas a tener un aumento del 10%, tu sueldo actual es de: $',sueldo,'y el sueldo nuevo va a ser de: $',format(sueldonuevo, '.2f'))
elif (sueldo > 7900) and (sueldo <= 12000):
    sueldonuevo = (sueldo * 1.06)
    print('Vas a tener un aumento del 6%, tu sueldo actual es de: $',sueldo,'y el sueldo nuevo va a ser de: $',format(sueldonuevo, '.2f'))
elif (sueldo > 12000):
    print('No vas a tener un aumento. tu sueldo actual es de: $',sueldo)