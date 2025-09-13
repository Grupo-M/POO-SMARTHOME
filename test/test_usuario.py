# test/test_usuario.py

# pylint: disable=import-error, missing-function-docstring
# pylint: disable=invalid-name

from modelos.usuario import Usuario  # pylint: disable=import-error

def test_crear_usuario():
    # Crear un usuario de prueba
    usuario = Usuario("Carolina", "Lanfranco", "caro123@gmail.com", "Oreo4")
    
    # Verificar que el atributo nombre exista
    assert hasattr(usuario, "nombre")

def test_validar_credenciales():
    usuario = Usuario("Caro", "Lanfranco", "caro123@gmail.com", "Oreo4")
    
    # Comprobar que validar_credenciales funcione correctamente
    assert usuario.validar_credenciales("caro123@gmail.com", "Oreo4") is True

def test_modificar_rol():
    usuario = Usuario("Caro", "Lanfranco", "caro123@gmail.com", "Oreo4")
    
    # Inicializamos el rol para que Pylint no marque warning
    if not hasattr(usuario, "rol"):
        usuario.rol = "usuario"

    usuario.modificar_rol("administrador")
    
    # Comprobar que el rol se haya modificado
    assert usuario.rol == "administrador"
