class Automatizacion:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def activar_modo_ahorro(self, lista_dispositivos):
        for dispositivo in lista_dispositivos:
            dispositivo["estado"] = "apagado"
        return lista_dispositivos

