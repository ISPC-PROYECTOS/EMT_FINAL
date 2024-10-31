import mysql.connector


def check_stock():
    try:
   
        cnx = mysql.connector.connect(user="root", password="vicki1996", host="localhost", database="emyl")
        cursor = cnx.cursor()


        print("Conexión a la base de datos exitosa.")


       
        query = ("SELECT descripcion, cantidad, cantidadMin FROM productosgranel WHERE cantidad <= cantidadMin")
        cursor.execute(query)


        print("Consulta ejecutada con éxito.")


   
        productos = cursor.fetchall()
        if productos:
            for (descripcion, cantidad, cantidadMin) in productos:
                print(f"¡Alerta! El producto '{descripcion}' tiene una cantidad de {cantidad}, que está por debajo del mínimo requerido de {cantidadMin}.")
        else:
            print("No se encontraron productos por debajo de la cantidad mínima.")


        cursor.close()
        cnx.close()


    except mysql.connector.Error as err:
        print(f"Error: {err}")


# Llama a la función para verificar el stock
check_stock()