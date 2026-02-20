class MonticuloB:
    """
    Implementación de un montículo binario configurable.
    Puede funcionar como minimo o maximo según el parámetro es_minimo.
    """

    def __init__(self, es_minimo=True):
        # Lista interna (índice 0 no utilizado)
        self._listaMonticulo = [0]
        self._tamanoActual = 0

        # True → es minimo
        # False → es maximo
        self.__es_minimo = es_minimo

    def infiltArriba(self, i):
        """
        Ajusta el elemento hacia arriba hasta restaurar
        la propiedad del montículo.
        """
        while i // 2 > 0:
            if (self.__es_minimo and self._listaMonticulo[i] < self._listaMonticulo[i // 2]) or \
               (not self.__es_minimo and self._listaMonticulo[i] > self._listaMonticulo[i // 2]):

                # Intercambio con el padre
                self._listaMonticulo[i], self._listaMonticulo[i // 2] = \
                    self._listaMonticulo[i // 2], self._listaMonticulo[i]

            i = i // 2

    def insertar(self, k):
        """
        Inserta un nuevo elemento y lo reubica correctamente.
        """
        self._listaMonticulo.append(k)
        self._tamanoActual += 1
        self.infiltArriba(self._tamanoActual)

    def infiltAbajo(self, i):
        """
        Ajusta el elemento hacia abajo para restaurar
        la propiedad del montículo.
        """
        while (i * 2) <= self._tamanoActual:
            hm = self._hijoPrioritario(i)

            if (self.__es_minimo and self._listaMonticulo[i] > self._listaMonticulo[hm]) or \
               (not self.__es_minimo and self._listaMonticulo[i] < self._listaMonticulo[hm]):

                # Intercambio con el hijo correspondiente
                self._listaMonticulo[i], self._listaMonticulo[hm] = \
                    self._listaMonticulo[hm], self._listaMonticulo[i]

            i = hm

    def _hijoPrioritario(self, i):
        """
        Devuelve el índice del hijo que corresponde comparar:
        - el menor si es minimo
        - el mayor si es maximo
        """
        if i * 2 + 1 > self._tamanoActual:
            return i * 2
        else:
            if (self.__es_minimo and self._listaMonticulo[i * 2] < self._listaMonticulo[i * 2 + 1]) or \
               (not self.__es_minimo and self._listaMonticulo[i * 2] > self._listaMonticulo[i * 2 + 1]):
                return i * 2
            else:
                return i * 2 + 1

    def eliminar(self):
        """
        Elimina y devuelve el elemento en la raíz.
        - En minimo → devuelve el mínimo.
        - En maximo → devuelve el máximo.
        """
        if self._tamanoActual == 0:
            raise IndexError("El montículo está vacío")

        valorSacado = self._listaMonticulo[1]
        self._listaMonticulo[1] = self._listaMonticulo[self._tamanoActual]
        self._tamanoActual -= 1
        self._listaMonticulo.pop()
        self.infiltAbajo(1)

        return valorSacado

    def construirMonticulo(self, unaLista):
        """
        Construye el montículo a partir de una lista dada
        utilizando heapify bottom-up.
       """
        i = len(unaLista) // 2
        self._tamanoActual = len(unaLista)
        self._listaMonticulo = [0] + unaLista[:]

        while i > 0:
            self.infiltAbajo(i)
            i -= 1

    def estaVacio(self):
        """Devuelve True si el montículo está vacío."""
        return self._tamanoActual == 0

    def verRaiz(self):
        """Devuelve el elemento de la raíz sin eliminarlo."""
        if self._tamanoActual == 0:
            return None
        return self._listaMonticulo[1]
    
    def mostrar(self):
        """Devuelve una lista con los elementos actuales del montículo"""
        return self._listaMonticulo[1:]
    

if __name__ == "__main__":

    print("Probando MIN-HEAP")
    min_heap = MonticuloB(es_minimo=True)
    min_heap.construirMonticulo([9, 5, 6, 2, 3])

    print(min_heap.mostrar())

    # Muestro el contenido del montículo ordenado (eliminando las raíces sucesivamente)
    while not min_heap.estaVacio():
        print(min_heap.eliminar(), end=" ")
    
    print("\n")
    print("Probando MAX-HEAP")
    max_heap = MonticuloB(es_minimo=False)
    max_heap.construirMonticulo([9, 5, 6, 2, 3])
    
    print(max_heap.mostrar())
    
    # Muestro el contenido del montículo ordenado (eliminando las raíces sucesivamente)
    while not max_heap.estaVacio():
        print(max_heap.eliminar(), end=" ")