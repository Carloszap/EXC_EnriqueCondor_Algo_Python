# Decoración de inicio
print("----------------------------------------")
print("Ejercicio 3: Calcular puntaje final del alumno.")
print("----------------------------------------")

# Datos de entrada:
print("Por favor ingrese el número de respuestas correctas: ")
resp_ok = int(input("Correctas: "))

print("Por favor ingrese el número de respuestas incorrectas: ")
resp_nok = int(input("Incorrectas: "))

print("Por favor ingrese el número de respuestas en blanco: ")
resp_null = int(input("En blanco: "))

# Proceso: cálculo de puntaje en base a respuestas y peso:
punt_final = (resp_ok * 3) + (resp_nok * -1) + (resp_null * 0)

# Datos de salida:
print("El puntaje final obtenido es: ", punt_final)
