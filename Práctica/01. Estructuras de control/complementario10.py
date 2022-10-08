#10 Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad distinta.
# Obtener el porcentaje que cada quien invierte con respecto a la cantidad total invertida.

inv1 = float(input('Ingrese inversion 1 \n'))
inv2 = float(input('Ingrese inversion 2 \n'))
inv3 = float(input('Ingrese inversion 3 \n'))

total = (inv1 + inv2 + inv3)

porc1 = (inv1 / total) * 100
porc2 = (inv2 / total) * 100
porc3 = (inv3 / total) * 100

print ('La inversion 1 representa un ',format(porc1, '.2f'),'% del total. \n La inversion 2 representa un ',format(porc2, '.2f'),'% del total. \n La inversion 3 representa un ',format(porc3, '.2f'),' % del total. \n')