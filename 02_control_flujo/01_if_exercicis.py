###
# EXERCICIS
###

# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.
a = float(input('Entra el primer nombre: '))
b = float(input('Entra el segon nombre: '))
if a == b:
    print(f'{a} y {b} son iguals')
elif a > b:
    print(f'{a} és més gran que {b}')
else:
    print(f'{b} és més gran que {a}')

# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /).
# Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).
a = float(input('Entra el primer nombre: '))
b = float(input('Entra el segon nombre: '))
op = input('Entra operació (+, -, *, /): ')
if op == '+':
    print(a+b)
elif op == '-':
    print(a-b)
elif op == '*':
    print(a*b)
elif b != 0:
    print(a/b)
else:
    print('No es pot dividir per 0!')

# Exercici 3: Any de traspàs
# Demana a l'usuari que introdueixi un any i determina si és de traspàs.
# Un any és de traspàs si és divisible per 4, excepte si és divisible per 100
# però no per 400.
year = int(input('Entra un any: '))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f'{year} es un any de traspàs')
else:
    print(f'{year} no es un any de traspàs')

# Exercici 4: Classificar edats
# Demana a l'usuari que introdueixi una edat i classifica-la en:
# - Nadó (0-2 anys)
# - Infant (3-12 anys)
# - Adolescent (13-17 anys)
# - Adult (18-64 anys)
# - Persona gran (65 anys o més)
age = int(input('Entra edat: '))
if age < 0:
    print('Edat invalida')
elif age <= 2:
    print('Nadó')
elif age <= 12:
    print('Infant')
elif age <= 17:
    print('Adolescent')
elif age <= 64:
    print('Adult')
else:
    print('Persona gran')

# Exercici 5: Qualitat del senyal Wi-Fi
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

# Exercici 6: Nivell de recepció d'una connexió de fibra òptica
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

# Exercici 7: Consum mensual de dades mòbils
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

# Exercici 8: Diagnòstic d'una connexió de fibra
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



# Exercici 9: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
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

# Exercici 10: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.
latency_ms = float(input("Latencia en ms: "))
lost_pkgs_percent = float(input("Percentatge de paquets perduts: "))
if latency_ms < 0 or lost_pkgs_percent < 0 or lost_pkgs_percent > 100:
    print("Connexió rebutjada")
elif latency_ms <= 30 and lost_pkgs_percent <= 1:
    print("Connexió excel·lent")
elif latency_ms <= 80 and lost_pkgs_percent <= 3:
    print("Connexió bona")
elif latency_ms <= 150 and lost_pkgs_percent <= 5:
    print("Connexió acceptable")
else:
    print("Connexió deficient")


# Exercici 11: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.
plan_type = input("Pla bàsic o plus? ")
consumed_gb = float(input("Consum mensual en GB: "))
tota_cost_eur = 0.0
if consumed_gb < 0:
    print("Consum invalid (negatiu)")
elif plan_type == 'basic':
    additional_gb = (consumed_gb - 10) if consumed_gb > 10 else 0
    total_cost_eur = 10 + additional_gb*1.5
    print(f'Cost total: {total_cost_eur}')
elif plan_type == 'plus':
    additional_gb = (consumed_gb - 30) if consumed_gb > 30 else 0
    total_cost_eur = 20 + additional_gb*1.5
    print(f'Cost total: {total_cost_eur}')
else:
    print("Pla invalid (basic o plus)")



# Exercici 12: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.
is_acc_active = int(input("El compte està actiu? "))
is_pass_ok = int(input("La contrasenya és correcta? "))
is_double_verified = 0
if is_acc_active == 0:
    print("Accés denegat: compte no és actiu")
elif is_pass_ok == 0:
    print("Accés denegat: contrasenya incorrecta")
else:
    is_double_verified = int(input("El codi de doble verificació és correcte? "))
    if is_double_verified == 0:
        print("Accés denegat: codi falla")
    else:
        print("Accés permes")



# Exercici 13: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.

# EL MATEIX QUE L'EXERCISI 4



# Exercici 14: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.
is_critical_svc_affected = input("La incidència afecta un servei crític? ")
affected_users = int(input("Nombre d'usuaris afectats: "))
is_alternative_available = int(input("Hi ha una alternative de connexió disponible? "))
if affected_users < 0:
    print("Error: introdueix un valor positiu d'usuaris")
elif (is_alternative_available == 0) and (is_critical_svc_affected == 1 or affected_users >= 50):
    print("Prioritat crítica!")
elif affected_users >= 10 or is_critical_svc_affected == 1:
    print("Prioritat alta!")
else:
    print("Prioritat baixa")
