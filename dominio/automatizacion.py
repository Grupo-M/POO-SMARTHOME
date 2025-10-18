from dominio.dispositivo import Dispositivo

class Automatizacion:

    def __init__(self, nombre: str):
        if not nombre.strip():
            raise ValueError("El nombre de la automatización no puede estar vacío.")
        self.__nombre = nombre

    @property
    def nombre(self) -> str:
        """Devuelve el nombre de la automatización."""
        return self.__nombre

    def activar_modo_ahorro(self, lista_dispositivos: list[Dispositivo]):
      
        for dispositivo in lista_dispositivos:
            dispositivo.apagar()  
        print(f"Modo ahorro activado para {len(lista_dispositivos)} dispositivos.")

