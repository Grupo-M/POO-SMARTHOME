from dao.usuario_dao import UsuarioDAO
from dao.dispositivo_dao import DispositivoDAO
from dao import rol_dao  
from dominio.rol import Rol
from dominio.usuario import Usuario

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

def menu_roles():
    while True:
        print("\n--- Gestión de Roles ---")
        print("1. Listar roles")
        print("2. Agregar nuevo rol")
        print("3. Modificar rol existente")
        print("4. Eliminar rol")
        print("5. Volver al menú anterior")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            roles = rol_dao.listar_roles()
            if roles:
                for r in roles:
                    print(f"ID: {r.id_rol} - Nombre: {r.nombre} - Descripción: {r.descripcion}")
            else:
                print("No hay roles registrados.")

        elif opcion == "2":
            id_rol = int(input("ID del nuevo rol: "))
            nombre = input("Nombre del rol: ")
            descripcion = input("Descripción: ")
            nuevo_rol = Rol(id_rol, nombre, descripcion)
            rol_dao.insertar_rol(nuevo_rol)
            print("Rol agregado correctamente.")

        elif opcion == "3":
            id_rol = int(input("ID del rol a modificar: "))
            nombre = input("Nuevo nombre: ")
            descripcion = input("Nueva descripción: ")
            rol_actualizado = Rol(id_rol, nombre, descripcion)
            rol_dao.actualizar_rol(rol_actualizado)
            print("Rol actualizado correctamente.")

        elif opcion == "4":
            id_rol = int(input("ID del rol a eliminar: "))
            rol_dao.eliminar_rol(id_rol)
            print("Rol eliminado correctamente.")

        elif opcion == "5":
            break
        else:
            print("Opción inválida.")


def main():
    usuario_dao = UsuarioDAO()
    dispositivo_dao = DispositivoDAO()

    while True:
        opcion = menu_principal()

        if opcion == "1":
            email = input("Ingrese su email: ")
            usuario = usuario_dao.obtener_por_email(email)

            if usuario:
                print(f"\nBienvenido, {usuario.nombre} ({'Admin' if usuario.rol.id_rol == 1 else 'Usuario'})")

                if usuario.rol.id_rol == 1:
                    while True:
                        op = menu_admin()

                        if op == "1":
                            dispositivos = dispositivo_dao.obtener_todos()
                            if dispositivos:
                                for d in dispositivos:
                                    print(d)
                            else:
                                print("No hay dispositivos registrados.")

                        elif op == "2":
                            nombre = input("Nombre del dispositivo: ")
                            tipo = input("Tipo (luz, cámara, etc.): ")
                            estado = input("Estado inicial (encendido/apagado): ")
                            dispositivo_dao.insertar_objeto(nombre, tipo, estado, usuario.id_usuario)
                            print("Dispositivo agregado correctamente.")

                        elif op == "3":
                            id_disp = int(input("ID del dispositivo: "))
                            nuevo_estado = input("Nuevo estado (encendido/apagado): ")
                            dispositivo_dao.actualizar_estado(id_disp, nuevo_estado)
                            print("Estado actualizado correctamente.")

                        elif op == "4":
                            id_disp = int(input("ID del dispositivo a eliminar: "))
                            dispositivo_dao.eliminar(id_disp)
                            print("Dispositivo eliminado correctamente.")

                        elif op == "5":
                            menu_roles()

                        elif op == "6":
                            print("Cerrando sesión de administrador...")
                            break
                        else:
                            print("Opción inválida.")

                else:
                    while True:
                        op = menu_usuario()
                        if op == "1":
                            print("\nDatos personales:")
                            print(f"Nombre: {usuario.nombre} {usuario.apellido}")
                            print(f"Email: {usuario.email}")
                            print(f"Rol: {usuario.rol.nombre}")
                        elif op == "2":
                            dispositivos = dispositivo_dao.obtener_por_usuario(usuario.id_usuario)
                            if dispositivos:
                                for d in dispositivos:
                                    print(d)
                            else:
                                print("No tenés dispositivos asignados.")
                        elif op == "3":
                            print("Cerrando sesión de usuario...")
                            break
                        else:
                            print("Opción inválida.")
            else:
                print("Usuario no encontrado.")

        elif opcion == "2":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            email = input("Email: ")
            password = input("Contraseña: ")

            rol_usuario = Rol(2, "usuario", "Permisos básicos")
            nuevo_usuario = Usuario(nombre, apellido, email, password, rol_usuario)
            usuario_dao.guardar(nuevo_usuario)
            print("Usuario registrado correctamente.")

        elif opcion == "3":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()

    