from datetime import date
from Ejercicio6 import ProductoKwikE
from Ejercicio8 import ListaEnlazada

class KwikEMart:
    def __init__(self):
        self.pasillos = {
            "Bebidas": ListaEnlazada(),
            "Snacks": ListaEnlazada(),
            "Conveniencia": ListaEnlazada()
        }

    def agregar_producto(self, pasillo: str, producto: ProductoKwikE):
        if pasillo not in self.pasillos:
            self.pasillos[pasillo] = ListaEnlazada()
        self.pasillos[pasillo].agregar(producto)

    def buscar_por_id(self, id_producto: int):
        for pasillo, lista_prod in self.pasillos.items():
            for prod in lista_prod:  
                if prod.id_producto == id_producto:
                    return prod, pasillo
        return None, None

    def remover_producto(self, id_producto: int) -> bool:
        prod, pasillo = self.buscar_por_id(id_producto)
        if prod:
            self.pasillos[pasillo].eliminar(lambda p: p.id_producto == id_producto)
            return True
        return False

    def actualizar_stock(self, id_producto: int, nuevo_stock: int) -> bool:
        prod, _ = self.buscar_por_id(id_producto)
        if prod:
            prod.cambiar_datos(stock=nuevo_stock)
            return True
        return False

    def desechar_expirados_24h(self, fecha_referencia: date = None) -> int:
        hoy = fecha_referencia if fecha_referencia is not None else date.today()
        desechados = 0

        for pasillo, lista_prod in self.pasillos.items():
            ids_a_eliminar = []
            for prod in lista_prod:
                dias = (prod.fecha_vencimiento - hoy).days
                if dias <= 1:
                    ids_a_eliminar.append(prod.id_producto)

            for id_prod in ids_a_eliminar:
                eliminado = lista_prod.eliminar(lambda p: p.id_producto == id_prod)
                if eliminado:
                    print(f"Apu desechó: {eliminado.descripcion} (ID: {eliminado.id_producto})")
                    desechados += 1

        return desechados