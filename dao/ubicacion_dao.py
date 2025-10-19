from typing import List, Optional, Tuple
from conn.db_conn import execute_query

class Ubicacion:
    def __init__(self, id_ubicacion: int, nombre: str):
        self.id_ubicacion = id_ubicacion
        self.nombre = nombre

class UbicacionDAO:
    def obtener_todas(self) -> List[Ubicacion]:
        query = "SELECT id_ubicacion, nombre FROM ubicacion"
        resultados = execute_query(query)
        ubicaciones = []
        if resultados:
            for fila in resultados:
                id_ubicacion, nombre = fila
                ubicaciones.append(Ubicacion(id_ubicacion, nombre))
        return ubicaciones

