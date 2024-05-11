#Imports
from datos import *
from menu import *
from usuarios import *

#Constants
BASE_DE_DATOS_USUARIOS = "usuarios.json"

usuarios = cargar_datos(BASE_DE_DATOS_USUARIOS)

while True:
    menu_principal()
    menu = pedir_opcion()
    if menu == 1:
        menu_gestion_usuarios()
        opc = pedir_opcion()
        if opc == 1:
            crear_ususario(usuarios)
        guardar_datos(usuarios,BASE_DE_DATOS_USUARIOS)
    elif menu == 2:
        menu_gestion_servicios()
        opc = pedir_opcion()
    elif menu == 3:
        menu_ventas()
        opc = pedir_opcion()
    elif menu == 4:
        menu_reportes()
        opc = pedir_opcion()
    elif menu == 0:
        print("SALIR")
        print("****************************************************************")
        break
    else:
        print("No existe esta opción")