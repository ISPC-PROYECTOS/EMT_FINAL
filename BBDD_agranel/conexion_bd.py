import mysql.connector
from mysql.connector import Error

HOST = "localhost"
USER = "root"
PASSWORD = "112233"
BD = "stockagranel"

class ErrorConexion(Exception):
    pass

def conectar_base_datos():
    try:
        conn = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=BD
        )
        if conn.is_connected():
            print("Conexión a la base de datos exitosa.")
            cursor = conn.cursor()
            return conn, cursor
    except Error as e:
        raise ErrorConexion(f"Error al conectar a la base de datos: {e}")

def cerrar_conexion(conn, cursor):
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexión a la base de datos cerrada.")