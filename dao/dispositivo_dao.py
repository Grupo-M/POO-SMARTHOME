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
    
    