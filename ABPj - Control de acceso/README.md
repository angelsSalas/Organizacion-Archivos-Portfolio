# Proyecto 2: Sistema de Control de Acceso y Auditoría Externa - Maquiladora

## 1. Descripción del Sistema
Este módulo es una solución de seguridad perimetral diseñada para regular el ingreso de personal a las instalaciones de una planta maquiladora. El sistema se compone de un módulo local de autenticación desarrollado en **Python** que emula un lector de tarjetas y un monitor web de supervisión en tiempo real desarrollado en **PHP, HTML5 y CSS3**. El sistema intercepta las solicitudes de acceso, evalúa los privilegios del empleado y genera registros automáticos de auditoría para mitigar riesgos de intrusión.

---

## 2. Arquitectura de Archivos y Flujo de Datos
La estructura interna sigue los lineamientos de arquitectura limpia exigidos por la rúbrica institucional, centralizando el código fuente dentro del directorio `src/`:

1. **`src/usuarios.json`**: Base de datos local estructurada que almacena los ID de tarjetas, nombres de empleados, departamentos y niveles de seguridad.
2. **`src/control.py`**: Lógica central del lector de accesos (Python). Lee el archivo JSON, procesa las entradas en bucle y despacha eventos.
3. **`src/auditoria.txt`**: Archivo secuencial plano de persistencia permanente que funciona como bitácora inmutable de eventos.
4. **`src/index.php`**: Monitor de seguridad web que parsea y renderiza los datos de la bitácora, aplicando estilos dinámicos automáticos ante alertas de vulneración.
5. **`src/style.css`**: Hoja de estilos encargada del diseño responsivo, tipografías y codificación por colores de la interfaz de seguridad.

---

## 3. Justificación Científica de Formatos y Modos de Acceso

### Estructura de Datos en Formato Organizado (`usuarios.json`)
* **Justificación:** Se seleccionó el formato **JSON (JavaScript Object Notation)** para la lista de usuarios autorizados porque proporciona una organización jerárquica nativa basada en pares clave-valor. Esto permite almacenar estructuras complejas de los empleados (como objetos con niveles de seguridad y departamentos) sin el sobrecosto de un motor de base de datos relacional, asegurando portabilidad y una sintaxis estandarizada legible tanto para Python como para PHP.
* **Modo de Acceso:** En Python se utiliza el método de acceso exclusivo de lectura `r` (`open("usuarios.json", "r")`), cargando los datos eficientemente a memoria con `json.load()` para realizar búsquedas optimizadas mediante comparaciones lógicas.

### Registro de Eventos Secuenciales (`auditoria.txt`)
* **Justificación:** Se implementa un archivo de texto plano para la bitácora debido a que los registros de auditoría requieren un almacenamiento puramente secuencial con la marca de tiempo exacta de los eventos. 
* **Modo de Acceso:** * En Python se abre usando el modo de anexado `a` (`open("auditoria.txt", "a")`), el cual es crucial en ingeniería de datos ya que posiciona el puntero al final del archivo de forma automática, garantizando que los nuevos ingresos se concatenen de manera segura sin destruir o sobrescribir el historial preexistente.
  * En PHP se utiliza el modo de lectura lineal continua `r` (`fopen("auditoria.txt", "r")`) combinado con un ciclo iterativo `fgets()`, extrayendo línea por línea para no saturar la memoria del servidor al renderizar registros masivos.

---

## 4. Evitada de Código Fijo (Anti-Hardcoded)
Para asegurar el cumplimiento de las buenas prácticas de desarrollo, el sistema no contiene identificadores de tarjetas ni nombres de empleados quemados (*hardcoded*) en el código fuente. Toda validación de identidad se resuelve dinámicamente mapeando el archivo de configuración externo `usuarios.json`, lo que permite dar de alta o baja personal de forma externa sin alterar la lógica de programación.
