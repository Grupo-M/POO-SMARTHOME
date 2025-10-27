from typing import List
from dao.dispositivo_dao import DispositivoDAO
from dao.ubicacion_dao import UbicacionDAO
from dominio.dispositivo import Dispositivo

class GestorDispositivos:
    def __init__(self):
        self.dispositivo_dao = DispositivoDAO()
        self.ubicacion_dao = UbicacionDAO()

    def agregar_dispositivo(self, dispositivo: Dispositivo) -> bool:
        return self.dispositivo_dao.insertar_objeto(
            nombre=dispositivo.nombre,
            estado=dispositivo.estado,
            esencial=int(dispositivo.esencial),
            id_ubicacion=dispositivo.ubicacion.id_ubicacion
        )

    def listar_dispositivos(self) -> List[Dispositivo]:
        return self.dispositivo_dao.obtener_todos_objetos()

    def cambiar_estado(self, dispositivo: Dispositivo, nuevo_estado: str) -> bool:
        dispositivo.estado = nuevo_estado  # actualiza en memoria
        return self.dispositivo_dao.actualizar_estado(dispositivo.id_dispositivo, nuevo_estado)

    def eliminar_dispositivo(self, dispositivo: Dispositivo) -> bool:
        return self.dispositivo_dao.eliminar(dispositivo.id_dispositivo)

    def aplicar_modo_ahorro(self, dispositivos: List[Dispositivo]) -> int:
        apagados = 0
        for d in dispositivos:
            if not d.esencial:
                if self.dispositivo_dao.actualizar_estado(d.id_dispositivo, "apagado"):
                    d.estado = "apagado"
                    apagados += 1
        return apagados

