import os

# Importamos las funciones de cada archivo del proyecto
from datos        import leer_csv, leer_json
from pacientes    import agregar_paciente, buscar_paciente
from estadisticas import mostrar_reporte, mostrar_estadisticas
from graficas     import mostrar_dashboard

# ================================================================
#  MENU.PY (Versión Mejorada)
#  Responsabilidad: coordinar todo el sistema
#  Es el único archivo que se ejecuta directamente
# ================================================================

# Variables compartidas entre todas las opciones del menú
tamano                 = 0
estadisticas           = {}
top_medicamentos       = None
consultas_especialidad = None
muestra_edades         = []
temp_por_edad          = None
tiempo_csv             = 0
tiempo_json            = 0


def seleccionar_tamano():
    """
    Muestra un submenú sencillo para elegir el tamaño de datos
    sin necesidad de escribir todos los ceros.
    """
    print("\n  --- SELECCIÓN DE GRUPO DE DATOS ---")
    print("  1. 1,000,000 registros (1 Millón)")
    print("  2. 10,000,000 registros (10 Millones)")
    print("  3. 20,000,000 registros (20 Millones)")
    
    eleccion = input("\n  Elige una opción (1/2/3): ").strip()
    
    if eleccion == "1":
        return 1_000_000
    elif eleccion == "2":
        return 10_000_000
    elif eleccion == "3":
        return 20_000_000
    else:
        print("  [!] Opción inválida. No se cambió el grupo de datos.")
        return None


def cargar_datos(nuevo_tamano):
    """
    Lee el CSV y el JSON del tamaño elegido.
    Guarda los resultados en las variables compartidas.
    """
    global tamano, estadisticas, top_medicamentos
    global consultas_especialidad, muestra_edades
    global temp_por_edad, tiempo_csv, tiempo_json

    archivo_csv  = f"datos_{nuevo_tamano}.csv"
    archivo_json = f"datos_{nuevo_tamano}.json"

    if not os.path.exists(archivo_csv) or not os.path.exists(archivo_json):
        print(f"\n  [Error] No se encontraron los archivos para {nuevo_tamano:,} registros.")
        print("  Ejecuta primero generador_datos.py")
        return False

    print(f"\n{'='*55}")
    print(f"  CARGANDO DATOS ({nuevo_tamano:,} REGISTROS)")
    print(f"{'='*55}")

    # 1. Cargar y procesar CSV
    resultados_csv = leer_csv(archivo_csv)
    tiempo_csv     = resultados_csv["tiempo"]

    # 2. Cargar y procesar JSON
    resultados_json = leer_json(archivo_json)
    tiempo_json      = resultados_json["tiempo"]

    # Guardar en variables globales para las otras opciones
    tamano                 = nuevo_tamano
    estadisticas           = resultados_csv["estadisticas"]
    top_medicamentos       = resultados_csv["top_medicamentos"]
    consultas_especialidad = resultados_csv["consultas_especialidad"]
    muestra_edades         = resultados_csv["muestra_edades"]
    temp_por_edad          = resultados_csv["temp_por_edad"]

    # Agregar los tiempos al diccionario de estadísticas para la comparativa
    estadisticas["tiempo_csv"]  = tiempo_csv
    estadisticas["tiempo_json"] = tiempo_json

    print(f"\n  [OK] ¡Datos cargados con éxito!")
    print(f"  -> Tiempo CSV:  {tiempo_csv:.2f} segundos")
    print(f"  -> Tiempo JSON: {tiempo_json:.2f} segundos")
    return True


def menu():
    global tamano, estadisticas, top_medicamentos
    global consultas_especialidad, muestra_edades, temp_por_edad

    # Forzar la selección del tamaño al arrancar el programa por primera vez
    print("=== BIENVENIDO AL SISTEMA HOSPITALARIO ===")
    while tamano == 0:
        opcion_tamano = seleccionar_tamano()
        if opcion_tamano:
            if not cargar_datos(opcion_tamano):
                # Si los archivos no existen, reiniciamos el bucle para que elija otra opción
                tamano = 0 

    while True:
        print(f"\n=============================================")
        print(f"  MENÚ PRINCIPAL  (datos actuales: {tamano:,})")
        print(f"=============================================")
        print("  1. Cambiar grupo de datos")
        print("  2. Agregar nuevo paciente")
        print("  3. Buscar paciente (por ID o nombre)")
        print("  4. Ver reporte médico completo")
        print("  5. Ver estadísticas básicas")
        print("  6. Ver gráficas del dashboard")
        print("  7. Salir")

        opcion = input("\n  Elige una opción: ").strip()

        if opcion == "1":
            opcion_tamano = seleccionar_tamano()
            if opcion_tamano and opcion_tamano != tamano:
                cargar_datos(opcion_tamano)

        elif opcion == "2":
            nombre       = input("  Nombre: ")
            edad         = int(input("  Edad: "))
            temperatura  = float(input("  Temperatura: "))
            presion      = input("  Presión (ej. 120/80): ")
            medicamento  = input("  Medicamento: ")
            especialidad = input("  Especialidad: ")
            agregar_paciente(tamano, nombre, edad, temperatura, presion, medicamento, especialidad)

        elif opcion == "3":
            criterio = input("  ID o nombre a buscar: ").strip()
            if criterio:
                buscar_paciente(tamano, criterio)

        elif opcion == "4":
            if estadisticas:
                mostrar_reporte(tamano, estadisticas, top_medicamentos, consultas_especialidad)
            else:
                print("  [!] Carga los datos primero (opción 1).")

        elif opcion == "5":
            if estadisticas:
                mostrar_estadisticas(tamano, estadisticas)
            else:
                print("  [!] Carga los datos primero (opción 1).")

        elif opcion == "6":
            if estadisticas:
                mostrar_dashboard(tamano, muestra_edades, consultas_especialidad, temp_por_edad, top_medicamentos)
            else:
                print("  [!] Carga los datos primero (opción 1).")

        elif opcion == "7":
            print("  ¡Hasta luego!")
            break

        else:
            print("  [!] Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()