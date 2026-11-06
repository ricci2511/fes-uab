###
# EXERCICIS (for)
###

# Exercici 1: Imprimir números parells
# Imprimeix tots els números parells del 2 al 20 (inclosos) fent servir un bucle for.
for n in range(21):
    if n % 2 == 0: print(n)

# Exercici 2: Calcular la mitjana d'una llista
# Donada la llista de números següent:
# numeros = [10, 20, 30, 40, 50]
# Calcula la mitjana dels números fent servir un bucle for.
numeros = [10, 20, 30, 40, 50]
sum = 0
for n in numeros:
    sum += n
print(f'mitjana: {sum / len(numeros)}')


# Exercici 3: Buscar el màxim d'una llista
# Donada la llista de números següent:
# numeros = [15, 5, 25, 10, 20]
# Troba el número màxim de la llista fent servir un bucle for.
numeros = [15, 5, 25, 10, 20]
max = numeros[0]
for num in numeros[1:]:
    if num > max: max = num
print(f'max: {max}')

# Exercici 4: Filtrar cadenes per longitud
# Donada la llista de paraules següent:
# paraules = ["casa", "arbre", "sol", "elefant", "lluna"]
# Crea una llista nova que contingui només les paraules amb més de 5 lletres
# fent servir un bucle for i list comprehension.
paraules = ["casa", "arbre", "sol", "elefant", "lluna"]
paraules_llargues = []
for p in paraules:
    if len(p) > 5: paraules_llargues.append(p)
print(f'paraules amb més de 5 lletres: {paraules_llargues}')

# Exercici 5: Comptar paraules que comencen per una lletra
# Donada la llista de paraules següent:
# paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
# Demana a l'usuari que introdueixi una lletra.
# Compta quantes paraules de la llista comencen per aquesta lletra (sense diferenciar majúscules/minúscules).
paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
lletra = input('Entra una lletra: ')
count = 0
for p in paraules:
    if p[0] == lletra.lower(): count += 1
print(f'paraules de la llista comencen per aquesta lletra: {count}')

# Exercici 6: Mesures de tensió d'un sensor
# Durant una prova s'han registrat les tensions següents (en volts):
# tensions = [4.8, 5.0, 5.1, 4.9, 5.2]
# Fent servir un bucle for, calcula la tensió mitjana i imprimeix-la.
tensions = [4.8, 5.0, 5.1, 4.9, 5.2]
sum = 0
for v in tensions:
    sum += v
print(f'mitjana tensions: {sum / len(tensions)}')

# Exercici 7: Corrent en resistències
# En un circuit s'aplica una tensió de 12 V a aquestes resistències:
# resistencies = [100, 220, 470, 1000]
# Fent servir la llei d'Ohm (I = V / R) i un bucle for, calcula i imprimeix
# el corrent que circula per cada resistència, en ampers.
v = 12
resistencies = [100, 220, 470, 1000]
corrents = []
for r in resistencies:
    corrents.append(v/r)
print(f'corrents: {corrents}')

# Exercici 8: Mostres que superen el llindar de soroll
# Un receptor ha mesurat aquests nivells de soroll (en dBm):
# nivells_soroll = [-92, -85, -78, -95, -81, -88]
# Compta, amb un bucle for, quantes mostres superen el llindar de -80 dBm
# (és a dir, tenen un valor més gran que -80) i imprimeix el resultat.
nivells_soroll = [-92, -85, -78, -95, -81, -88]
count = 0
for nivel in nivells_soroll:
    if nivel > -80: count += 1
print(f'{count} superen el llindar de -80 dBm')

# Exercici 9: Càlcul de la taxa d'error de bits
# Compara els bits transmesos i rebuts:
# bits_transmesos = [1, 0, 1, 1, 0, 0, 1, 0]
# bits_rebuts =     [1, 0, 0, 1, 0, 1, 1, 0]
# Fent servir un bucle for i els índexs de les llistes, compta quants bits
# són diferents. Calcula i imprimeix la taxa d'error (bits diferents / total de bits).
bits_transmesos = [1, 0, 1, 1, 0, 0, 1, 0]
bits_rebuts =     [1, 0, 0, 1, 0, 1, 1, 0]
diff_count = 0
for idx, bit in enumerate(bits_transmesos):
    if bit == bits_rebuts[idx]: diff_count += 1
print(f'Taxa d\'error {diff_count / len(bits_transmesos)}')

# Exercici 10: Període d'un senyal
# Donades les freqüències següents, en hertzs:
# frequencies = [50, 100, 500, 1000]
# Fent servir un bucle for, calcula el període de cada senyal amb la fórmula
# T = 1 / f i imprimeix cada freqüència amb el seu període en segons.
frequencies = [50, 100, 500, 1000]
periodes = []
for f in frequencies:
    periodes.append(1/f)
print(f'periodes: {periodes}')
