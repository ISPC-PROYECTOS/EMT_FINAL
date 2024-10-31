from .conexion_bd import conectar_base_datos

def mostrar_productos_fraccionados_disponibles():
    conn, cursor = conectar_base_datos()
    try:
        query = """
        SELECT 
            idProductoFracc, 
            descripcion, 
            cantidad, 
            tamano, 
            unidadMedida, 
            cantidadMax, 
            cantidadMin, 
            idProductoGranel 
        FROM 
            stockagranel.presentaciones
        """
        cursor.execute(query)
        productos = cursor.fetchall()
        
        if productos:
            print("\nPRODUCTOS FRACCIONADOS DISPONIBLES:")
            for producto in productos:
                print(producto)
        else:
            print("No hay productos fraccionados en la base de datos.")
    except Exception as e:
        print(f"Error al mostrar productos fraccionados: {e}")

def mostrar_productos_granel_disponibles():
    conn, cursor = conectar_base_datos()
    try:
        query = """
        SELECT 
            idProductoGranel, 
            descripcion, 
            cantidad, 
            tamano, 
            unidadMedida, 
            cantidadMax, 
            cantidadMin, 
            idCategoria 
        FROM 
            productosgranel
        """
        cursor.execute(query)
        productos = cursor.fetchall()
        
        if productos:
            print("\nPRODUCTOS A GRANEL DISPONIBLES:")
            for producto in productos:
                print(producto)
        else:
            print("No hay productos a granel en la base de datos.")
    except Exception as e:
        print(f"Error al mostrar productos a granel: {e}")

def mostrar_categorias():
    conn, cursor = conectar_base_datos()
    try:
        query = "SELECT idCategoria, categoria FROM categorias"
        cursor.execute(query)
        categorias = cursor.fetchall()
        
        if categorias:
            print("\nCATEGORÍAS DISPONIBLES:")
            for categoria in categorias:
                print(categoria)
        else:
            print("No hay categorías en la base de datos.")
    except Exception as e:
        print(f"Error al mostrar categorías: {e}")

def mostrar_proveedores():
    conn, cursor = conectar_base_datos()
    try:
        query = """
        SELECT 
            CUIT, 
            proveedor, 
            direccion, 
            telefono, 
            email, 
            tiempoDeEntrega 
        FROM 
            proveedores
        """
        cursor.execute(query)
        proveedores = cursor.fetchall()
        
        if proveedores:
            print("\nPROVEEDORES DISPONIBLES:")
            for proveedor in proveedores:
                print(proveedor)
        else:
            print("No hay proveedores en la base de datos.")
    except Exception as e:
        print(f"Error al mostrar proveedores: {e}")