from .conexion_bd import conectar_base_datos, cerrar_conexion
from .mostrar_tablas import mostrar_productos_granel_disponibles, mostrar_productos_fraccionados_disponibles

def actualizar_stock():
    salir = False  
    while not salir: 
        print("Ingrese la opción de STOCK que desea ACTUALIZAR: ")
        print("1 - GRANEL")
        print("2 - FRACCIONADO")
        print("3 - SALIR")
        
        while True:
            try:
                tipo_stock2 = int(input("Ingrese una opción: "))
                if tipo_stock2 in [1, 2, 3]:
                    break
                else:
                    print("\nOpción incorrecta. Por favor elija 1, 2 o 3.")
            except ValueError:
                print("\nPor favor, ingrese un número válido.")

        if tipo_stock2 == 1:
            mostrar_productos_granel_disponibles()
            actualizar_granel()
            print("\nActualización STOCK GRANEL realizada con éxito.\n")
        elif tipo_stock2 == 2:
            mostrar_productos_fraccionados_disponibles()
            actualizar_fraccionado()
            print("\nActualización STOCK FRACCIONADO realizada con éxito.\n")
        elif tipo_stock2 == 3:
            print("Saliendo de la opción ACTUALIZACIÓN de STOCK...")
            salir = True  

def actualizar_granel():
    conn, cursor = conectar_base_datos()
    while True:
        try:
            id = int(input('Ingresa el ID del producto a actualizar: '))
            cantidad = int(input('Ingresa la cantidad a agregar: '))
            if cantidad <= 0:
                print("La cantidad debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Por favor, ingresa un número válido.")
    try:
        query = "UPDATE productosgranel SET cantidad = cantidad + %s WHERE idproductogranel = %s"
        values = (cantidad, id)
        cursor.execute(query, values)
        conn.commit()
        print(f"Stock del producto con ID {id} actualizado en {cantidad} unidades.")
    except Exception as e:
        print(f"Error al actualizar el stock: {e}")
        conn.rollback()  

def actualizar_fraccionado():
    conn, cursor = conectar_base_datos()
    while True:
        try:
            id = int(input('Ingresa el ID del producto fraccionado a actualizar: '))
            cantidad = int(input('Ingresa la cantidad a agregar: '))
            if cantidad <= 0:
                print("La cantidad debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Por favor, ingresa un número válido.")

    try:
        query = "UPDATE presentaciones SET cantidad = cantidad + %s WHERE idproductofracc = %s"
        values = (cantidad, id)
        cursor.execute(query, values)
        conn.commit()
        print(f"Stock del producto fraccionado con ID {id} actualizado en {cantidad} unidades.")
    except Exception as e:
        print(f"Error al actualizar el stock: {e}")
        conn.rollback() 