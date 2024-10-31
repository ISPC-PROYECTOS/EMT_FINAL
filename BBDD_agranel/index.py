from .actualizar_stock import actualizar_stock
from .alta import alta
from .baja import baja
from .consultar_stock import consultar_stock
from .modificar import modificar
from .registro_venta import registro_venta_actualizacion_stock


def menu_stock_granel():
    salir = False
    while not salir:
        print('-' * 25)
        print("---> MENÚ DE OPCIONES <---")
        print('-' * 25)
        print("")
        print("1 - REGISTRO VENTA")
        print("2 - CONSULTAR STOCK")
        print("3 - ACTUALIZAR STOCK")
        print("4 - ALTA")
        print("5 - BAJA")
        print("6 - MODIFICAR")
        print("7 - SALIR") 

        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            registro_venta_actualizacion_stock()
        elif opcion == 2:
            consultar_stock()
        elif opcion == 3:
            actualizar_stock()
        elif opcion == 4:
            alta()
        elif opcion == 5:
            baja()
        elif opcion == 6:
            modificar()
        elif opcion == 7:
            print("Gracias por utilizar nuestro programa.")
            salir = True
        else: 
            print("La opción es incorrecta.")
