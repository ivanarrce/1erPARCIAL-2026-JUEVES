from datetime import date
from Ejercicio5 import ProductoKwikE as ProductoKwikEBase

class ProductoKwikE(ProductoKwikEBase):
    def __str__(self) -> str:
        return (f"Producto: {self.descripcion} | ID: {self.id_producto} | "
                f"Precio: ${self.precio:.2f} | Stock: {self.stock}")

    def __eq__(self, otro) -> bool:
        if not isinstance(otro, ProductoKwikE):
            return False
        return self.id_producto == otro.id_producto and self.descripcion == otro.descripcion