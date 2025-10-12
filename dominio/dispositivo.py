from dominio.ubicacion import Ubicacion  

class Dispositivo:
    def __init__(self, id_dispositivo: int, nombre: str, estado: str, esencial: bool, ubicacion: Ubicacion):
        self.id_dispositivo = id_dispositivo
        self.nombre = nombre
        self.estado = estado
        self.esencial = esencial
        self.__ubicacion = ubicacion

    def encender(self):
        self.estado = "encendido"
        print(f"{self.nombre} está encendido.")

    def apagar(self):
        self.estado = "apagado"
        print(f"{self.nombre} está apagado.")

    def cambiar_estado(self):
        if self.estado == "apagado":
            self.encender()
        else:
            self.apagar()

    def __str__(self):
        return f"[{self.id_dispositivo}] {self.nombre} - Estado: {self.estado} - Esencial: {'Sí' if self.esencial else 'No'} - Ubicación: {self.ubicacion.nombre}"

