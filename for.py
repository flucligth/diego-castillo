# edad=input("ingrese su edad")

# print(f'hola mundo su edad es {edad}')

# tabla de multiplicar

# num=int(input("ingrse su numero"))
# for i in range(1,11):
#   print(num,"x",i,"=", num*i)

# nombre=input("ingrese su nombre")
# for i in range(3):
#     print("hola" , nombre)

#sacar promedio con for

# cant=int(input("ingrese su cantidad de notas"))
# suma=0
# for i in range(cant):
#     nota= float(input(f"ingrese su nota {i +1}:"))
#     suma+=nota

# promedio = suma /cant
# print("el promedio es: ",round,{promedio})

cant=int(input("ingrese la cantidad de numeros"))
n1=int(input("ingrese su nota"))
suma=0
for i in range(cant):
    suma+=n1
print("la suma de todos los numeros es", suma)