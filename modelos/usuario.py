
class Usuario:
    def __init__(self,nombre,apellido,email,password,rol="usuario"):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
        self.rol = rol # por ahora string, luego se puede cambiar a objeto Rol

    def validar_credenciales(self,email,password):
        return self.email == email and self.password == password

    def modificar_rol(self,nuevo_rol):
        self.rol = nuevo_rol
        
