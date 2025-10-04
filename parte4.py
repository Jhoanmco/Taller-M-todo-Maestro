import sqlite3
import pandas as pd
import sys

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', None)

def cargar_datos_desde_sql(db_name="taller_db.sqlite", sql_file="personas_desordenadas.sql"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS personas;")
    
    with open(sql_file, 'r', encoding='utf-8') as f:
        sql_script = f.read()
        
    #hay algunos id duplicados
    sql_script_ignorar = sql_script.replace("INSERT INTO", "INSERT OR IGNORE INTO")

    cursor.executescript(sql_script_ignorar) 
    conn.commit()
    
    cursor.execute("SELECT id, nombre, fecha_nacimiento FROM personas")
    columnas = [desc[0] for desc in cursor.description]
    registros = [dict(zip(columnas, row)) for row in cursor.fetchall()]
    
    conn.close()
    return registros
    
#ALGORITMO DE BÚSQUEDA RECURSIVA EXHAUSTIVA [T(n) = 2T(n/2) + O(n)]
def busqueda_recursiva_exhaustiva(registros, condicion):
    """Implementa la recurrencia T(n) = 2T(n/2) + O(n)."""
    n = len(registros)
    if n <= 1:
        return [registros[0]] if n == 1 and condicion(registros[0]) else []

    mid = n // 2
    left_half = registros[:mid]
    right_half = registros[mid:]

    resultados_izquierda = busqueda_recursiva_exhaustiva(left_half, condicion)
    resultados_derecha = busqueda_recursiva_exhaustiva(right_half, condicion)

    return resultados_izquierda + resultados_derecha

def condicion_nacidos_post_1990(registro):
    return registro['fecha_nacimiento'] > '1990-01-01'

print("1. Cargando datos desde el archivo 'personas_desordenadas.sql'...")
try:
    DATOS_PERSONAS = cargar_datos_desde_sql(sql_file="personas_desordenadas.sql")
    print(f"   -> {len(DATOS_PERSONAS)} registros cargados correctamente.")
    
    print("\n2. Ejecutando Búsqueda Recursiva Exhaustiva [O(n log n)]...")
    resultados_finales = busqueda_recursiva_exhaustiva(DATOS_PERSONAS, condicion_nacidos_post_1990)
    
    print("\nResultados de la Búsqueda (TODOS los registros encontrados)")
    if resultados_finales:
        df = pd.DataFrame(resultados_finales)
        
        print(df[['id', 'nombre', 'fecha_nacimiento']].to_string(index=False, max_rows=len(df)))
        
        print(f"\nTotal de personas nacidas después de 1990: {len(resultados_finales)}")
    else:
        print("No se encontraron resultados que cumplan la condición.")

    print("Análisis de Complejidad (Método Maestro): T(n) = Θ(n log n)")

except Exception as e:

    print(f"\n[ERROR NO MANEJADO]: Ocurrió un error inesperado. Detalles: {e}")
