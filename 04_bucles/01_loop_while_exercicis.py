###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.
i = 10
while i >= 1:
    print(f'{i}')
    i -= 1;

# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.
sum = 0
i = 1
while i <= 20:
    if i % 2 == 0:
        sum += i
    i += 1
print(f'Suma de parells entre 1 i 20: {sum}')

# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
num = int(input('Entra enter positiu: '))
factorial = 1
while num >= 1:
    factorial *= num
    num -= 1
print(f'El factorial es {factorial}')

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".
passw = ''
while len(passw) < 8:
    passw = input('Entra contrasenya (min 8 caràcters): ')
print('Contrasenya vàlida')

# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
num = int(input('Entra número: '))
i = 1
while i <= 10:
    print(f'{num}*{i} = {num*i}')
    i += 1

# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.
n = int(input('Entra enter positiu: '))
i = 2
while i <= n:
    is_prime = True
    div = 2
    while div*div <= i:
        if i % div == 0:
            is_prime = False
            break
        div += 1
    if is_prime:
        print(i)
    i += 1

# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.
sum = 0
i = int(input('Entra enter (0 per sortir): '))
while i != 0:
    sum += i
    i = int(input('Entra enter (0 per sortir): '))
print(f'Suma total: {sum}')

# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.
i = int(input('Entra enter positiu: '))
digits = 0
while i >= 1:
    digits += 1
    i /= 10
print(f'Nombre de xifres: {digits}')

# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.
fib_num = int(input('Quants termes de la seqüència de Fibonacci vols veure? '))
i = 0
prev = 0
curr = 1
print(0)
while i <= fib_num:
    print(curr)
    next = prev + curr
    prev = curr
    curr = next
    i += 1

# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.
secret_n = 7
guess = int(input('Adivina el nombre secret: '))
while guess != secret_n:
    if guess > secret_n:
        print('El nombre secret és més petit')
    else:
        print('El nombre secret és més gran')
    guess = int(input('Adivina el nombre secret: '))
print('Has encertat!')
