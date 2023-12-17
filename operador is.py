lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

print(lista1 is lista2)  # Output: False (aunque los valores son iguales, las listas son objetos diferentes)
print(lista1 is lista3)  # Output: True (lista1 y lista3 apuntan al mismo objeto en la memoria)
