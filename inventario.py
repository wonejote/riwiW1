#---------------------Task 2---------------------

print("Bienvenido a InventarioFacil.com \ningresa los siguientes datos para agregar un nuevo producto")

itemName = input("Nombre del producto: ")

while  itemName.isdecimal() or itemName.isspace():
    itemName = input(f"{itemName} es inválido. No es posible nombrar productos solo con numeros o espacios \npor favor ingresa un nombre válido: ")

itemPrice = input("Precio del producto: ")

while  itemPrice.isalpha() or itemPrice.isspace() or float(itemPrice) < 0:
    itemPrice = input(f" {itemPrice} es inválido, por favor ingresa un precio numérico y positivo: ")


itemPrice = float(itemPrice)

itemCount = input("Cantidad del producto: ")

while not itemCount.isdecimal():
    itemCount = input(f" {itemCount} es inválido, por favor ingresa una cantidad entera y positiva: ")
 
itemCount = int(itemCount)

#---------------------Task 3---------------------

costoTotal = itemPrice*itemCount

#---------------------Task 4---------------------

print(f"Producto: {itemName} | Precio: {itemPrice} | Cantidad: {itemCount} | Total: {costoTotal}")

#------------------------------------------------

