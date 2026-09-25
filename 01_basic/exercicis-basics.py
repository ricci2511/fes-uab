###
# exercicis-basics.py
# Exercicis per practicar els conceptes apresos a les lliçons.
###

print("\nExercici 1: Imprimir missatges")
print("Escriu un programa que imprimeixi el teu nom i la teva ciutat en línies separades.")

### Completa aquí
print("Ricardo Christmann", "S'Illot", sep="-")

print("--------------")

print("\nExercici 2: Mostra els tipus de dades de les variables següents:")
print("Utilitza la comanda 'type()' per determinar el tipus de dades de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(type(a), type(b), type(c), type(d), type(e))

print("--------------")

print("\nExercici 3: Conversió de tipus")
print("Converteix la cadena \"12345\" a un enter i després a un float.")
print("Converteix el float 3.99 a un enter. Què passa?")

### Completa aquí
print(int("12345"), float("12345"), int(3.99))
print("Si convertim 3.99 a int, el resultat es nomès la part entera, que és 3")


print("--------------")

print("\nExercici 4: Variables")
print("Crea variables per al teu nom, edat i alçada.")
print("Utilitza f-strings per imprimir una presentació.")

### Completa aquí
name = "Ricardo Christmann"
age = 99
height = 1.75
print(f"Hola! Em dic {name}, tinc {age} anys i faig {height} metres")

print("--------------")

print("\nExercici 5: Nombres")
print("1. Crea una variable amb el nombre PI (sense assignar una variable)")
print("2. Arrodoneix el nombre amb round()")
print("3. Fes la divisió entera entre el nombre resultant i el nombre 2")
print("4. El resultat hauria de ser 1")

PI = 3.14159
print("Resultat: ", int(round(PI) / 2))

print("--------------")

print("\nExercici 6: Conversor de temperatura")
print("Demana a l'usuari una temperatura en graus Celsius.")
print("Converteix aquest valor a Fahrenheit amb la fórmula: F = (C * 9/5) + 32")
print("Mostra els dos valors amb un missatge clar.")

### Completa aquí
celsius = float(input("Introduex la temperatura en graus Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperatura en Celsius: {celsius}, Temperatura en Fahrenheit: {fahrenheit}")

print("--------------")

print("\nExercici 7: Calculadora de propina")
print("Demana el total d'un compte i el percentatge de propina.")
print("Calcula quant és la propina i el total final que s'ha de pagar.")
print("Mostra els resultats amb 2 decimals.")

### Completa aquí
total = float(input("Introdueix el total del compte: "))
propina_percentatge = float(input("Introdueix el percentatge de propina: "))
propina = total * propina_percentatge / 100
total_final = total + propina
print(f"Propina: {round(propina, 2)}, Total final: {round(total_final, 2)}")

print("--------------")

print("\nExercici 8: Validador de contrasenya simple")
print("Demana una contrasenya a l'usuari.")
print("Comprova si té almenys 8 caràcters.")
print("Mostra 'Contrasenya vàlida' o 'Contrasenya no vàlida'.")

### Completa aquí
password = input("Introdueix la contrasenya: ")
if len(password) >= 8:
    print("Contrasenya vàlida")
else:
    print("Contrasenya no vàlida")
