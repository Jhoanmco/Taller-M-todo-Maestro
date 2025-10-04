def busqueda_binaria(arr, objetivo):
    """
    Implementa la búsqueda binaria de forma recursiva.
    Asume que la lista 'arr' está ORDENADA.
    """
    # Caso base: la lista está vacía
    if not arr:
        return -1
    
    n = len(arr)
    mitad = n // 2
    
    # Caso base: el elemento se encuentra en la mitad
    if arr[mitad] == objetivo:
        return mitad
    
    # Caso recursivo: el elemento está en la mitad izquierda
    elif arr[mitad] > objetivo:
        # Se busca en la primera mitad
        return busqueda_binaria(arr[:mitad], objetivo)
        
    # Caso recursivo: el elemento está en la mitad derecha
    else:
        # Se busca en la segunda mitad y se ajusta el índice
        resultado = busqueda_binaria(arr[mitad+1:], objetivo)
        
        # Si se encuentra, se suma el desplazamiento para obtener el índice real
        return resultado if resultado == -1 else mitad + 1 + resultado

# Ejemplo de uso
lista_ordenada = [1, 5, 8, 12, 16, 23, 38, 56, 72, 91]
elemento_buscado = 23

indice = busqueda_binaria(lista_ordenada, elemento_buscado)

print(f"Lista: {lista_ordenada}")
if indice != -1:
    print(f"El elemento {elemento_buscado} se encontró en el índice: {indice}")
else:
    print(f"El elemento {elemento_buscado} no se encontró en la lista.")

# T(n) = T(n/2) + O(1)
