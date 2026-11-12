###
# EXERCICIS (funcions)
###

# Exercici 1: Funció de salutació
# Crea una funció saludar_a(nom, salutacio="Hola") que imprimeixi la salutació seguida del nom.
# Prova-la amb i sense el segon argument.
def saludar_a(nom, salutacio="Hola"):
    print(f'{salutacio} {nom}!')

saludar_a('undead one', 'Wussup')

# Exercici 2: Parell o senar
# Crea una funció es_parell(numero) que retorni True si el número és parell i False si no ho és.
def es_parell(numero):
    return numero % 2 == 0

# Exercici 3: Mitjana d'una llista
# Crea una funció mitjana(numeros) que rebi una llista de números i en retorni la mitjana.
# Fes servir un bucle for.
def mitjana(numeros):
    sum = 0
    for n in numeros: sum += n
    return sum / len(numeros)

# Exercici 4: Suma amb *args
# Crea una funció sumar_tot(*args) que retorni la suma de tots els números rebuts.
# Prova-la amb 2, 5 i 10 arguments.
def sumar_tot(*args):
    sum = 0
    for arg in args: sum += arg
    return sum
print(sumar_tot(1, 2))
print(sumar_tot(1, 2, 3, 4, 5))
print(sumar_tot(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# Exercici 5: Taula de multiplicar
# Crea una funció taula_multiplicar(numero, limit=10) que imprimeixi la taula de multiplicar
# del número fins al límit indicat, fent servir range().
def taula_multiplicar(numero, limit=10):
    for n in range(1, limit + 1):
        print(f'{n}*{numero} = {n*numero}')

taula_multiplicar(10)

# Exercici 6: Informació amb **kwargs
# Crea una funció mostrar_perfil(**kwargs) que imprimeixi cada parella clau: valor.
# Crida-la amb les dades d'un estudiant (nom, edat, grau).
def mostrar_perfil(**kwargs):
     for key, val in kwargs.items():
         print(f"{key}: {val}")

mostrar_perfil(nom='Undead one', edat=20, grau='Teleco')

# Exercici 7: Reconvertir exercicis anteriors
# Torna a l'exercici del factorial (while) i del màxim d'una llista (for)
# i converteix-los en funcions que retornin el resultat.
def factorial(n):
    f = 1
    while n > 0:
        f *= n
        n -= 1
    return f

# Exercici 8: Comptar vocals
# Crea una funció comptar_vocals(text) que rebi una cadena de text i retorni quantes vocals
# (a, e, i, o, u) conté. Ha de funcionar tant amb majúscules com amb minúscules.
def comptar_vocals(text):
    vocals = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in text:
        if char in vocals: count += 1
    return count

print(f'"Hello" te {comptar_vocals("Hello")} vocals.')

# Exercici 9: Retorn múltiple (mínim i màxim)
# Crea una funció minim_i_maxim(numeros) que rebi una llista de números i retorni tant el valor
# mínim com el valor màxim alhora. Desempaqueta el resultat en dues variables.
def minim_i_maxim(numeros):
    min_val = numeros[0]
    max_val = numeros[0]
    for n in numeros[1:]:
        min_val = min(min_val, n)
        max_val = max(max_val, n)
    return min_val, max_val

nums = [20, 14, 54, 10, 18, 7, 9]
min_val, max_val = minim_i_maxim(nums)
print(f'Valor minim i maxim de {nums} son {min_val} i {max_val} respectivament.')

# Exercici 10: Palíndrom
# Crea una funció es_palindrom(text) que retorni True si una paraula es llegeix igual d'esquerra a dreta
# que de dreta a esquerra (ignorant majúscules i minúscules), i False en cas contrari.
def es_palindrom(text: str):
    normalitzat = text.lower()
    return normalitzat == normalitzat[::-1]

print(f'"Oro" es palindrom: {es_palindrom("Oro")}')
print(f'"Hola" es palindrom: {es_palindrom("Hola")}')
