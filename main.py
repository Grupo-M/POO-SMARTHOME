from dao.usuario_dao import UsuarioDAO
from dao.dispositivo_dao import DispositivoDAO
from dao.ubicacion_dao import UbicacionDAO
from dao.rol_dao import RolDAO
from dominio.rol import Rol
from dominio.usuario import Usuario

# Instancias DAO
usuario_dao = UsuarioDAO()
dispositivo_dao = DispositivoDAO()
ubicacion_dao = UbicacionDAO()
rol_dao = RolDAO()

# --- Menús ---
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
    print("5. Gestión de roles")
    print("6. Cerrar sesión")
    return input("Seleccione una opción: ")

def menu_roles():
    while True:
        print("\n--- Gestión de Roles ---")
        print("1. Listar roles")
        print("2. Agregar nuevo rol")
        print("3. Modificar rol existente")
        print("4. Eliminar rol")
        print("5. Cambiar rol de un usuario")
        print("6. Volver al menú anterior")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            roles = rol_dao.listar_todos()
            if roles:
                for r in roles:
                    print(f"ID: {r.id_rol} - Nombre: {r.nombre} - Descripción: {r.descripcion}")
            else:
                print("No hay roles registrados.")

        elif opcion == "2":
            nombre = input("Nombre del rol: ")
            descripcion = input("Descripción: ")
            nuevo_rol = Rol(None, nombre, descripcion)
            if rol_dao.insertar(nuevo_rol):
                print("Rol agregado correctamente.")
            else:
                print("Error al agregar el rol.")

        elif opcion == "3":
            try:
                id_rol = int(input("ID del rol a modificar: "))
                if id_rol in (1, 2):
                    print("No se puede modificar este rol por seguridad.")
                    continue
                nombre = input("Nuevo nombre: ")
                descripcion = input("Nueva descripción: ")
                rol_actualizado = Rol(id_rol, nombre, descripcion)
                if rol_dao.actualizar(rol_actualizado):
                    print("Rol actualizado correctamente.")
                else:
                    print("Error al actualizar el rol.")
            except ValueError:
                print("ID inválido.")

        elif opcion == "4":
            try:
                id_rol = int(input("ID del rol a eliminar: "))
                if id_rol in (1, 2):
                    print("No se puede eliminar este rol por seguridad.")
                    continue
                if rol_dao.eliminar(id_rol):
                    print("Rol eliminado correctamente.")
                else:
                    print("Error al eliminar el rol.")
            except ValueError:
                print("ID inválido.")

        elif opcion == "5":
            usuarios = usuario_dao.listar_todos()
            print("Usuarios disponibles:")
            for u in usuarios:
                print(f"ID: {u.id_usuario} - {u.nombre} {u.apellido} - Rol: {u.rol.nombre}")
            try:
                id_usuario = int(input("Ingrese ID del usuario a modificar: "))
                usuario_seleccionado = usuario_dao.obtener_por_id(id_usuario)
                if not usuario_seleccionado:
                    print("Usuario no encontrado.")
                    continue

                roles = rol_dao.listar_todos()
                print("Roles disponibles:")
                for r in roles:
                    print(f"{r.id_rol} - {r.nombre}")

                id_rol_nuevo = int(input("Ingrese el ID del nuevo rol: "))
                if id_rol_nuevo not in [r.id_rol for r in roles]:
                    print("ID de rol no válido.")
                    continue

                rol_nuevo = rol_dao.obtener_por_id(id_rol_nuevo)
                if not rol_nuevo:
                    print("Rol no encontrado.")
                    continue

                usuario_seleccionado.rol = rol_nuevo
                usuario_dao.modificar(usuario_seleccionado)
                print(f"Rol de {usuario_seleccionado.nombre} actualizado a {rol_nuevo.nombre}.")

            except ValueError:
                print("ID inválido.")

        elif opcion == "6":
            break
        else:
            print("Opción inválida.")

# --- Main ---
def main():
    while True:
        opcion = menu_principal()

        if opcion == "1":  # Iniciar sesión
            email = input("Ingrese su email: ")
            password = input("Ingrese su Password: ")

            usuario = usuario_dao.obtener_por_email(email)
            if usuario and usuario.validar_credenciales(email, password):
                print(f"\nBienvenido, {usuario.nombre} ({usuario.rol.nombre})")

                if usuario.rol.id_rol == 1:  # Administrador
                    while True:
                        op = menu_admin()
                        if op == "5":
                            menu_roles()
                        elif op == "6":
                            print("Cerrando sesión de administrador...")
                            break
                        else:
                            print("Funcionalidad de dispositivos omitida para este ejemplo.")
                else:  # Usuario estándar
                    while True:
                        op = menu_usuario()
                        if op == "3":
                            print("Cerrando sesión de usuario...")
                            break
                        else:
                            print("Funcionalidad omitida para este ejemplo.")
            else:
                print("Credenciales incorrectas. Intente nuevamente.")

        elif opcion == "2":  # Registrar nuevo usuario
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            email = input("Email: ")
            password = input("Password: ")

            rol_usuario = rol_dao.obtener_por_id(2)  # ID 2 → Usuario estándar
            nuevo_usuario = Usuario(nombre, apellido, email, password, rol_usuario)
            if usuario_dao.guardar(nuevo_usuario):
                print("Usuario registrado correctamente.")
            else:
                print("Error al registrar el usuario.")

        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()



