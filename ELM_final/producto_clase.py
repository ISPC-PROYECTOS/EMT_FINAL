# class Producto:
#     def __init__(self,id_producto,nombre,presentacion,cantidad_max, cantidad_min,fecha_vencimiento):
#         self.__id_producto=id_producto
#         self._nombre=nombre
#         self.presentacion= presentacion
#         self.cantidad_max=cantidad_max
#         self.cantidad_min=cantidad_min

#     def __str__(self):
#         return f"{self._nombre} ({self.presentacion}): Vence el {self.fecha_vencimiento.date()}"
   

# NO QUISE BORRAR LO ANTERIOR POR QUE TAL VEZ QUERÍAS USARLO EN ALGO, PERO LOS ATRIBUTOS TIENEN QUE COINCIDIR CON LO QUE DSP
# VAS A PASARLE A LA CLASE PARA INSTANCIARLO, Y DE ESTA FORMA SIRVE A COMO PLANTEASTE LA ALARMA, SINO NO ANDABA.
class Producto():
    def __init__(self, nombre, fecha_vencimiento, cantidad):
        self.nombre = nombre
        self.fecha_vencimiento = fecha_vencimiento
        self.cantidad = cantidad


    def __str__(self):
        f"{self._nombre}: Vence el {self.fecha_vencimiento.date()}"