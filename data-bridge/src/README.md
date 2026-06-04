# Proyecto 1: Data Bridge - Sistema de Filtrado e Interfaz Dinámica para Hot Wheels

## 1. Descripción del Sistema
Este sistema funciona como un puente de datos corporativo (*Data Bridge*) dividido en dos capas operativas principales. La primera es un módulo de simulación e inserción masiva desarrollado en **Python**, capaz de estructurar colecciones de datos bajo reglas consistentes. La segunda es una plataforma web desarrollada en **PHP, HTML5 y CSS3** encargada del filtrado dinámico secuencial en tiempo real, permitiendo aislar registros específicos mediante consultas por palabras clave.

---

## 2. Arquitectura de Archivos y Flujo de Datos
El sistema implementa una arquitectura limpia, aislando la lógica operativa y de interfaz dentro de la subcarpeta `src/`. El flujo de datos sigue este orden secuencial:

1. **`src/generacion.py`**: Script central de automatización encargado de poblar el almacén primario con estructuras aleatorias controladas.
2. **`src/maestro.txt`**: Almacén masivo de persistencia plano que resguarda el inventario completo separado por delimitadores.
3. **`src/formulario.html`**: Interfaz de usuario que captura los parámetros de filtrado mediante métodos síncronos `POST`.
4. **`src/procesar.php`**: Motor de búsqueda que implementa un ciclo de lectura lineal para interceptar coincidencias.
5. **`src/filtrado.txt`**: Archivo de salida temporal que guarda los resultados de la consulta actual.
6. **`src/visualizar.php`**: Script encargado de parsear y renderizar los datos filtrados en una tabla HTML limpia y dinámica estructurada con **`src/estilos.css`**.

---

## 3. Justificación Científica de Formatos y Modos de Acceso

### Almacenamiento en Texto Plano Delimitado (`maestro.txt` y `filtrado.txt`)
* **Justificación:** Se seleccionó el formato de texto plano con codificación `UTF-8` y delimitadores por tuberías (`|`) debido a su bajísimo sobrecosto de almacenamiento (*overhead*). A diferencia de estructuras más pesadas como XML, el archivo de texto plano no requiere metadatos redundantes por cada registro, maximizando la eficiencia de almacenamiento por cada Hot Wheels generado.
* **Modos de Acceso:** * En Python se utiliza el modo de apertura `w` (`open(ARCHIVO_MAESTRO, "w")`) para la sobrescritura limpia de datasets de prueba masivos.
  * En PHP se emplean las funciones nativas `file()` y `file_put_contents()`, las cuales cargan las cadenas de texto en arreglos de memoria indexados, optimizando los tiempos de procesamiento en ráfagas de lectura/escritura secuencial lineal.

### Modos de Diseño y Estructura Web
* **Estilos Externos (`estilos.css`):** Se maneja de forma externa para mantener la modularidad de la arquitectura de software. Esto evita la mala práctica de incrustar estilos de manera estática o fija (*hardcoded*) en las plantillas de visualización PHP, garantizando un código limpio y escalable.

---

## 4. Evidencia de Código Limpio y Operaciones de Archivos
Toda la manipulación de datos en el sistema utiliza manejadores nativos con cierres automáticos seguros (`with open` en Python) o validaciones previas de existencia (`file_exists` en PHP), asegurando la integridad del sistema ante excepciones en tiempo de ejecución.
