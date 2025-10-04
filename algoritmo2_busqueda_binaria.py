def busqueda_binaria(arr, objetivo):
    #caso base: la lista vacía
    if not arr:
        return -1

    n = len(arr)
    mitad = n // 2

    if arr[mitad] == objetivo:
        return mitad
    elif arr[mitad] > objetivo:
        return busqueda_binaria(arr[:mitad], objetivo)
    else:
        resultado = busqueda_binaria(arr[mitad+1:], objetivo)
        return resultado if resultado == -1 else mitad + 1 + resultado

#ejemplo
lista_ordenada = [1, 5, 8, 12, 16, 23, 38, 56, 72, 91]
elemento_buscado = 12

indice = busqueda_binaria(lista_ordenada, elemento_buscado)

print(f"Lista: {lista_ordenada}")
if indice != -1:
    print(f"El elemento {elemento_buscado} se encontró en el índice: {indice} (indices: 0,1,2, ..., n)")
else:
    print(f"El elemento {elemento_buscado} no se encontró en la lista.")

# T(n) = T(n/2) + O(1)
