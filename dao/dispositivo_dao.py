from typing import List
from dominio.dispositivo import Dispositivo
from dominio.ubicacion import Ubicacion
from interfaces.idispositivo_dao import IDispositivoDAO
from conn.db_crud import insert_query, execute_query, update_query, delete_query

class DispositivoDAO(IDispositivoDAO):
    
    def obtener_todos_objetos(self) -> List[Dispositivo]:
        query = """
            SELECT d.id_dispositivo, d.nombre, d.estado, d.esencial,
                   u.id_ubicacion, u.nombre, u.id_casa
            FROM dispositivo d
            JOIN ubicacion u ON d.id_ubicacion = u.id_ubicacion
        """
        resultados = execute_query(query)
        dispositivos = []

        if resultados:
            for fila in resultados:
                id_disp, nombre_disp, estado, esencial, id_ubicacion, nombre_ubicacion, casa_ubicacion = fila
                ubicacion = Ubicacion(id_ubicacion, nombre_ubicacion, casa_ubicacion)
                disp = Dispositivo(id_disp, nombre_disp, estado, bool(esencial), ubicacion)
                dispositivos.append(disp)

        return dispositivos

    def insertar_objeto(self, nombre: str, estado: str, esencial: int, id_ubicacion: int) -> bool:
        query = """
            INSERT INTO dispositivo (nombre, estado, esencial, id_ubicacion)
            VALUES (%s, %s, %s, %s)
        """
        valores = (nombre, estado, esencial, id_ubicacion)
        return insert_query(query, valores)

    def actualizar_estado(self, id_dispositivo: int, nuevo_estado: str) -> bool:
        query = "UPDATE dispositivo SET estado = %s WHERE id_dispositivo = %s"
        valores = (nuevo_estado, id_dispositivo)
        return update_query(query, valores)

    def modificar(self, id_dispositivo: int, nombre: str, estado: str, esencial: int, id_ubicacion: int) -> bool:
        query = """
            UPDATE dispositivo
            SET nombre = %s, estado = %s, esencial = %s, id_ubicacion = %s
            WHERE id_dispositivo = %s
        """
        valores = (nombre, estado, esencial, id_ubicacion, id_dispositivo)
        return update_query(query, valores)

    def eliminar(self, id_dispositivo: int) -> bool:
        query = "DELETE FROM dispositivo WHERE id_dispositivo = %s"
        valores = (id_dispositivo,)
        return delete_query(query, valores)

