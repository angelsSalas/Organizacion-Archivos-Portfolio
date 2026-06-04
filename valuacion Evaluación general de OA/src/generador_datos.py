import csv
import json
import random
import time
import os

# ================================================================
#  DATOS FICTICIOS
#  Listas de donde se escogen valores al azar para cada paciente
# ================================================================
NOMBRES        = ["Ana", "Carlos", "Luis", "Maria", "Jorge", "Elena", "Pedro", "Sofia", "Juan", "Laura"]
APELLIDOS      = ["Lopez", "Ruiz", "Gomez", "Martinez", "Sanchez", "Perez", "Diaz", "Torres", "Ramirez", "Flores"]
MEDICAMENTOS   = ["Paracetamol", "Ibuprofeno", "Amoxicilina", "Metformina", "Omeprazol", "Losartan", "Atorvastatina"]
ESPECIALIDADES = ["Pediatria", "Cardiologia", "Medicina General", "Ginecologia", "Traumatologia", "Nutricion"]

# ================================================================
#  PARTE 1 — CREAR UN PACIENTE
#  Genera los datos de un solo paciente de forma aleatoria
# ================================================================
def crear_paciente(id):
    return {
        "id":           id,
        "nombre":       f"{random.choice(NOMBRES)} {random.choice(APELLIDOS)}",
        "edad":         random.randint(1, 85),
        "temperatura":  round(random.uniform(36.0, 39.5), 1),
        "presion":      f"{random.randint(110, 140)}/{random.randint(70, 90)}",
        "medicamento":  random.choice(MEDICAMENTOS),
        "especialidad": random.choice(ESPECIALIDADES)
    }
# ================================================================
#  PARTE 2 — GUARDAR EN CSV
#  Escribe todos los pacientes en un archivo de tabla plana
# ================================================================
def guardar_csv(nombre_archivo, lista_pacientes):
    columnas = ["id", "nombre", "edad", "temperatura", "presion", "medicamento", "especialidad"]

    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()           # Primera fila: los nombres de columna
        escritor.writerows(lista_pacientes)  # Las demás filas: los datos
# ================================================================
#  PARTE 3 — GUARDAR EN JSON
#  Escribe todos los pacientes con estructura anidada (jerárquica)
# ================================================================
def guardar_json(nombre_archivo, lista_pacientes):
    estructura = {
        "pacientes": [
            {
                "id":           p["id"],
                "nombre":       p["nombre"],
                "edad":         p["edad"],
                "especialidad": p["especialidad"],
                "consulta": {          # Nivel interno con los signos vitales
                    "temperatura": p["temperatura"],
                    "presion":     p["presion"],
                    "medicamento": p["medicamento"]
                }
            }
            for p in lista_pacientes
        ]
    }
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(estructura, archivo, indent=2)
# ================================================================
#  PARTE 4 — PROGRAMA PRINCIPAL
#  Le pregunta al usuario cuántos registros quiere y genera ese grupo
# ================================================================
def main():
    opciones_validas = {"1000000", "10000000", "20000000"}

    print("=== GENERADOR DE DATOS HOSPITALARIOS ===\n")
    print("¿Cuántos registros deseas generar?")
    print("  1 → 1,000,000")
    print("  2 → 10,000,000")
    print("  3 → 20,000,000")

    eleccion = input("\nElige una opción (1/2/3): ").strip()

    if eleccion == "1":
        total = 1_000_000
    elif eleccion == "2":
        total = 10_000_000
    elif eleccion == "3":
        total = 20_000_000
    else:
        print("[!] Opción no válida. Saliendo.")
        return

    print(f"\nGenerando {total:,} pacientes...")
    pacientes = [crear_paciente(i) for i in range(1, total + 1)]

    # Medir tiempo de escritura CSV
    inicio      = time.time()
    archivo_csv = f"datos_{total}.csv"
    guardar_csv(archivo_csv, pacientes)
    tiempo_csv  = time.time() - inicio
    peso_csv    = os.path.getsize(archivo_csv) / 1024   # Bytes → KB

    # Medir tiempo de escritura JSON
    inicio       = time.time()
    archivo_json = f"datos_{total}.json"
    guardar_json(archivo_json, pacientes)
    tiempo_json  = time.time() - inicio
    peso_json    = os.path.getsize(archivo_json) / 1024

    print(f"\n  CSV  → {tiempo_csv:.2f}s  |  {peso_csv:,.0f} KB")
    print(f"  JSON → {tiempo_json:.2f}s  |  {peso_json:,.0f} KB")
    print(f"\n[OK] Archivos 'datos_{total}.csv' y 'datos_{total}.json' generados.")

if __name__ == "__main__":
    main()