###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
name = "router-A"
location = "datacenter"
ports = 15
is_on = True
print(f"El router {name} està encès a la ubicació {location} amb {ports} ports.")

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.
gb_total = 100
gb_consumed = 50
gb_remaining = gb_total - gb_consumed
print(f"Queden {gb_remaining} GB disponibles.")
gb_consumed = 65
gb_remaining = gb_total - gb_consumed
print(f"Queden {gb_remaining} GB disponibles.")
