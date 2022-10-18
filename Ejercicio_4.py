# Decoración de inicio

print("-----------------------------------------------------------------------")
print("Ejercicio 4: Calcular puntaje total del club ABC en el torneo apertura.")
print("-----------------------------------------------------------------------")

# Datos de entrada:
print("Por favor ingrese el número de partidos ganados por el club: ")
PG = int(input())
print("Por favor ingrese el número de partidos perdidos por el club: ")
PP = int(input())
print("Por favor ingrese el número de partidos empatados por el club: ")
PE = int(input())

# Cálculo del puntaje:
PPG = PG * 3
PPP = PP * 1
PPE = PE * 0

PF = PPG + PPP + PPE

#Datos de salida:
print("El puntaje final del club ABC en el torneo apertura es ", PF)
