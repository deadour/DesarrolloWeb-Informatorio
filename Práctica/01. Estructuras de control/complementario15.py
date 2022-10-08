#15 Un obrero necesita calcular su salario semanal, el cual se obtiene de la siguiente manera:

#i. Si trabaja 40 horas o menos se le paga $16 por hora

#ii. Si trabaja más de 40 horas se le paga $16 por cada una de las primeras 40 horas y $20 por cada hora extra.

horas = int(input('Ingrese horas trabajadas \n'))

if horas <= 40:
    salario = (horas * 16)
else:
    extras = (horas - 40)
    salario = (40 * 16) + (extras * 20)

print ('Su salario es de: $',salario)
