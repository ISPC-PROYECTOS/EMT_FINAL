from .conexion_bd import conectar_base_datos
from .mostrar_tablas import mostrar_productos_fraccionados_disponibles

def registro_venta_actualizacion_stock(): 
    print('\nPRODUCTOS DISPONIBLES:\n ')
    print('ID - DESCRIP - CANT - TAMAÑO - UM...') 
    mostrar_productos_fraccionados_disponibles() 
    fecha_venta = input('Ingresa la fecha(AAAA-MM-DD): ')
    cantidad = int(input('Ingresa la cantidad: ')) 
    id_producto_fracc = int(input('Ingresa el ID del producto vendido: ')) 
    conn, cursor = conectar_base_datos()
    try:
        query_insert = "INSERT INTO registroventa (fechaventa, cantidad, idproductofracc) VALUES (%s, %s, %s)"
        values_insert = (fecha_venta, cantidad, id_producto_fracc) 
        cursor.execute(query_insert, values_insert)
        query_update = "UPDATE presentaciones SET cantidad = cantidad - %s WHERE idProductoFracc = %s" 
        values_update = (cantidad, id_producto_fracc)
        cursor.execute(query_update, values_update) 
        conn.commit()
        print("\nSU VENTA SE REGISTRÓ EXITOSAMENTE.\n")
    except Exception as e:
        print(f"Error al registrar la venta: {e}")
        conn.rollback() 