# import random

# num=random.randint(1.100)
# intentosm=10
# intentosa=0
# dead=False
# print("bienvenido al programa este ejercicio trata de descubrir el numero entre 1y 100 buen suerte")
# acierto=int(input("ingrese su numero"))
# while True:
#     intentosa+=1
#     if acierto!= num:
#         intentosm-=1
#         if intentosm <1:
#             muerto=False
#             break
#         print(f"error no acertaste te quedan {intentosa} intentos")
#         if acierto> num:





# def calcular_puntaje(ingresos, nivel_educacional, nacionalidad):
#     # Calcular valor de ingresos
#     if 500000 <= ingresos <= 1000000:
#         puntaje_ingresos = 300000
#     elif 1000000 < ingresos <= 1500000:
#         puntaje_ingresos = 650000
#     elif ingresos > 1500000:
#         puntaje_ingresos = 1000000
#     else:
#         return "Ingreso no válido"

#     # Determinar el multiplicador de acuerdo al nivel educacional
#     if nivel_educacional == "básico":
#         multiplicador = 1
#     elif nivel_educacional == "medio":
#         multiplicador = 1.3
#     elif nivel_educacional == "superior":
#         multiplicador = 1.5
#     else:
#         return "Nivel educacional no válido"

#     # Bonificación por nacionalidad
#     if nacionalidad == "chilena":
#         bonificacion = 300000
#     elif nacionalidad == "extranjero":
#         bonificacion = 0
#     else:
#         return "Nacionalidad no válida"

#     # Calcular el puntaje final
#     puntaje_credito = (puntaje_ingresos * multiplicador) + bonificacion
#     return puntaje_credito

# # Ejemplo de uso
# ingresos = 1200000  # Ejemplo de ingresos
# nivel_educacional = "medio"  # Ejemplo de nivel educacional
# nacionalidad = "chilena"  # Ejemplo de nacionalidad

# puntaje = calcular_puntaje(ingresos, nivel_educacional, nacionalidad)
# print(f"Puntaje de crédito: {puntaje}")

# credito=input("hola puedes decirme tus ingresos este es un sistema automatico que te ayude a calcular tu credito ")

# if 500.000<=1.000.000
from random import randint
num=int(input("ingresa un numero "))
num2=int(input("ingresa un numero mayor al primero "))
numr=randint(num,num2)

if num>=num2:
    print("invalido el numero es menor al numero 2")
else:
    print(f"su numero es {num} y {num2}")

print(f"▄ "*numr)

