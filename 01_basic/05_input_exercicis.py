###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.
technician = input("Introdueix el nom del tècnic: ")
network = input("Introdueix el nom de la xarxa: ")
print(f"El tècnic {technician} està instal·lant la xarxa {network}.")


# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.
link_len = float(input("Introdueix la longitud de l'enllaç en quilòmetres: ")) # No serveix per res?
vel_gbps = float(input("Introdueix la velocitat de transmissió en Gbps: "))
vel_gb = vel_gbps / 8 # 1 GB = 8 Gb
time_seconds = 1 / vel_gb # Segons per transmetre 1 GB
print(f"Cal {round(time_seconds, 2)} segons per transmetre 1 GB de dades.")


# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.
hours = float(input("Introdueix el nombre d'hores de feina: "))
hourly_rate = float(input("Introdueix el preu per hora: "))
material_cost = float(input("Introdueix el preu del material: "))
total_cost = hours * hourly_rate + material_cost
print(f"El cost total de la instal·lació és {round(total_cost, 2)}.")
