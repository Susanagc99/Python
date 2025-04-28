#OPERADORES RELACIONALES

print("⬇️")
#Pide dos números e indica cuál es mayor o si son iguales.
print ("Ingresa dos números y veamos cuál es mayor")
num1 = float(input("\nIngresa un número \n"))
num2 = float(input("Ingresa otro número \n"))
if num1 > num2:
    print (f"\n{num1} es mayor que {num2}")
elif num1 < num2:
    print (f"\n{num2} es mayor que {num1}")
else:
    print (f"\n{num1} es igual a {num2}")    
    
print("") 
print("") 



print("⬇️")
#Solicita una edad y determina si la persona es menor de edad (menor a 18).
print ("Vamos a determinar si eres menor de edad")
edad = int(input("\nIngresa tu edad\n"))
if edad < 18:
    print ("\nSi, eres menor de edad")
else:
    print ("\nNo, ya eres todo un adulto")

print("") 
print("") 



print("⬇️")
#Escribe un programa que compare dos cadenas de texto e indique si son iguales o distintas.
print("Comparador de cadenas de texto")

cadena1 = input("\nIngresa la primera cadena de texto: ")
cadena2 = input("Ingresa la segunda cadena de texto: ")

if cadena1 == cadena2:
    print("\nLas dos cadenas de texto son iguales.")
else:
    print("\nLas dos cadenas de texto son distintas.")

print("") 
print("")

 

#OPERADORES LÓGICOS

print("⬇️")
#Pide al usuario su edad y si tiene licencia de conducción. Solo si ambas condiciones se cumplen, imprime que puede conducir.
print ("Veamos si puedes conducir en Colombia")
edadmin = int(input("\nIngresa tu edad\n"))
licencia = input("¿Tienes licencia de conducir? (si/no):\n").lower()
if edadmin >= 16 and licencia == "si":
    print ("\nPuedes conducir!")
else: 
    print ("\nAún no puedes conducir :c")

print("") 
print("") 


    
print("⬇️")
# Solicita si una persona tiene experiencia laboral y título universitario. Usa operadores lógicos para decidir si puede aplicar a una oferta de trabajo.
print("Vamos a verificar si puedes aplicar a una oferta de trabajo")

tiene_experiencia = input("\n¿Tienes experiencia laboral? (si/no): ").lower()
tiene_titulo = input("¿Tienes título universitario? (si/no): ").lower()

aplicación = (tiene_experiencia == "si") and (tiene_titulo == "si")

if aplicación:
    print("\n¡Felicidades! Cumples con los requisitos para aplicar a la oferta.")
else:
    print("\nLo sentimos, no cumples con ambos requisitos para aplicar a esta oferta.")

print("") 
print("") 



print("⬇️")
# Dado un número, determina si está en el rango de 10 a 50 (inclusive).
print("Verificador de rango numérico")

numero = int(input("\nIngresa un número:\n"))

if numero >=10 and numero <= 50:
    print(f"\nEl número {numero} está dentro del rango de 10 a 50 (inclusive).")
else:
    print(f"\nEl número {numero} está fuera del rango de 10 a 50.")