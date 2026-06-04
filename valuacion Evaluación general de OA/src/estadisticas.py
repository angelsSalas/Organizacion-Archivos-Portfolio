# ================================================================
#  ESTADISTICAS.PY
#  Responsabilidad: mostrar reportes y estadísticas en consola
# ================================================================


def mostrar_reporte(tamano, estadisticas, top_medicamentos, consultas_especialidad):
    """
    Muestra un resumen completo: edades, temperaturas,
    medicamentos más usados y consultas por especialidad.
    """
    e = estadisticas

    print(f"\n{'='*45}")
    print(f"  REPORTE MÉDICO — {tamano:,} registros")
    print(f"{'='*45}")
    print(f"  Total de pacientes:   {e['total']:,}")

    print(f"\n  --- Edades ---")
    print(f"  Promedio:    {e['edad_prom']:.1f} años")
    print(f"  Mínima:      {e['edad_min']} años")
    print(f"  Máxima:      {e['edad_max']} años")

    print(f"\n  --- Temperaturas ---")
    print(f"  Promedio:    {e['temp_prom']:.2f} °C")
    print(f"  Máxima:      {e['temp_max']} °C")

    print(f"\n  --- Top 5 Medicamentos ---")
    for med, cant in top_medicamentos.items():
        print(f"  {med:<20} {int(cant):,} recetas")

    print(f"\n  --- Consultas por Especialidad ---")
    for esp, cant in consultas_especialidad.items():
        print(f"  {esp:<22} {int(cant):,} consultas")


def mostrar_estadisticas(tamano, estadisticas):
    """
    Versión corta: solo muestra promedios, máximos y mínimos.
    """
    e = estadisticas

    print(f"\n{'='*45}")
    print(f"  ESTADÍSTICAS BÁSICAS — {tamano:,} registros")
    print(f"{'='*45}")
    print(f"  Total registros:    {e['total']:,}")
    print(f"  Edad promedio:      {e['edad_prom']:.1f} años")
    print(f"  Edad mínima:        {e['edad_min']}")
    print(f"  Edad máxima:        {e['edad_max']}")
    print(f"  Temperatura prom:   {e['temp_prom']:.2f} °C")
    print(f"  Temperatura máx:    {e['temp_max']} °C")
