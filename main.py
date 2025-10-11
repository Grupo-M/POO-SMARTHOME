from dao.usuario_dao import UsuarioDAO
from dao.dispositivo_dao import DispositivoDAO


def menu_principal():
    print("\n--- SmartHome Solutions ---")
    print("1. Iniciar sesión")
    print("2. Registrar nuevo usuario")
    print("3. Salir")
    return input("Seleccione una opción: ")


def menu_usuario():
    print("\n--- Menú Usuario Estándar ---")
    print("1. Ver mis datos personales")
    print("2. Ver mis dispositivos")
    print("3. Cerrar sesión")
    return input("Seleccione una opción: ")


def menu_admin():
    print("\n--- Menú Administrador ---")
    print("1. Listar dispositivos")
    print("2. Agregar dispositivo")
    print("3. Modificar estado de dispositivo")
    print("4. Eliminar dispositivo")
    print("5. Cerrar sesión")
    return input("Seleccione una opción: ")