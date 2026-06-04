import pandas as pd
import json
import time

# ================================================================
#  DATOS.PY
#  Responsabilidad: abrir y leer los archivos CSV y JSON
#  Otros archivos importan las funciones de aquí para usarlas
# ================================================================


def leer_csv(archivo):
    """
    Lee el CSV en bloques de 100,000 filas para no agotar la RAM.
    Devuelve un diccionario con todo lo calculado.
    """
    BLOQUE = 100_000
    total_edad = total_temp = total_filas = 0
    max_edad   = max_temp = 0
    min_edad   = 999
    frec_especialidad = pd.Series(dtype='int64')
    frec_medicamento  = pd.Series(dtype='int64')
    muestra_edades    = []
    muestra_temps     = []

    print(f"  Leyendo '{archivo}' en bloques de {BLOQUE:,}...")
    inicio = time.time()

    for bloque in pd.read_csv(archivo, chunksize=BLOQUE):
        total_filas += len(bloque)
        total_edad  += bloque['edad'].sum()
        total_temp  += bloque['temperatura'].sum()
        max_edad     = max(max_edad, bloque['edad'].max())
        min_edad     = min(min_edad, bloque['edad'].min())
        max_temp     = max(max_temp, bloque['temperatura'].max())

        # Contar cuántas veces aparece cada especialidad y medicamento
        frec_especialidad = frec_especialidad.add(bloque['especialidad'].value_counts(), fill_value=0)
        frec_medicamento  = frec_medicamento.add(bloque['medicamento'].value_counts(),  fill_value=0)

        # Guardamos el 1% de cada bloque como muestra para las gráficas
        muestra_edades.extend(bloque['edad'].sample(frac=0.01, random_state=42).tolist())
        muestra_temps.extend(bloque['temperatura'].sample(frac=0.01, random_state=42).tolist())

    tiempo_csv = time.time() - inicio

    # Temperatura promedio agrupada por rango de 5 años (para gráfica de líneas)
    df = pd.DataFrame({"edad": muestra_edades, "temperatura": muestra_temps})
    df['rango']    = (df['edad'] // 5) * 5
    temp_por_edad  = df.groupby('rango')['temperatura'].mean().reset_index()

    # Devolvemos todo lo calculado en un solo diccionario
    return {
        "tiempo":              tiempo_csv,
        "estadisticas": {
            "total":     total_filas,
            "edad_prom": total_edad / total_filas,
            "temp_prom": total_temp / total_filas,
            "edad_max":  max_edad,
            "edad_min":  min_edad,
            "temp_max":  max_temp
        },
        "top_medicamentos":       frec_medicamento.sort_values(ascending=False).head(5),
        "consultas_especialidad": frec_especialidad.sort_values(ascending=False),
        "muestra_edades":         muestra_edades,
        "temp_por_edad":          temp_por_edad
    }


def leer_json(archivo):
    """
    Lee el JSON línea por línea para no agotar la RAM.
    Devuelve un diccionario con los resultados básicos.
    """
    total_edad = total_temp = total_filas = 0

    print(f"  Leyendo '{archivo}' línea por línea...")
    inicio = time.time()

    with open(archivo, 'r', encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip().rstrip(',')

            # Solo procesamos líneas que sean un objeto completo { ... }
            if not (linea.startswith('{') and linea.endswith('}')):
                continue

            try:
                paciente     = json.loads(linea)
                total_filas += 1
                total_edad  += paciente['edad']
                total_temp  += paciente['consulta']['temperatura']
            except (json.JSONDecodeError, KeyError):
                continue

    tiempo_json = time.time() - inicio

    return {
        "tiempo":     tiempo_json,
        "total":      total_filas,
        "edad_prom":  total_edad / total_filas if total_filas else 0,
        "temp_prom":  total_temp / total_filas if total_filas else 0
    }
