def overlapping(list1, list2):
    for element1 in list1:
        for element2 in list2:
            if element1 == element2:
                return True
    return False


lista_a = [1, 2, 3, 4, 5]
lista_b = [5, 6, 7, 8, 9]

result = overlapping(lista_a, lista_b)
print(result)