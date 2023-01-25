# print("****MOZZARRELA PIZZA****")#35:08
# print("Menú de pizzas\n 1- Margarita = 10$\n 2- Jamón y Queso = 15$\n 3- Cuatro Quesos = 20$")
# seleccion_pizza = int(input("Hola, por favor, seleccione su pizza con un número de opción: "))
# dinero = float(input("Hola indique el dinero que lleva: "))
# margarita = 10
# jamon_queso = 15
# cuatro_quesos = 20
# error = True
# match seleccion_pizza:
#     case 1:
#         print(f"Ha elegido la pizza Margarita")
#     case 2:
#         print(f"Ha elegido la pizza Jamón y Queso")
#     case 3:
#         print(f"Ha elegido la pizza Cuatro Quesos")
#     case _:
#         error = False

# if dinero >= margarita:
#         total = dinero - margarita
#         restante = dinero - total
#         #print(f"Su total a pagar es {total}$ ")
#         #print(f"Le quedan {restante}$")
# elif dinero >= jamon_queso:
#         total = dinero - jamon_queso
#         restante = dinero - total
#         #print(f"Su total a pagar es {total}$ ")
#         #print(f"Le quedan {restante}$")
# else: 
#     dinero >= cuatro_quesos
#     total = dinero - cuatro_quesos
#     restante = dinero - total
# print(f"Su total a pagar es {restante}$ ")
# print(f"Le quedan {total}$")


# seleccion_ingrediente = int(input("Desea algún ingrediente adicional, seleccione:\n 1. Champiñones 2$\n 2. Maíz $1\n 3. Tocineta $4\n 4. No añadir extra y pagar\n"))
# champinones = 2
# maiz = 1
# tocineta = 4
# error = True

# match seleccion_ingrediente:
#         case 1:
#             print(f"Ha elegido Champiñones")
            
#         case 2:
#             print(f"Ha elegido Maíz")
            
#         case 3:
#             print(f"Ha elegido Tocineta")
            
#         case _:
#             error = False

# if seleccion_ingrediente == champinones:
#     print(f"Extra a pagar {champinones}$")
#     total_extra = total - champinones
#     print(f"Su total a pagar es: {total_extra}")
#     int(input("Desea algún ingrediente adicional, seleccione:\n 1. Maíz $1\n 2. Tocineta $4\n 3. No añadir extra y pagar\n"))
# elif seleccion_ingrediente == maiz:
#     print(f"Extra a pagar {maiz}$")
#     total_extra = total - maiz
#     print(f"Su total a pagar es: {total-total_extra}")
#     int(input("Desea algún ingrediente adicional, seleccione:\n 1. 1. Tocineta $4\n 2. No añadir extra y pagar\n"))
# else:
#     seleccion_ingrediente == tocineta
#     print(f"Extra a pagar {tocineta}$")
#     total_extra = total - tocineta
#     print(f"Su total a pagar es: {total-total_extra}")
    

# print("--------SU PEDIDO--------")
# print(f"El total de su pedido es: {total_extra}$")

# print(f"-{seleccion_pizza}")
# print(f"-{seleccion_ingrediente}\n")
# print("¡Buen provecho!")


#Primero se declaran las variables
print("****MOZZARRELA PIZZA****")
dinero = float(input("Hola, ingrese el dinero que lleva:\n"))
dinero_inicial = dinero
total = 0
pedido = [] #Se van a ir almacenando el pedido del cliente

margarita = 10.5
jamon_queso = 15.2
cuatro_quesos = 20.6

champinones = 2.1
maiz = 1.3
tocineta = 4.0
error = True

print("------Menu de Pizzas------")
while True:#Hacemos el bucle infinito

    print(f"1- Margarita - {margarita}$")
    print(f"2- Jamón y Queso - {jamon_queso}$")
    print(f"3- Cuatro quesos - {cuatro_quesos}$")

    eleccion = int(input("Hola, por favor, seleccione la opción de su pizza:\n"))

    match eleccion:
        case 1:
            print(f"Ha elegido la pizza Margarita.\n Total a pagar {margarita}$")
            dinero -= margarita
            print(f"Le quedan {round(dinero,2)}$")
            total += margarita
            pedido.append(f"Margarita - {margarita}$")
            break 
        case 2:
            print(f"Ha elegido la pizza Jamón y Queso. Total a pagar {jamon_queso}$")
            dinero -= jamon_queso
            print(f"Le quedan {round(dinero,2)}$")
            total += jamon_queso
            pedido.append(f"Jamón y Queso - {jamon_queso}$")
            break 
        case 3:
            print(f"Ha elegido la pizza Cuatro quesos. Total a pagar {cuatro_quesos}$")
            dinero -= cuatro_quesos
            print(f"Le quedan {round(dinero,2)}$")
            total += cuatro_quesos
            pedido.append(f"Jamón y Queso - {cuatro_quesos}$")
            break 
        case _:
            print(f"Opcion incorrecta. Seleccione una opción válida del 1 al 3\n")

print("------Ingredientes Extras------")

while True:
      print(f"1- Champiñones - {champinones}$")
      print(f"2- Maíz - {maiz}$")
      print(f"3- Tocineta - {tocineta}$")
      print("4- No añadir extra y cancelar")

      eleccion = int(input("Desea algún ingrediente adicional:\n"))

      match eleccion:
        case 1:
            print(f"Ha elegido Champiñones. Extra a pagar {champinones}$\n")
            dinero -= champinones
            total += champinones
            print(f"Total a pagar {round(total,2)}$")
            print(f"Le quedan {round(dinero,2)}$\n")
            pedido.append(f"Champiñones - {champinones}$")
        case 2:
            print(f"Ha elegido Maíz. Extra a pagar {maiz}$")
            dinero -= maiz
            total += maiz
            print(f"Total a pagar {round(total,2)}$")
            print(f"Le quedan {round(dinero,2)}$\n")
            pedido.append(f"Champiñones - {maiz}$")            
        case 3:
            print(f"Ha elegido Tocineta. Extra a pagar {tocineta}$")
            dinero -= tocineta
            total += tocineta
            print(f"Total a pagar {round(total,2)}$")
            print(f"Le quedan {round(dinero,2)}$\n")
            pedido.append(f"Champiñones - {tocineta}$")  
        case 4:
            print("4- No añadir extra y cancelar")
            break
        case _:
            print(f"Opcion incorrecta. Seleccione la opción del 1 al 4")
if total <= dinero_inicial:
   

    print("----------SU PEDIDO---------")
    for i in pedido:
        print(f"{i}")

    print("\n ------FACTURA------")
    print(f"El total de su pedido es: {round(total,2)}$")
    print(f"Su cambio es: {round(dinero,2)}$\n")
    
    print("¡Buen provecho!")
else:
    print("Saldo insuficiente")




     






