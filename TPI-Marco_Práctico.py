import random
lista_desordenada = []

# Generación de una lista desordenada con 50 números aleatorios entre 0 y 100
for i in range(0,20):
    lista_desordenada.append(random.randint(0, 50))


# Algoritmo de ordenación por inserción
def ordenamiento_insercion(lista_desordenada):
    for i in range(1, len(lista_desordenada)):
        actual = lista_desordenada[i]
        index = i 
        """
        Este bucle intercambia los dos número de posición 
        mientras que el número anterior sea más grande que el número actual
        """
        while index > 0 and lista_desordenada[index - 1] > actual:
            lista_desordenada[index] = lista_desordenada[index - 1]
            index = index - 1
        lista_desordenada[index] = actual
    return lista_desordenada

print("lista desordenada:", lista_desordenada)
lista_ordenada = ordenamiento_insercion(lista_desordenada)
print("lista ordenada:   ", lista_ordenada)

# Algoritmo de búsqueda binaria
def busqueda_binaria(lista_ordenada, objetivo, inicio, fin ):
    if inicio > fin:
        return -1

    centro = (inicio + fin) // 2
    if lista_ordenada[centro] == objetivo:
        return centro
    elif lista_ordenada[centro] < objetivo:
        return busqueda_binaria(lista_ordenada, objetivo, centro + 1, fin)
    else:
        return busqueda_binaria(lista_ordenada, objetivo, inicio, centro - 1)     

# Ejemplo de uso
numero_objetivo = 17
inicio_busqueda = 0
fin_busqueda = len(lista_ordenada) - 1

resultado = busqueda_binaria(lista_ordenada, numero_objetivo, inicio_busqueda, fin_busqueda)

if resultado != -1:
    print(f"El número {numero_objetivo} se encuentra en la posición {resultado}.")
else:
    print(f"El númeor {numero_objetivo} NO se encuentra en la lista.")