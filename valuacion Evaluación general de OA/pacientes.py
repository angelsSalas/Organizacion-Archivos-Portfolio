import pandas as pd
import csv
import json
import time
import os

# ================================================================
#  PACIENTES.PY
#  Responsabilidad: agregar nuevos pacientes y buscar existentes
# ================================================================

def agregar_paciente(tamano, nombre, edad, temperatura, presion, medicamento, especialidad):
    """
    Agrega una nueva fila al final del CSV y del JSON garantizando la paridad de datos
    y previniendo la corrupción de líneas agregando un salto de línea inicial.
    """
    archivo_csv  = f"datos_{tamano}.csv"
    archivo_json = f"datos_{tamano}.json"

    # --- 1. AGREGAR AL CSV ---
    # Revisamos si el archivo termina con salto de línea para evitar corromper las columnas
    necesita_salto = False
    if os.path.exists(archivo_csv) and os.path.getsize(archivo_csv) > 0:
        with open(archivo_csv, 'rb') as f_binary:
            f_binary.seek(-1, os.SEEK_END)
            if f_binary.read(1) != b'\n':
                necesita_salto = True

    with open(archivo_csv, mode='a', encoding='utf-8') as f:
        if necesita_salto:
            f.write('\n') # Forzamos el salto de línea si no existía antes

        escritor = csv.DictWriter(f, fieldnames=["id", "nombre", "edad", "temperatura", "presion", "medicamento", "especialidad"])
        escritor.writerow({
            "id":           "nuevo",
            "nombre":       nombre,
            "edad":         edad,
            "temperatura":  temperatura,
            "presion":      presion,
            "medicamento":  medicamento,
            "especialidad": especialidad
        })

    # --- 2. AGREGAR AL JSON (Formato línea por línea compatible) ---
    estructura_json = {
        "id": "nuevo",
        "nombre": nombre,
        "edad": edad,
        "especialidad": especialidad,
        "consulta": {
            "temperatura": temperatura,
            "presion": presion,
            "medicamento": medicamento
        }
    }
    
    with open(archivo_json, mode='a', encoding='utf-8') as f_json:
        # json.dumps escribe el objeto en una sola línea compacta
        f_json.write(json.dumps(estructura_json, ensure_ascii=False) + "\n")

    print(f"  [OK] Paciente '{nombre}' agregado correctamente en CSV y JSON.")


def buscar_paciente(tamano, criterio):
    """
    Recorre el CSV en bloques filtrando por ID o nombre.
    Muestra máximo 3 coincidencias para no inundar la pantalla.
    """
    print(f"\n  Buscando '{criterio}'...")
    encontrados = []
    inicio      = time.time()

    # Leemos el archivo en bloques cuidando la memoria RAM
    for bloque in pd.read_csv(f"datos_{tamano}.csv", chunksize=200_000):
        # Convertimos la columna 'id' a string temporalmente para poder buscar IDs tipo "nuevo" o números sin error
        bloque['id'] = bloque['id'].astype(str)
        
        if criterio.isdigit():
            # Si buscas un número, comparamos strings directos
            resultado = bloque[bloque['id'] == criterio]
        else:
            # Si buscas texto, buscamos coincidencias en el nombre o en el ID "nuevo"
            resultado = bloque[
                bloque['nombre'].str.contains(criterio, case=False, na=False) |
                (bloque['id'] == criterio)
            ]

        if not resultado.empty:
            encontrados.append(resultado)
            if len(encontrados) >= 3:
                break

    print(f"  Búsqueda terminada en {time.time() - inicio:.2f}s")

    if encontrados:
        # Combinamos los bloques con hallazgos y los imprimimos ordenadamente
        df_final = pd.concat(encontrados)
        print("\n  Registros encontrados:")
        print(df_final.head(3).to_string(index=False))
    else:
        print("  No se encontraron registros.")