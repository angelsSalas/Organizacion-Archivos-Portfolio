# Proyecto 4: Sistema de Procesamiento de Big Data Hospitalaria y Análisis Comparativo de Rendimiento

## 1. Descripción del Sistema
Este sistema es una plataforma analítica de alto rendimiento diseñada para la ingesta, manipulación, búsqueda y abstracción estadística de conjuntos de datos masivos (Big Data) en entornos hospitalarios, procesando volúmenes de **1, 10 y 20 millones de registros** de pacientes. El software evalúa de forma empírica la eficiencia algorítmica y el comportamiento de las estructuras de persistencia mediante un análisis comparativo de tiempos de respuesta y consumo de recursos entre arquitecturas de datos planas y jerárquicas.

---

## 2. Arquitectura de Archivos y Flujo de Datos
El proyecto implementa un diseño modular basado en el principio de responsabilidad única. La arquitectura de software se distribuye en los siguientes componentes dentro de `src/`:

1. **`src/menu.py`**: Orquestador principal de la aplicación. Gestiona el ciclo de vida del programa y provee la interfaz de usuario por consola.
2. **`src/datos.py`**: Capa de abstracción de datos. Contiene los motores lógicos optimizados para la lectura y parsing de archivos masivos.
3. **`src/pacientes.py`**: Módulo transaccional. Responsable de la inserción y búsqueda de registros garantizando la paridad entre formatos.
4. **`src/estadisticas.py`**: Motor de agregación numérica encargado de computar promedios, máximos y mínimos operando sobre la memoria RAM.
5. **`src/graficas.py`**: Interfaz de visualización estadística que renderiza dashboards analíticos interactivos a partir de submuestreos.

---

## 3. Justificación Científica de Formatos, Modos de Acceso y Optimización de RAM

### Estructura de Almacenamiento Plana vs. Jerárquica (`.csv` vs `.json`)
* **Formato CSV (Tabla Plana):** Utilizado para el almacenamiento masivo transaccional uniforme. Al estructurarse mediante registros de longitud variable delimitados estrictamente por comas, minimiza el costo de almacenamiento por nodo (*overhead*), ideal para operaciones matriciales masivas.
* **Formato JSON (Estructura Jerárquica Anidada):** Utilizado para simular expedientes clínicos complejos que requieren anidamiento de datos (por ejemplo, el objeto interno `consulta` que agrupa los signos vitales `temperatura`, `presion` y `medicamento`). Provee una semántica autodescriptiva estructurada y portátil.

### Estrategias de Optimización para la Mitigación de Agotamiento de Memoria (RAM)
* **Procesamiento de CSV por Bloques (*Chunking*):** Al procesar archivos con millones de líneas, cargarlos por completo en la memoria RAM provocaría un colapso del sistema (*Out of Memory*). Para mitigar esto, en `datos.py` se implementa la carga fraccionada mediante el parámetro `chunksize=100000` de **Pandas**. El sistema procesa los datos secuencialmente en bloques iterativos, manteniendo una huella de memoria RAM constante y reducida sin importar el tamaño total del dataset original.
* **Procesamiento de JSON mediante Flujo de Líneas (*Streaming*):** A diferencia de un archivo JSON convencional estructurado como un arreglo masivo que requiere cargarse por completo en memoria para ser parseado, este sistema implementa un diseño híbrido donde cada línea representa un objeto JSON independiente separado por saltos de línea (`\n`). Esto permite abrir el archivo en modo de lectura nativo `r` y recorrerlo mediante un ciclo lineal que procesa línea por línea (`json.loads(linea)`), descartando el objeto de la memoria inmediatamente después de extraer sus valores métricos acumulados.

---

## 4. Evitada de Código Fijo (Anti-Hardcoded) y Modularidad
El sistema cumple rigurosamente con los estándares institucionales de código limpio al aislar por completo las variables del negocio. No existen rutas de archivos estáticas fijadas en el código; los nombres de los recursos se construyen de forma dinámica en tiempo de ejecución basándose en el volumen seleccionado por el usuario (`f"datos_{nuevo_tamano}.csv"`). Todas las funciones de cálculo son genéricas y parametrizables, lo que permite modificar el origen de los datos o escalar los límites de procesamiento sin reescribir la lógica algorítmica fundamental.
