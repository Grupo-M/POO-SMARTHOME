from conn.db_setup import crear_base_si_no_existe, ejecutar_script_sql, verificar_tablas

# Crear base
crear_base_si_no_existe("smarthome_db")

# Ejecutar scripts
ejecutar_script_sql("BD-Evidencia-6/estructura.sql")
ejecutar_script_sql("BD-Evidencia-6/datos_iniciales.sql")

# Verificación
tablas = [
    "rol",
    "usuario",
    "casa",
    "ubicacion",
    "dispositivo",
    "automatizacion",
    "automatizacion_dispositivo"
]

verificar_tablas(tablas)

