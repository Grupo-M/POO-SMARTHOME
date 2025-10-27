from typing import List
from dominio.ubicacion import Ubicacion
from conn.db_crud import execute_query
from interfaces.iubicacion_dao import IUbicacionDAO
from dominio.casa import Casa

class UbicacionDAO:
    def obtener_todas(self) -> List[Ubicacion]:
        query = """
            SELECT u.id_ubicacion, u.nombre, c.id_casa, c.nombre
            FROM ubicacion u
            JOIN casa c ON u.id_casa = c.id_casa
        """
        resultados = execute_query(query)
        ubicaciones = []
        if resultados:
            for fila in resultados:
                id_ubicacion, nombre, id_casa, nombre_casa = fila
                casa = Casa(id_casa, nombre_casa)
                ubicaciones.append(Ubicacion(id_ubicacion, nombre, casa))
        return ubicaciones
    
    from conn.db_crud import execute_query
from dominio.ubicacion import Ubicacion

class UbicacionDAO:
    def obtener_todas(self) -> list[Ubicacion]:
        query = "SELECT id_ubicacion, nombre, id_casa FROM ubicacion"
        resultados = execute_query(query)
        ubicaciones = []
        if resultados:
            for fila in resultados:
                id_ubicacion, nombre, id_casa = fila
                ubicaciones.append(Ubicacion(id_ubicacion, nombre, id_casa))
        return ubicaciones

    def obtener_por_id(self, id_ubicacion: int) -> Ubicacion | None:
        query = "SELECT id_ubicacion, nombre, id_casa FROM ubicacion WHERE id_ubicacion = %s"
        resultados = execute_query(query, (id_ubicacion,))
        if resultados:
            id_u, nombre, id_casa = resultados[0]
            return Ubicacion(id_u, nombre, id_casa)
        return None


