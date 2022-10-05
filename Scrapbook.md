Ejercicio 3.
Se necesita elaborar un algoritmo que solicite el
número de respuestas correctas, incorrectas y en blanco,
correspondientes a postulantes, y muestre su puntaje final
considerando que por cada respuesta correcta tendrá
3 puntos, respuestas incorrectas tendrá -1 y respuestas en
blanco tendrá 0.

Datos de entrada:
Número de respuestas correctas = resp_ok
Numero de respuestas incorrectas = resp_nok
Número de respuestas en blanco = resp_null

Proceso:
Calcular puntaje final y asignar a variable:
punt_final = (resp_ok * 3) + (resp_nok * -1) + (resp_null * 0)

Datos de salida:
Imprimir punt_final