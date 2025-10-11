from modelos import ubicacion
class Dispositivo:
    def __init__(self, id_dispositivo: int, nombre: str, esencial: bool, ubicacion: ubicacion):
        self.id_dispositivo = id_dispositivo
        self.nombre = nombre
        self.estado = "apagado"  # por defecto
        self.esencial = esencial
        self.ubicacion = ubicacion

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

        