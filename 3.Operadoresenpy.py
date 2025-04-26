#OPERADORES EN PYTHON
print("⬇️")
#Calcula el área de un rectángulo a partir de base y altura ingresadas por el usuario.
print ("Ingresa la base y la altura de un rectángulo a continuación")
base = float(input("base: "))
altura = float(input("altura: "))
area = base*altura
print(f"El area del rectángulo es: {area}")
print("")


print("⬇️")
#Dado un precio y un porcentaje de descuento, muestra el valor final a pagar.
print("Ingresa un precio")
precio = float(input())
print ("Ingresa el porcentaje de descuento que quieras aplicarle al precio anterior")
descuento = float(input())
valorf = precio - (precio*descuento/100)
print (f"El valor total con el descuento es de:  {valorf}")
print("")


print("⬇️")
#Calcula el residuo de dividir dos números dados por el usuario.
print("Vamos a hayar el residuo al dividir dos números")
r1 = int(input("Ingresa el primer número:  "))
r2 = int(input("Ingresa el segundo número:  "))
resultadoR = r1%r2
print(f"EL residuo de la división entre {r1} y {r2} es:  {resultadoR}")
print("")


print("⬇️")
#Escribe una fórmula que use al menos tres operadores diferentes y muestre el resultado.
resultadoop = (5 + 26) * 30
print(f"(5+26)*30 es igual a:  {resultadoop}")
