from typing import List, Optional, Tuple
from conn.db_conn import insert_query, execute_query, update_query, delete_query

class DispositivoDAO:
    def insertar_objeto(self, nombre, estado, esencial, id_ubicacion):
        query = """
            INSERT INTO dispositivo (nombre, estado, esencial, id_ubicacion)
            VALUES (%s, %s, %s, %s)
        """
        valores = (nombre, estado, esencial, id_ubicacion)
        return insert_query(query, valores)

    def obtener_todos(self) -> Optional[List[Tuple]]:
        query = "SELECT id_dispositivo, nombre, estado, esencial, id_ubicacion FROM dispositivo"
        return execute_query(query)

    def obtener_por_usuario(self, id_usuario: int) -> Optional[List[Tuple]]:
        # Si querés filtrar por usuario, tu tabla debe tener una columna id_usuario
        query = "SELECT id_dispositivo, nombre, estado, esencial, id_ubicacion FROM dispositivo WHERE id_usuario = %s"
        return execute_query(query, (id_usuario,))

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

