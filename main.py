from dao.usuario_dao import UsuarioDAO
from dao.rol_dao import RolDAO
from dao.ubicacion_dao import UbicacionDAO
from dominio.rol import Rol
from dominio.usuario import Usuario
from dominio.gestor_dispositivos import GestorDispositivos

# --- Instancias DAO y Gestor ---
usuario_dao = UsuarioDAO()
rol_dao = RolDAO()
ubicacion_dao = UbicacionDAO()
gestor_dispositivos = GestorDispositivos()

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
    print("2. Ver dispositivos disponibles")
    print("3. Cerrar sesión")
    return input("Seleccione una opción: ")

def menu_administrador():
    print("\n--- Menú Administrador ---")
    print("1. Listar dispositivos")
    print("2. Agregar dispositivo")
    print("3. Modificar estado de dispositivo")
    print("4. Eliminar dispositivo")
    print("5. Gestión de roles")
    print("6. Eliminar usuario")
    print("7. Cerrar sesión")
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
                        op = menu_administrador()
                        if op == "1":
                            dispositivos = gestor_dispositivos.listar_dispositivos()
                            if dispositivos:
                                for d in dispositivos:
                                    print(f"[{d[0]}] {d[1]} - Estado: {d[2]} - Esencial: {'Sí' if d[3] else 'No'} - Ubicación ID: {d[4]}")
                            else:
                                print("No hay dispositivos registrados.")

                        elif op == "2":
                            nombre = input("Nombre del dispositivo: ")
                            estado = input("Estado inicial (encendido/apagado): ").lower()
                            esencial = input("¿Es esencial? (s/n): ").lower() == "s"
                            ubicaciones = ubicacion_dao.obtener_todas()
                            print("Ubicaciones disponibles:")
                            for u in ubicaciones:
                                print(f"{u.id_ubicacion} - {u.nombre}")
                            try:
                                id_ubicacion = int(input("ID de ubicación: "))
                                if gestor_dispositivos.agregar_dispositivo(nombre, estado, esencial, id_ubicacion):
                                    print("Dispositivo agregado correctamente.")
                                else:
                                    print("Error al agregar el dispositivo.")
                            except ValueError:
                                print("ID inválido.")

                        elif op == "3":
                            dispositivos = gestor_dispositivos.listar_dispositivos()
                            if dispositivos:
                                print("\nDispositivos disponibles:")
                                for d in dispositivos:
                                    print(f"[{d[0]}] {d[1]} - Estado: {d[2]} - Esencial: {'Sí' if d[3] else 'No'} - Ubicación ID: {d[4]}")
                                try:
                                    id_disp = int(input("\nID del dispositivo a modificar: "))
                                    nuevo_estado = input("Nuevo estado (encendido/apagado): ").lower()
                                    if gestor_dispositivos.cambiar_estado(id_disp, nuevo_estado):
                                        print("Estado actualizado.")
                                    else:
                                        print("Error al actualizar el estado.")
                                except ValueError:
                                    print("ID inválido.")
                            else:
                                print("No hay dispositivos registrados.")

                        elif op == "4":
                            dispositivos = gestor_dispositivos.listar_dispositivos()
                            if dispositivos:
                                print("\nDispositivos disponibles:")
                                for d in dispositivos:
                                    print(f"[{d[0]}] {d[1]} - Estado: {d[2]} - Esencial: {'Sí' if d[3] else 'No'} - Ubicación ID: {d[4]}")
                                try:
                                    id_disp = int(input("\nID del dispositivo a eliminar: "))
                                    if gestor_dispositivos.eliminar_dispositivo(id_disp):
                                        print("Dispositivo eliminado.")
                                    else:
                                        print("Error al eliminar el dispositivo.")
                                except ValueError:
                                    print("ID inválido.")
                            else:
                                print("No hay dispositivos registrados.")

                        elif op == "5":
                            menu_roles()

                        elif op == "6":  # Eliminar usuario
                            usuarios = usuario_dao.listar_todos()
                            usuarios_estandar = [u for u in usuarios if u.rol.id_rol != 1]

                            if not usuarios_estandar:
                                print("No hay usuarios estándar para eliminar.")
                                continue

                            print("\nUsuarios disponibles para eliminar:")
                            for u in usuarios_estandar:
                                print(f"ID: {u.id_usuario} - {u.nombre} {u.apellido} - Email: {u.email} - Rol: {u.rol.nombre}")

                            email_usuario = input("Ingrese el email del usuario a eliminar: ")
                            usuario_seleccionado = usuario_dao.obtener_por_email(email_usuario)

                            if usuario_seleccionado and usuario_seleccionado.rol.id_rol != 1:
                                confirmacion = input(f"¿Está seguro que quiere eliminar a {usuario_seleccionado.nombre}? (si/no): ").lower()
                                if confirmacion == "si":
                                    usuario_dao.eliminar_por_email(email_usuario)
                                    print(f"{usuario_seleccionado.nombre} eliminado correctamente.")
                                else:
                                    print("Eliminación cancelada.")
                            else:
                                print("No se puede eliminar a un administrador o el usuario no existe.")

                        elif op == "7":
                            print("Cerrando sesión de administrador...")
                            break
                        else:
                            print("Opción inválida.")

                else:  # Usuario estándar
                    while True:
                        op = menu_usuario()
                        if op == "1":
                            print(f"Nombre: {usuario.nombre} {usuario.apellido}")
                            print(f"Email: {usuario.email}")
                            print(f"Rol: {usuario.rol.nombre}")
                        elif op == "2":
                            dispositivos = gestor_dispositivos.listar_dispositivos()
                            if dispositivos:
                                for d in dispositivos:
                                    print(f"[{d[0]}] {d[1]} - Estado: {d[2]} - Esencial: {'Sí' if d[3] else 'No'} - Ubicación ID: {d[4]}")
                            else:
                                print("No hay dispositivos registrados.")
                        elif op == "3":
                            print("Cerrando sesión de usuario...")
                            break
                        else:
                            print("Opción inválida.")

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
