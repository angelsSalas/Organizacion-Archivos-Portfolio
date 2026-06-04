import matplotlib.pyplot as plt
import pandas as pd

# ================================================================
#  GRAFICAS.PY (Versión Simplificada)
#  Responsabilidad: generar visualizaciones usando el estilo directo de Pandas
# ================================================================

def mostrar_dashboard(tamano, muestra_edades, consultas_especialidad, temp_por_edad, top_medicamentos):
    """
    Muestra las 4 gráficas solicitadas de forma secuencial y sencilla,
    utilizando el método directo .plot() de Pandas.
    """
    print(f"\n  [Generando gráficas para {tamano:,} registros... Cierra cada ventana para ver la siguiente]")

    # 1. Histograma: Rango de edades
    # Convertimos la lista de muestra a una Serie de Pandas para usar .plot()
    df_edades = pd.Series(muestra_edades)
    df_edades.plot(kind='hist', bins=15, color='teal', edgecolor='black')
    plt.title(f"Pacientes por Rango de Edad ({tamano:,} reg.)")
    plt.xlabel("Edad")
    plt.ylabel("Cantidad de Pacientes")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

    # 2. Gráfica de barras: Consultas por especialidad
    consultas_especialidad.plot(kind='bar', color='purple')
    plt.title("Consultas por Especialidad")
    plt.xlabel("Especialidad")
    plt.ylabel("Cantidad de Consultas")
    plt.xticks(rotation=45, ha='right') # Inclinar texto para que no se amontone
    plt.tight_layout()
    plt.show()

    # 3. Gráfica de líneas: Temperatura promedio por grupo de edad
    temp_por_edad.plot(kind='line', marker='o', color='red', linewidth=2)
    plt.title("Temperatura Promedio por Rango de Edad")
    plt.xlabel("Rango de Edad")
    plt.ylabel("Temperatura (°C)")
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.show()

    # 4. Gráfica circular (Pie): Top 5 Medicamentos
    top_medicamentos.plot(kind='pie', autopct='%1.1f%%', startangle=90, 
                          colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
    plt.title("Porcentaje del Top 5 Medicamentos Recetados")
    plt.ylabel("") # Oculta la etiqueta del eje y
    plt.show()
