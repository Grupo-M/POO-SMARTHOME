from dao.dispositivo_dao import DispositivoDAO
from dao.ubicacion_dao import UbicacionDAO

class GestorDispositivos:
    def __init__(self):
        self.dispositivo_dao = DispositivoDAO()
        self.ubicacion_dao = UbicacionDAO()

    def agregar_dispositivo(self, nombre: str, estado: str, esencial: bool, id_ubicacion: int) -> bool:
        return self.dispositivo_dao.insertar_objeto(nombre, estado, int(esencial), id_ubicacion)

    def listar_dispositivos(self) -> list:
        return self.dispositivo_dao.obtener_todos()

    def cambiar_estado(self, id_dispositivo: int, nuevo_estado: str) -> bool:
        return self.dispositivo_dao.actualizar_estado(id_dispositivo, nuevo_estado)

    def eliminar_dispositivo(self, id_dispositivo: int) -> bool:
        return self.dispositivo_dao.eliminar(id_dispositivo)

    def aplicar_modo_ahorro(self, dispositivos: list) -> None:
        apagados = 0
        for d in dispositivos:
            if not d[3]:  # campo 'esencial'
                if self.dispositivo_dao.actualizar_estado(d[0], "apagado"):
                    apagados += 1
        print(f"Modo ahorro aplicado. {apagados} dispositivos apagados.")

