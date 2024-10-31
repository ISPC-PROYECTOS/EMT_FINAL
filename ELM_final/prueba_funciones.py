import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mysql.connector import Error
from BBDD_agranel import conexion_bd

def obtener_datos_ventas():
    conn, cursor = conexion_bd.conectar_base_datos()
    
    # Consulta SQL para obtener la cantidad vendida de cada producto del mes actual
    query = """
    SELECT p.descripcion, SUM(rv.cantidad) AS total_vendido
    FROM registroventa rv
    JOIN presentaciones p ON rv.idProductoFracc = p.idProductoFracc
    WHERE rv.fechaVenta >= CURDATE() - INTERVAL DAY(CURDATE()) - 1 DAY
    AND rv.fechaVenta < CURDATE() + INTERVAL 1 DAY
    GROUP BY p.idProductoFracc, p.descripcion;
    """

    try:
        cursor.execute(query)
        resultados = cursor.fetchall()
    
        datos_ventas = []
        
        for producto, total in resultados:
            datos_ventas.append({'producto': producto, 'total_vendido': total})
        
        return datos_ventas  
    except Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        return []  # Devolver una lista vacía en caso de error
    finally:
        conexion_bd.cerrar_conexion(conn, cursor)

def consulta_total():
    conn, cursor = conexion_bd.conectar_base_datos()  
    if conn:
        try:
            query = """
            SELECT p.descripcion,
                  p.cantidad AS cantidad_fraccionado,
                  p.tamano AS tamano_fraccionado,
                  p.unidadmedida AS unidad_medida_fraccionado,
                  g.descripcion AS descripcion_granel,
                  g.cantidad AS cantidad_granel,
                  g.tamano AS tamano_granel,
                  g.unidadmedida AS unidad_medida_granel
            FROM stockagranel.presentaciones p
            INNER JOIN stockagranel.productosgranel g ON (p.idProductoGranel = g.idProductoGranel)
            WHERE p.descripcion = %s;
            """  
            nombre = input('Ingresa el nombre del producto: ').upper()
            print('')
            print("DEPÓSITO FRACCIONADO        | DEPÓSITO GRANEL")
            print("Desc.        | Cant. | Tamaño | UM  || Desc.        | Cant. | Tamaño | UM")
            print("-" * 75)
            
            value = (nombre,)
            cursor.execute(query, value)
            productos = cursor.fetchall()

            stock_total = 0  # Inicializa el stock total
            if productos:
                for producto in productos:
                    descripcion_fraccionado, cantidad_fraccionado, tamano_fraccionado, unidad_medida_fraccionado, descripcion_granel, cantidad_granel, tamano_granel, unidad_medida_granel = producto
                    
                    # Calcula el stock para cada producto fraccionado
                    stock_fraccionado = cantidad_fraccionado * tamano_fraccionado
                    # Calcula el stock para el producto granel, convirtiendo kg a g
                    stock_granel = (cantidad_granel * tamano_granel * 100) / 3 

                    # Suma al stock total
                    stock_total += (stock_fraccionado + stock_granel) / 1000
                    
                    # Imprime los productos con formato alineado
                    print(f"{descripcion_fraccionado:<12} | {cantidad_fraccionado:<5} | {tamano_fraccionado:<6} | {unidad_medida_fraccionado:<2} || {descripcion_granel:<12} | {cantidad_granel:<5} | {tamano_granel:<6} | {unidad_medida_granel:<2}")
                    print(f"Stock Fraccionado: {stock_fraccionado} g, Stock Granel: {stock_granel:.2f} g")
                print(f"\nSTOCK TOTAL: {stock_total:.2f} kg")
            else:
                print("No hay productos en la base de datos.")
                stock_total = 0  
        except Exception as e:
            print(f"Error al consultar el stock total: {e}")
            stock_total = 0  
        finally:
            conexion_bd.cerrar_conexion(conn, cursor)
    return stock_total  # Devuelve el stock total calculado

def verificar_abastecimiento(stock_total, punto_pedido, producto):
    if stock_total < punto_pedido:
        print(f"¡Alerta de abastecimiento para {producto}! El stock total es de {stock_total} kg, que está por debajo del punto de pedido de {punto_pedido} kg.")

if __name__ == '__main__':
    ventas = obtener_datos_ventas()
    
    for venta in ventas:
        producto = venta['producto']
        total_vendido = venta['total_vendido']
        print(f"Producto: {producto}, Total Vendido: {total_vendido}")
    
        dias_trabajados = 27
        
        demanda_diaria = total_vendido / dias_trabajados if dias_trabajados > 0 else 0
        print(f"Demanda diaria media para {producto}: {round(demanda_diaria)}")

        plazo_de_entrega = 7
        
        stock_seguridad = plazo_de_entrega * demanda_diaria
        print(f"Stock de seguridad para {producto}: {round(stock_seguridad)}")

        punto_pedido = round((demanda_diaria * plazo_de_entrega) + stock_seguridad)
        print(f"Punto de pedido para {producto}: {round(punto_pedido)}")

        stock_actual = consulta_total()

        # Verificar abastecimiento
        verificar_abastecimiento(stock_actual, punto_pedido, producto)