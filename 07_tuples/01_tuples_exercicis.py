# 📝 Exercicis sobre tuples

# 1️⃣ Crea una tupla amb els noms de 5 ciutats i mostra la segona i la penúltima ciutat.
ciutats = ("Barcelona", "Madrid", "Valencia", "Granada", "Sevilla")
print(ciutats[1])
print(ciutats[3])

# 2️⃣ Donada una tupla amb números enters, compta quantes vegades apareix el número 3 a la tupla.
nums: tuple[int, ...] = (1, 3, 5, 8, 3, 10, 18, 3, 9, 28, 32)
print(nums.count(3))

# 3️⃣ Crea una funció que rebi una tupla amb números i retorni una tupla nova amb els números ordenats de menor a major.
def sort_tuple(tuple: tuple[int, ...]):
    return sorted(tuple) # Parametre tipat per obtenir intellisense
print(sort_tuple(nums))
