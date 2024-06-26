#Imports
from datos import *
from menu import *
from usuarios import *
from servicios import *
from ventas import *
from reportes import *

#Constants
BASE_DE_DATOS_USUARIOS = "usuarios.json"
BASE_DE_DATOS_CATALOGO = "catalogo.json"
BASE_DE_DATOS_VENTAS = "ventas.json"

usuarios = cargar_datos(BASE_DE_DATOS_USUARIOS)
catalogo = cargar_datos(BASE_DE_DATOS_CATALOGO)
ventas = cargar_datos(BASE_DE_DATOS_VENTAS)

while True:
    menu_principal()
    menu = pedir_opcion()
    if menu == 1:
        while True:
            menu_gestion_usuarios()
            opc = pedir_opcion()
            if opc == 1:
                crear_ususario(usuarios)
            elif opc == 2:
                mostrar_usuario(usuarios)
            elif opc == 3:
                actualizar_usuario(usuarios)
            elif opc == 4:
                eliminar_usuario(usuarios)
            elif opc == 5:
                registrar_pqrs(usuarios)
            elif opc == 0:
                break
            else:
                print("¡Opción no válida!")
            guardar_datos(usuarios,BASE_DE_DATOS_USUARIOS)
    elif menu == 2:
        while True:
            menu_gestion_servicios()
            opc = pedir_opcion()
            if opc == 1:
                while True:
                    tipo = seleccionar_tipo()
                    if tipo == 0:
                        break
                    elif tipo != -1:
                        while True:
                            categoria = seleccionar_categoria(tipo)
                            if categoria == 0:
                                break
                            elif categoria != -1:
                                print("----------------------------------------------------------------")
                                print("Ingrese toda la información:")
                                print("")
                                crear_producto_servicio(catalogo, tipo, categoria)
                                guardar_datos(catalogo,BASE_DE_DATOS_CATALOGO)
            elif opc == 2:
                while True:
                    tipo = seleccionar_tipo()
                    if tipo == 0:
                        break
                    elif tipo != -1:
                        while True:
                            categoria = seleccionar_categoria(tipo)
                            if categoria == 0:
                                break
                            elif categoria != -1:
                                mostrar_producto_servicio(catalogo,tipo,categoria)
            elif opc == 3:
                while True:
                    tipo = seleccionar_tipo()
                    if tipo == 0:
                        break
                    elif tipo != -1:
                        while True:
                            categoria = seleccionar_categoria(tipo)
                            if categoria == 0:
                                break
                            elif categoria != -1:
                                actualizar_producto_servicio(catalogo,tipo,categoria)
                                guardar_datos(catalogo,BASE_DE_DATOS_CATALOGO)
            elif opc == 4:
                while True:
                    tipo = seleccionar_tipo()
                    if tipo == 0:
                        break
                    elif tipo != -1:
                        while True:
                            categoria = seleccionar_categoria(tipo)
                            if categoria == 0:
                                break
                            elif categoria != -1:
                                eliminar_producto_servicio(catalogo,tipo,categoria)
                                guardar_datos(catalogo,BASE_DE_DATOS_CATALOGO)

            elif opc == 0:
                break
            else:
                print("¡Opción no válida!")
    elif menu == 3:
        while True:
            validar_categoria(usuarios)
            guardar_datos(usuarios,BASE_DE_DATOS_USUARIOS)
            menu_ventas()
            opc = pedir_opcion()
            if opc == 1:
                mostrar_catalogo(catalogo)
                print("Seleccione un producto / servicio")
                print("para mostrar la información completa")
                while True:
                    tipo = seleccionar_tipo()
                    if tipo == 0:
                        break
                    elif tipo != -1:
                        while True:
                            categoria = seleccionar_categoria(tipo)
                            if categoria == 0:
                                break
                            elif categoria != -1:
                                mostrar_producto_servicio(catalogo,tipo,categoria)
            elif opc == 2:
                while True:
                    tipo = seleccionar_tipo()
                    if tipo == 0:
                        break
                    elif tipo != -1:
                        while True:
                            categoria = seleccionar_categoria(tipo)
                            if categoria == 0:
                                break
                            elif categoria != -1:
                                registrar_venta(catalogo,tipo,categoria,ventas,usuarios)
                                guardar_datos(ventas,BASE_DE_DATOS_VENTAS)
                                guardar_datos(usuarios,BASE_DE_DATOS_USUARIOS)     
                                guardar_datos(catalogo,BASE_DE_DATOS_CATALOGO)
            elif opc == 3:
                mostrar_ventas(ventas)
            elif opc == 0:
                break
            else:
                print("¡Opción no válida!")
    elif menu == 4:
        while True:
            menu_reportes()
            opc = pedir_opcion()
            if opc == 1:
                cantidad_productos_servicios(catalogo)
            elif opc == 2:
                mas_populares(catalogo)
            elif opc == 3:
                usuarios_por_producto_servicio(catalogo)
            elif opc == 0:
                break
            else:
                print("¡Opción no válida!")
    elif menu == 0:
        print("SALIR")
        print("****************************************************************")
        break
    else:
        print("No existe esta opción")