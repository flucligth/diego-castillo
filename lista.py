# i=[]
# for e in range(3):
#     i.append(input("ingrese un producto "))
# print(i)
# try:

#  l=int(input("ingrese un numero de productos a eleminar"))
# except Exception:
#    print("ingrese un numero valido entre 1 y 3")
# print(i)
# print("============================")
# i.pop(l)
# print(i)
# list=[]




while True:
    print('''  
           1,- agregar elementos a tu lista
           2,- eliminar elementos de tu lista
           3,- mostrar cada uno de los elementos de forma ordenada
           4,- cerrar el programa''')
    op=int(input("ingrese una opcion "))
    print("====================================")
    print("esta es tu lista actual", list)
    print("===================================")
    match op:
        case 1:
            list.append(input("ingrese un producto "))
        case 2:
            l=int(input("ingresa un numero del producto que deseas eliminar(empieza desde 0) "))
            for i,item in enumerate(list):
                print(f" {i},- {item}")
            list.pop(l)
        case 3:
            for i,item in enumerate(list):
                print(f" {i}.- {item}")
        case 4:
            break
print("=======================")
print("hasta luego vuelva pronto")
print("=======================")
print(" asi termino tu lista", list)


# l=input("ingresa algo")

# for i in len(l):
#     print(i)