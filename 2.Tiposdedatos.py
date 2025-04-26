#TIPOS DE DATOS EN PYTHON
print("⬇️  Declara variables de cada tipo")
#Declara una variable de cada tipo básico: entero, flotante, cadena y booleano.
entero = 20
flotante = 5.2
cadena = "Hola Sebas"
booleano = True
print("")

print (f"Tipo int = {entero}")
print (f"Tipo float = {flotante}")
print (f"Tipo str = '{cadena}'")
print (f"Tipo bool = {booleano}")
print("")
print("")



print("⬇️  Conversión de cadena a entero y suma con otro número")
#Convierte una cadena con valor numérico a entero y realiza una suma con otro número.
cadenavn = "50"
num = int(cadenavn)
num2 = int(8)
suma = num + num2

print (f"La cadena de valor numérico es: '{cadenavn}'")
print (f"Ya convertido {cadenavn} a tipo int({num}), sumamos {num} + {num2}")
print (f"El resultado de la suma es: {suma}")
print("")
print("")



print("⬇️  Conversión de entrada de texto a float y multiplicación ")
#Convierte una entrada de texto a número flotante, multiplícala por 2 y muestra el resultado.
entradadt = input("Ingresa un número que quieras multiplicar por 2:\n")
try:
    numerofloat = float(entradadt)
    resultado = numerofloat * 2
    print (f"Ya convertida la entrada de texto ({entradadt}) a tipo float({numerofloat}), pasamos a multiplicar")
    print (f"Si multiplicamos {numerofloat} x 2, nos da como resultado {resultado}")
except ValueError:
    print (f" ⚠️ Error: '{entradadt}' no es un número.")
print("")
print("")



print("⬇️  Función que recibe un str y devuelve True or False")
#Escribe una función que reciba un string y devuelva True si puede convertirse a número y False si no.
def numtof(texto):
    try:
        float(texto)
        return True
    except ValueError:
        return False

# Probando la función
print(f"'123' ¿es número? {numtof('123')}")
print(f"'108.5' ¿es número? {numtof('108.5')}")
print(f"'-5' ¿es número? {numtof('-5')}")
print(f"'Hola' ¿es número? {numtof('Hola')}")
print("")
entrada = input("Escribe algo y veamos si es un número o no\n")
if numtof(entrada):
    print("✅ ¡Es un número!")
else:
    print("⚠️  No es un número.")