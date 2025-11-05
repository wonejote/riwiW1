#---------------------Task 2---------------------

print("Bienvenido a InventarioFacil.com \ningresa los siguientes datos para agregar un nuevo producto") 

itemName = input("Nombre del producto: ") #itemName almacena el nombre del producto

while  itemName.isdecimal() or itemName.isspace(): #bucle while, solo se entra si itemName conitene solo números o espacios
                                                   #Si se entra en el bucle, se vuelve a pedir al usuario un nombre de producto
                                                   #el bucle se repite hasta que itemName sea correcto
    itemName = input(f"{itemName} es inválido. No es posible nombrar productos solo con numeros o espacios \npor favor ingresa un nombre válido: ")

itemPrice = input("Precio del producto: ") #itemPrice almacena el precio del producto

while  itemPrice.isalpha() or itemPrice.isspace() or float(itemPrice) < 0: #bucle while, se puede entrar si sucede 1 de 3 casos:
                                                                           # 1: tiene letras, tiene espacios, es negativo
    itemPrice = input(f" {itemPrice} es inválido, por favor ingresa un precio numérico y positivo: ")


itemPrice = float(itemPrice)  #si se sale del bucle, es porque el usuario ingreso un valor correcto, entonces es posible 
                              #convertir itemPrice a tipo flotante

itemCount = input("Cantidad del producto: ") #itemCount almacena el numero de productos

while not itemCount.isdecimal():
    itemCount = input(f" {itemCount} es inválido, por favor ingresa una cantidad entera y positiva: ")
 
itemCount = int(itemCount)

#---------------------Task 3---------------------

costoTotal = itemPrice*itemCount

#---------------------Task 4---------------------

print(f"Producto: {itemName} | Precio: {itemPrice} | Cantidad: {itemCount} | Total: {costoTotal}")

#------------------------------------------------

