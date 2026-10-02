###
# EXERCICIS
###

# Exercici 1: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble
dbm = float(input("Introdueix el nivell de senyal en dBm: "))
if dbm >= -50:
    print("Excel·lent")
elif dbm >= -67:
    print("Bona")
elif dbm >= -75:
    print("Feble")
else:
    print("Molt feble")

# Exercici 2: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.
power = float(input("Introdueix la potència òptica rebuda en dBm: "))
if power > -8:
    print("Massa alt")
elif power >= -27:
    print("Acceptable")
else:
    print("Massa baix")

# Exercici 3: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.
plan_gb = 20 # GB
consumed_gb = float(input("Introdueix el consum de dades en GB: "))
if consumed_gb <= plan_gb:
    print("Dins del límit")
else:
    print("Has superat el límit")
    additional_gb = round(abs(consumed_gb - plan_gb), 2)
    print(f"Has consumit {additional_gb} GB addicionals")

# Exercici 4: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.
los_on = int(input("Introdueix si l'indicador LOS està encès (1/0): "))
internet_on = int(input("Introdueix si l'indicador d'Internet està encès (1/0): "))
if los_on == 1 and internet_on == 1:
    print("La connexió sembla funcionar correctament")
elif los_on == 1 and internet_on == 0:
    print("Cal revisar el cable de fibra")
elif los_on == 0 and internet_on == 1:
    print("Cal revisar el servei del proveïdor")
else:
    print("No s'han introduït valors vàlids")



# Exercici 5: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.
battery_lvl = float(input("Introdueix el percentatge de bateria disponible: "))
if battery_lvl < 0 or battery_lvl > 100:
    print("No s'han introduït valors vàlids")
elif battery_lvl < 20:
    print("El nivell de bateria és crític")
elif battery_lvl < 50:
    print("El nivell de bateria és baix")
else:
    print("El nivell de bateria és suficient")
