from datetime import date

class ProductoKwikE:
    def __init__(self, descripcion: str, id_producto: int, fecha_vencimiento: date, precio: float, stock: int):
        self.descripcion = str(descripcion)
        self.id_producto = int(id_producto)
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = float(precio)
        self.stock = int(stock)

    def cambiar_datos(self, descripcion: str = None, precio: float = None, stock: int = None):
        if descripcion is not None:
            self.descripcion = str(descripcion)
        if precio is not None:
            self.precio = float(precio)
        if stock is not None:
            self.stock = int(stock)

    def dias_para_expirar(self, fecha_referencia: date = None) -> int:
        hoy = fecha_referencia if fecha_referencia is not None else date.today()
        dias = (self.fecha_vencimiento - hoy).days

        if dias <= 0:
            print(f"[ALERTA] El producto '{self.descripcion}' (ID: {self.id_producto}) ha expirado.")
            self.stock = 0

        return dias