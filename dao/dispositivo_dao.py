from typing import List, Optional, Tuple
from conn.db_conn import insert_query, execute_query, update_query, delete_query


class DispositivoDAO:
    def insertar_objeto(self, nombre: str, tipo: str, estado: str, usuario_id: int) -> bool:
        query = """
            INSERT INTO dispositivos (nombre, tipo, estado, usuario_id)
            VALUES (%s, %s, %s, %s)
        """
        valores = (nombre, tipo, estado, usuario_id)
        return insert_query(query, valores)

    def obtener_todos(self) -> Optional[List[Tuple]]:
        query = "SELECT id, nombre, tipo, estado, usuario_id FROM dispositivos"
        return execute_query(query)

    def obtener_por_usuario(self, usuario_id: int) -> Optional[List[Tuple]]:
        query = "SELECT id, nombre, tipo, estado, usuario_id FROM dispositivos WHERE usuario_id = %s"
        return execute_query(query, (usuario_id,))
    
    def actualizar_estado(self, id_dispositivo: int, nuevo_estado: str) -> bool:
        query = "UPDATE dispositivos SET estado = %s WHERE id = %s"
        valores = (nuevo_estado, id_dispositivo)
        return update_query(query, valores)

    def modificar(self, id_dispositivo: int, nombre: str, tipo: str, estado: str) -> bool:
        query = """
            UPDATE dispositivos
            SET nombre = %s, tipo = %s, estado = %s
            WHERE id = %s
        """
        valores = (nombre, tipo, estado, id_dispositivo)
        return update_query(query, valores)

    def eliminar(self, id_dispositivo: int) -> bool:
        query = "DELETE FROM dispositivos WHERE id = %s"
        valores = (id_dispositivo,)
        return delete_query(query, valores)