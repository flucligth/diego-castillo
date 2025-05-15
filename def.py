
carrito=0

def agregar_carrito():
    
    global carrito,n
    n=input("ingrese su nombre ")

    
    while True:
        
        print('''1=papas fritas con sabor oregano
              2,=bolsa de coyacs
              3;=cabritas
              4;=chocolate blanco
              5;=salir''')
        op=int(input(f"hola {n} bienvenido al supermercado que desea llevar? "))
        match op:
            
         case 1:
          print("usted lleva papas fritas con sabor oregano")
          carrito+=2000

         case 2:
          print("usted lleva una bolsa de coyacs")
          carrito+=1500

         case 3:
          print("usted lleva cabritas")
          carrito+=2500

         case 4:
          print("usted lleva chocolate blanco")
          carrito+=4000

         case 5:
          print("desea salir de el supermercado")
          break
            

def boleta(n):
  print(f"mr {n} su total es de {round(carrito*1.19)} pesos")









while True:
 op=int(input('''ingrese una opcion
              1,= carrito
              2,=boleta
              3,=salir
              '''))
 match op:
  case 1:
    agregar_carrito()
  case 2:
    boleta(n)
  case 3:
   print("opcion invalida")
  case 3:
   print("gracias por su compra")
   break
   