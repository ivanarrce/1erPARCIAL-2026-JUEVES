class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig


class IteradorListaEnlazada:
    def __init__(self, primer_nodo):
        self.actual = primer_nodo

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual is None:
            raise StopIteration
        dato = self.actual._elem
        self.actual = self.actual._nxt
        return dato


class ListaEnlazada:
    def __init__(self):
        self.header = Nodo(0)
        self._tam = 0

    def __len__(self):
        return self._tam

    def es_vacia(self):
        return self.header._nxt is None

    def __iter__(self):
        return IteradorListaEnlazada(self.header._nxt)

    def agregar(self, dato):
        nuevo = Nodo(dato)
        actual = self.header
        while actual._nxt is not None:
            actual = actual._nxt
        actual._nxt = nuevo
        self._tam += 1

    def eliminar(self, criterio_o_dato):
        anterior = self.header
        actual = self.header._nxt

        while actual is not None:
            coincide = (criterio_o_dato(actual._elem) 
                        if callable(criterio_o_dato) 
                        else actual._elem == criterio_o_dato)
            if coincide:
                anterior._nxt = actual._nxt
                self._tam -= 1
                return actual._elem
            anterior = actual
            actual = actual._nxt

        return None