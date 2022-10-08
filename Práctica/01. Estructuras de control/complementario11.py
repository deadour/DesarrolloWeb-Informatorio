#11 Determinar si un alumno aprueba a reprueba un curso, sabiendo que aprobara si su promedio
# de tres calificaciones es mayor o igual a 70; desaprueba en caso contrario.

calif1 = float(input('Ingrese calificacion 1 \n'))
calif2 = float(input('Ingrese calificacion 2 \n'))
calif3 = float(input('Ingrese calificacion 3 \n'))

promedio = ((calif1 + calif2 + calif3) / 3)

if promedio >= 70:
    print ('El alumno aprobó el curso. El promedio es de:',format(promedio,'.2f'))
else:
     print ('El alumno desaprobó el curso. El promedio es de:',format(promedio,'.2f'))