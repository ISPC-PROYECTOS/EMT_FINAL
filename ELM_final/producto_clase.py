class Producto:
    def __init__(self,id_producto,nombre,presentacion,cantidad_max, cantidad_min,fecha_vencimiento):
        self.__id_producto=id_producto
        self._nombre=nombre
        self.presentacion= presentacion
        self.cantidad_max=cantidad_max
        self.cantidad_min=cantidad_min

    def __str__(self):
        return f"{self._nombre} ({self.presentacion}): Vence el {self.fecha_vencimiento.date()}"
   


