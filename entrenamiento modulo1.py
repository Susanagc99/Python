#IMPORTANTE validar que tanto el precio como la cantidad sean números positivos, y que el descuento esté dentro del rango aceptable de 0 a 100%

print ("")
print ("")
print ("-"*36)
print ("|\tCarrito de compras 🛒\t""   ""|")
print ("-"*36)
print ("")
print ("")

#solcitar nombre del producto
print ("Nombre del producto ")
producto = input()
print (f"✅ El producto es ➡️   {producto} ")
print ("."*55)


#solicitar al usuario precio unitario / float
while True:
    try:
        print ("Ingresa el precio unitario") #se solicita el precio
        precio = float(input())
        if precio <= 0:
            print (f"⚠️  Error! ${precio} es incorrecto, debes ingresar un número positivo")
        else:
            print (f"✅ El precio unitario es ➡️   ${precio}")
            break               
    except ValueError:
        print ("⚠️  Error! Dato inválido. Vuelve a intentarlo")
print ("."*55)


#solicitar al usuario la cantidad de productos adquiridos / int
while True:
    try:
        print ("Ingresa la cantidad de productos que deseas comprar")
        cantidad = int(input())
        if cantidad > 0:
            print (f"✅ La cantidad que vas a comprar es ➡️   {cantidad}")
            break
        else:
            print (f"⚠️  Error! Debes ingresar un valor mayor que 0")
    except ValueError:
        print (f"⚠️  Error! Ingresaste un dato inválido. Vuelve a intentarlo")    
print ("."*55)        


#solicitar el porcentaje de descuento que se aplicará si es que existe alguno.
print ("¿Tu producto tiene descuento? (Si/No)")
haydescuento = input().strip().lower()
if haydescuento == "si":
    while True:
        try:
            print ("¿Cuál es el porcentaje del descuento?")
            porcentaje = float(input())
            if porcentaje >= 0 and porcentaje <= 100:
                preciowdescuento = precio - (precio*porcentaje/100)
                valorfinalwd = preciowdescuento*cantidad
                print (f"✅  EL valor final de tu compra es:  {valorfinalwd}")
                break
            else:
                print ("⚠️  Error! debes ingresar un porcentaje entre 0 y 100")
        except ValueError:
            print ("⚠️  Error! Ingresaste un dato inválido. Vuelve a intentarlo")            
elif haydescuento == "no":
    valorfinal1 = precio*cantidad
    print (f"✅ El valor total de tu compra es:  {valorfinal1}")
else:
    print (f"⚠️  Respuesta inválida. Asumimos que no tiene descuento")
    valorfinal1 = precio*cantidad
    print (f"✅ El valor total de tu compra es:  {valorfinal1}")
print ("."*55)  

#Imprimir factura
print ("")
print ("")
print ("-"*40)
print ("|\t  Factura de compra 🛍️\t        |")
print ("-"*40)
print ("")
print ("")

#subtotal de la factura
valorfinal1 = precio*cantidad

#Iniciar con descuento en 0, sino calcularlo según el descuento solicitado anteriormente
descuento = 0
if haydescuento == "si":
    descuento = (valorfinal1*porcentaje)/100
    valortotal = valorfinal1 - descuento
else:
    valortotal = valorfinal1
        
print (f"{producto:<26} {cantidad:>3} x {precio:>6.2f}") # Alineación a la izquierda (<) y derecha (>), y formato de número flotante con dos decimales(.2f)
print ("_"*40)
print (f"....................Subtotal    {valorfinal1:>6.2f}")
print (f"...................Descuento    -{descuento:>6.2f}")
print (f".......................Total    {valortotal:>6.2f}")
print ("_"*40)
