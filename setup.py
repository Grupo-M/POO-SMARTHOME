from conn.db_conn import crear_base_si_no_existe, ejecutar_script_sql, execute_query

# Crear la base de datos si no existe
crear_base_si_no_existe("smarthome_db")

# Ejecutar los scripts SQL desde la carpeta BD-Evidencia-6
ejecutar_script_sql("BD-Evidencia-6/estructura.sql")
ejecutar_script_sql("BD-Evidencia-6/datos_iniciales.sql")

# Verificación final: mostrar cantidad de registros por tabla
tablas = [
    "rol",
    "usuario",
    "casa",
    "ubicacion",
    "dispositivo",
    "automatizacion",
    "automatizacion_dispositivo"
]

print("\n📋 Verificación de carga:")
for tabla in tablas:
    resultado = execute_query(f"SELECT COUNT(*) FROM {tabla}")
    if resultado:
        print(f" - {tabla}: {resultado[0][0]} registros")
    else:
        print(f" - {tabla}: error al consultar")

