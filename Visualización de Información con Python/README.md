# Proyecto 3: Procesamiento, Jerarquía y Visualización Estadístico de Datos de Ventas

## 1. Descripción del Sistema
Este sistema es un módulo de análisis de inteligencia de negocios (*Business Intelligence*) desarrollado íntegramente en **Python 3**. Su propósito central es la ingesta de grandes volúmenes de datos transaccionales, el cálculo de métricas financieras indexadas en memoria y la posterior abstracción de la información crítica mediante reportes tabulares y componentes de graficación estadística interactiva de alto nivel.

---

## 2. Arquitectura de Archivos y Flujo de Datos
De acuerdo con los lineamientos de arquitectura limpia institucionales, el código fuente y el dataset origen se aíslan rigurosamente dentro del directorio `src/`:

1. **`src/ventas_tecnologia.csv`**: Repositorio de persistencia plano estructurado que almacena el histórico de transacciones comerciales de la organización.
2. **`src/analisis_ventas.py`**: Motor lógico principal (equivalente a tu script de procesamiento). Realiza la carga de datos, transformaciones analíticas, tabulaciones y despacha la renderización de interfaces gráficas.

---

## 3. Justificación Científica de Formatos y Modos de Acceso

### Persistencia de Datos Organizada (`ventas_tecnologia.csv`)
* **Justificación:** Se seleccionó el formato **CSV (Comma-Separated Values)** como el estándar para el almacenamiento del histórico transaccional debido a su naturaleza de texto plano delimitado por caracteres estructurados. Científicamente, esto garantiza una interoperabilidad absoluta entre sistemas híbridos de software, eliminando los metadatos propietarios redundantes de las suites ofimáticas convencionales. Esto optimiza los tiempos de transferencia de archivos por canal de red (*low overhead*) y permite cargas masivas a memoria a velocidades computacionales óptimas.
* **Modos de Acceso y Manipulación:** La lectura del recurso se gestiona mediante la biblioteca científica de alto rendimiento **Pandas** a través del método nativo `pd.read_csv()`. Este proceso lee el archivo de manera secuencial e inicializa una estructura indexada en la memoria RAM del sistema (*DataFrame*), lo que agiliza los ciclos iterativos concurrentes al realizar agrupaciones de información complejas mediante operaciones matriciales vectorizadas (`.groupby()`).

### Jerarquía e Interfaz Gráfica de Información
* **Justificación de Visualizaciones (`Matplotlib`):** El cerebro humano procesa imágenes con mayor velocidad que los textos planos secuenciales. Por lo tanto, el sistema implementa una abstracción visual de tres ejes jerárquicos:
  * **Gráfica de Barras:** Utilizada para el análisis comparativo inmediato y discreto de volumen físico de inventario por producto.
  * **Gráfica de Líneas:** Diseñada científicamente con marcadores nodales continuos para trazar series de tiempo y detectar tendencias, valles o picos de demanda estacional mensual.
  * **Gráfica Circular (*Pie Chart*):** Implementada con cálculos proporcionales automatizados (`autopct`) para ilustrar la composición porcentual y la participación de mercado de los ingresos, facilitando la toma de decisiones ejecutivas en el inventariado prioritario.

---

## 4. Evitada de Código Fijo y Manejo Limpio (Anti-Hardcoded)
El script de análisis matemático no contiene valores numéricos estáticos ni parámetros de negocio fijos (*hardcoded*) incrustados dentro de los algoritmos de cálculo. Métricas críticas como el "Producto con mayores ingresos" (`idxmax()`) o el "Mes más rentable" se determinan de forma totalmente dinámica y en tiempo de ejecución, permitiendo que el dataset `ventas_tecnologia.csv` incremente exponencialmente su número de registros sin necesidad de modificar una sola línea de código fuente.
