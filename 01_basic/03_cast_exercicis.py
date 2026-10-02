###
# Exercicis - conversió de tipus (casting)
# Completa els exercicis següents convertint dades entre tipus.
###

# Exercici 1
# Demana a l'usuari quants paquets ha rebut un encaminador. Converteix el valor
# introduït a un nombre enter, suma-hi 1200 paquets i mostra el total.
packets = int(input("Introdueix el nombre de paquets rebuts: "))
total = packets + 1200
print(f"El total de paquets és: {total}")

# Exercici 2
# Demana a l'usuari la velocitat d'una connexió en Mbps. Converteix el valor
# introduït a un nombre decimal i calcula la velocitat equivalent en MB/s
# dividint-la per 8. Mostra el resultat.
vel_mbps = float(input("Introdueix la velocitat en Mbps: "))
vel_mb = vel_mbps / 8
print(f"La velocitat equivalent en MB/s és: {round(vel_mb, 2)}")
