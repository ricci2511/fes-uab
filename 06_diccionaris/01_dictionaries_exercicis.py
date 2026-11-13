###
# EXERCICIS (diccionaris)
###

# Exercici 1: Crear un diccionari
# Crea un diccionari anomenat estudiant amb les claus "nom", "edat" i "assignatures"
# (aquesta última, una llista amb tres assignatures). Imprimeix-lo.
estudiant = {
    "nom": "John Doe",
    "edat": 20,
    "assignatures": ["Matemàtiques", "Física", "Electrònica"]
}
print(estudiant)

# Exercici 2: Accedir i modificar
# Imprimeix la segona assignatura de l'estudiant i canvia'n l'edat a un valor nou.
print(estudiant["assignatures"][1])
estudiant["edat"] = 21

# Exercici 3: Afegir i eliminar
# Afegeix la clau "grau" a l'estudiant i elimina després la clau "edat" amb del.
estudiant["grau"] = "Enginyeria en sistemes de telecomunicacio"
del estudiant["edat"]

# Exercici 4: Comprovar claus
# Comprova amb in si existeixen les claus "nom" i "email" i imprimeix el resultat.
print(f'Existeix la clau nom? {"nom" in estudiant}.')
print(f'Existeix la clau email? {"email" in estudiant}.')

# Exercici 5: Recórrer un diccionari
# Recorre el diccionari amb un bucle for i items() i imprimeix cada parella com "clau: valor".
for k, v in estudiant.items():
    print(f'{k}: {v}')

# Exercici 6: Comptar paraules
# Donada la llista de paraules:
# paraules = ["sol", "lluna", "sol", "estrella", "lluna", "sol"]
# Crea un diccionari que indiqui quantes vegades apareix cada paraula.
paraules = ["sol", "lluna", "sol", "estrella", "lluna", "sol"]
counts = {}
for p in paraules:
    if p in counts: counts[p] += 1
    else: counts[p] = 1
print(counts)
