from datetime import datetime, timedelta
from producto_clase import Producto

producto=Producto()

# Función para verificar productos próximos a vencer
def verificar_vencimiento(productos, dias_alerta=5):
    hoy = datetime.now()
    alertas = []

    for producto in productos:
        # Calcular la fecha de alerta
        fecha_alerta = producto.fecha_vencimiento - timedelta(days=dias_alerta)
        
        if hoy >= fecha_alerta and producto.cantidad > 0:
            alertas.append(f"Alerta: El producto '{producto.nombre}' está próximo a vencer el {producto.fecha_vencimiento.date()}.")

    return alertas

# Lista de productos
productos = [
    Producto("Arroz", datetime(2024, 11, 5), 20),
    Producto("Lentejas", datetime(2024, 10, 28), 15),
    Producto("Aceite", datetime(2024, 12, 15), 10)
]

# Ejecutar la verificación de vencimiento
alertas = verificar_vencimiento(productos)

# Imprimir las alertas
for alerta in alertas:
    print(alerta)
