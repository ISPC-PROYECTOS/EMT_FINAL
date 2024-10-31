from datetime import datetime, timedelta
from producto_clase import Producto

# producto = Producto() NO HACE FALTA INSTANCIARLO ACÁ, SE INSTANCIA DIRECTAMENTE DENTRO DE LA LISTA

# Función para verificar productos próximos a vencer
def verificar_vencimiento(productos, dias_alerta = 5):
    hoy = datetime.now()
    alertas = []

    for producto in productos:
        # Calcular la fecha de alerta
        fecha_alerta = producto.fecha_vencimiento - timedelta(days = dias_alerta)
        
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

# PRUEBAS
if __name__ == '__main__':
    # Prueba 1: Producto próximo a vencer
    productos_prueba_1 = [Producto("Harina Integral", datetime.now() + timedelta(days=3), 10)]
    alertas_prueba_1 = verificar_vencimiento(productos_prueba_1, dias_alerta=5)
    print("\nPrueba 1 - Producto próximo a vencer:")
    print(alertas_prueba_1)

    # Prueba 2: Producto no próximo a vencer
    productos_prueba_2 = [Producto("Harina Integral", datetime.now() + timedelta(days=10), 10)]
    alertas_prueba_2 = verificar_vencimiento(productos_prueba_2, dias_alerta=5)
    print("\nPrueba 2 - Producto no próximo a vencer:")
    print(alertas_prueba_2)

    # Prueba 3: Producto ya vencido
    productos_prueba_3 = [Producto("Harina Integral", datetime.now() - timedelta(days=1), 10)]
    alertas_prueba_3 = verificar_vencimiento(productos_prueba_3, dias_alerta=5)
    print("\nPrueba 3 - Producto ya vencido:")
    print(alertas_prueba_3)

    # Prueba 4: Producto próximo a vencer pero sin stock
    productos_prueba_4 = [Producto("Harina Integral", datetime.now() + timedelta(days=3), 0)]
    alertas_prueba_4 = verificar_vencimiento(productos_prueba_4, dias_alerta=5)
    print("\nPrueba 4 - Producto próximo a vencer pero sin stock:")
    print(alertas_prueba_4)