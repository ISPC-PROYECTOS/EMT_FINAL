from .conexion_bd import conectar_base_datos, cerrar_conexion
from .mostrar_tablas import mostrar_productos_granel_disponibles, mostrar_productos_fraccionados_disponibles

def consultar_stock():
    salir = False  
    while not salir:    
        print("Ingrese la opción de STOCK que desea CONSULTAR: ")
        print("1 - TOTAL")
        print("2 - GRANEL")
        print("3 - FRACCIONADO")
        print("4 - SALIR")
           
        tipo_stock1 = int(input("Ingrese una opción: "))

        if tipo_stock1 == 1:
            mostrar_productos_fraccionados_disponibles()
            consulta_total()
            print("\nConsulta STOCK TOTAL realizada con éxito.\n")
        elif tipo_stock1 == 2:
            mostrar_productos_granel_disponibles()
            print('DISPONIBLE: ')
            consulta_granel()
            print("\nConsulta STOCK GRANEL realizada con éxito.\n")
        elif tipo_stock1 == 3:
            mostrar_productos_fraccionados_disponibles()
            consulta_fraccionado()
            print("\nConsulta STOCK FRACCIONADO realizada con éxito.\n")
        elif tipo_stock1 == 4:
            print("Saliendo de la opción CONSULTA de STOCK...")
            salir = True 
        else:
            print("\nOpción incorrecta.\n")
            
# Consulta la tabla de presentaciones por nombre
def consulta_fraccionado():
    conn, cursor = conectar_base_datos() 
    if conn:
        try:
            query = "SELECT descripcion, cantidad, tamano, unidadmedida FROM stockagranel.presentaciones WHERE descripcion = %s"
            nombre = input('Ingresa el nombre del producto fraccionado: ').upper()
            print('')
            print("Descripción-Cant.-Tamaño-UM")
            values = (nombre,)
            cursor.execute(query, values)
            results = cursor.fetchall()
            for row in results:
                print(row)
        except Exception as e:
            print(f"Error al consultar el stock fraccionado: {e}")

# Consulta la tabla productos a granel por nombre
def consulta_granel():
    conn, cursor = conectar_base_datos() 
    if conn:
        try:
            query = "SELECT descripcion, cantidad, tamano, unidadmedida FROM stockagranel.productosgranel WHERE descripcion = %s"
            nombre = input('Ingresa el nombre del producto a granel: ').upper()
            print('')
            print("Descripción-Cant.-Tamaño-UM")
            values = (nombre,)
            cursor.execute(query, values)
            results = cursor.fetchall()
            for row in results:
                print(row)
        except Exception as e:
            print(f"Error al consultar el stock a granel: {e}")

# Consulta ambas tablas y trae el stock de cada depósito por identificador a granel
def consulta_total():
    conn, cursor = conectar_base_datos()  
    if conn:
        try:
            query = "SELECT p.descripcion, p.cantidad, p.tamano, p.unidadmedida, g.descripcion, g.cantidad, g.tamano, g.unidadmedida FROM stockagranel.presentaciones p INNER JOIN stockagranel.productosgranel g ON (p.idProductoGranel = g.idProductoGranel) WHERE p.descripcion = %s"  
            nombre = input('Ingresa el nombre del producto: ').upper()
            print('')
            print("DEPÓSITO FRACCIONADO---------DEPÓSITO GRANEL")
            print("Desc.-Cant.-Tamaño-UM-//-Desc.-Cant.-Tamaño-UM")
            value = (nombre,)
            cursor.execute(query, value)
            productos = cursor.fetchall()
            if productos:
                for producto in productos:
                    print(producto)
            else:
                print("No hay productos en la base de datos.")
        except Exception as e:
            print(f"Error al consultar el stock total: {e}")