import random

# Configuración del archivo de salida según el requerimiento 
ARCHIVO_MAESTRO = "maestro.txt"
CANTIDAD_REGISTROS = 500  # Rango permitido: 100 a 1,000 

# Listas de datos para generar registros realistas 
colores = ["Rojo", "Azul", "Verde", "Negro", "Blanco", "Amarillo", "Naranja"]
materiales = ["Metal", "Plástico Reforzado", "Aleación Ligera", "Fibra de Carbono (Simulada)"]
tipos_chasis = ["Deportivo", "Off-Road", "Clásico", "Low-Rider", "Prototipo"]
modelos = ["Twin Mill", "Bone Shaker", "Rodger Dodger", "Deora II", "Muscle Tone", "Night Shifter"]

def generar_dataset():
    try:
        with open(ARCHIVO_MAESTRO, "w", encoding="utf-8") as archivo:
            # Encabezado para facilitar el parseo posterior
            # archivo.write("ID|Modelo|Color|Material|Chasis|Año\n") 
            
            for i in range(1, CANTIDAD_REGISTROS + 1):
                # Generación de atributos
                id_prod = f"HW-{2026}-{i:04d}" 
                modelo = random.choice(modelos)
                color = random.choice(colores)
                material = random.choice(materiales)
                chasis = random.choice(tipos_chasis)
                anio = random.randint(1968, 2026) #origen de los carros
                
                # Construcción de la línea (Registro)
                registro = f"{id_prod}|{modelo}|{color}|{material}|{chasis}|{anio}\n"
                
                # Escritura en el archivo plano 
                archivo.write(registro)
                
        print(f"Éxito: Se ha generado '{ARCHIVO_MAESTRO}' con {CANTIDAD_REGISTROS} registros.")
    
    except Exception as e:
        print(f"Error al generar el archivo: {e}")

if __name__ == "__main__":
    generar_dataset()