from ayedfiuner.algoritmos.burbuja import ordenamiento_burbuja
from ayedfiuner.estructuras.circulo import Circulo
from ayedfiuner.estructuras.monticulo import MonticuloB
from ayedfiuner.algoritmos.busqueda_binaria import busqueda_binaria


# Ejemplo de uso del algoritmo de ordenamiento burbuja
lista = [64, 34, 25, 12, 22, 11, 90]
lista_ordenada = ordenamiento_burbuja(lista)
print("Lista ordenada:", lista_ordenada)


# Ejemplo de uso de la estructura Circulo
circulo1 = Circulo(1)
circulo5 = Circulo(5)


# Ejemplo de uso de la estructura MonticuloB
    # 1 - Crear un montículo mínimo e insertar elementos de a uno
monticulo = MonticuloB()
monticulo.insertar(5)
monticulo.insertar(3)
monticulo.insertar(8)
monticulo.insertar(1)

    # 2 - Crear un montículo máximo a partir de una lista dada
monticulo2 = MonticuloB(es_minimo=False)
monticulo2.construirMonticulo([3,4,5,7,9,1,2])


print("Radio del círculo de radio 1:", circulo1.get_radio())
print("Radio del círculo de radio 5:", circulo5.get_radio())

print("Área del círculo de radio 1:", circulo1.area())
print("Área del círculo de radio 5:", circulo5.area())


print("Montículo después de insertar elementos:", monticulo.mostrar())
    # 3 - Eliminar elementos de la raíz sucesivamente
monticulo.eliminar()
print("Montículo después de eliminar la raíz:", monticulo.mostrar())

print("Montículo máximo construido a partir de la lista:", monticulo2.mostrar())

# Ejemplo de uso del algoritmo de búsqueda binaria
lista_prueba = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print("Búsqueda binaria para el número 3:", busqueda_binaria(lista_prueba, 3))
print("Búsqueda binaria para el número 13:", busqueda_binaria(lista_prueba, 13))
print("Búsqueda binaria para el número 1:", busqueda_binaria(lista_prueba, 1))


