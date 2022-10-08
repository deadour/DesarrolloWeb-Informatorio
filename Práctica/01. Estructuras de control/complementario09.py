#9 En un Centro Asistencial existen tres áreas: Pediatría, Traumatología y Kinesiología.
# El presupuesto anual del hospital se reparte conforme a la sig. tabla:

#ÁREA 		   | PORCENTAJE

#Pediatría		|	60%

#Traumatología	|	 20%

#Kinesiología	|	20%


# Obtener la cantidad de dinero que recibirá cada área, para cualquier monto presupuestal 
# que se ingrese por teclado.

monto = float(input('Ingrese monto presupuestal \n'))

pediatria = (monto * 0.60)
traumokinesio = (monto * 0.20)

print('Para el monto ingresado: $',monto,'\n El área de pediatria recibirá: $',format(pediatria, '.2f'),'\n El área de traumotología recibirá: $',format(traumokinesio, '.2f'),'\n El área de kinesiología recibirá: $',format(traumokinesio, '.2f'))