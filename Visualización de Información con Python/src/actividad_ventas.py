import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo CSV
datos_ventas = pd.read_csv("ventas_tecnologia.csv")

# Crear columna de ingresos
datos_ventas["ingresos"] = datos_ventas["cantidad"] * datos_ventas["precio_unitario"]

# -----------------------------
# REPORTES TABULARES
# -----------------------------

# 1. Ventas totales por producto
ventas_producto = datos_ventas.groupby("producto")["cantidad"].sum()

# 2. Ventas totales por mes
ventas_mes = datos_ventas.groupby("mes")["cantidad"].sum()

# 3. Ingresos generados por producto
ingresos_producto = datos_ventas.groupby("producto")["ingresos"].sum()

# 4. Producto más vendido
producto_mas_vendido = ventas_producto.idxmax()

print("===== VENTAS POR PRODUCTO =====")
print(ventas_producto)

print("\n===== VENTAS POR MES =====")
print(ventas_mes)

print("\n===== INGRESOS POR PRODUCTO =====")
print(ingresos_producto)

print("\nProducto más vendido:")
print(producto_mas_vendido)

# -----------------------------
# GRÁFICAS
# -----------------------------

# Gráfica de barras
ventas_producto.plot(kind='bar', color='green')
plt.title("Ventas por Producto")
plt.xlabel("Producto")
plt.ylabel("Cantidad Vendida")
plt.show()

# Gráfica de líneas
ventas_mes.plot(kind='line', marker='o', color='blue')
plt.title("Evolución Mensual de Ventas")
plt.xlabel("Mes")
plt.ylabel("Cantidad Vendida")
plt.show()

# Gráfica circular
ventas_producto.plot(
    kind='pie',
    autopct='%1.1f%%',
    colors=['green', 'yellow', 'orange', 'red']
)

plt.title("Porcentaje de Ventas por Producto")
plt.ylabel("")
plt.show()

# -----------------------------
# JERARQUÍA DE INFORMACIÓN
# -----------------------------

producto_mayor_ingreso = ingresos_producto.idxmax()
producto_menos_vendido = ventas_producto.idxmin()
mes_mas_rentable = datos_ventas.groupby("mes")["ingresos"].sum().idxmax()

print("\n===== ANÁLISIS =====")
print("Producto con mayores ingresos:", producto_mayor_ingreso)
print("Producto menos vendido:", producto_menos_vendido)
print("Mes más rentable:", mes_mas_rentable)
print("Producto prioritario para inventario:", producto_mas_vendido)

# -----------------------------
# INTERPRETACIÓN FINAL
# -----------------------------

print("\n===== INTERPRETACIÓN =====")
print(f"El producto más importante para la empresa es {producto_mayor_ingreso},")
print("porque genera la mayor cantidad de ingresos.")

print("La información crítica para tomar decisiones son:")
print("- Las ventas mensuales")
print("- Los ingresos")
print("- Los productos más vendidos")

print(f"El producto que debería promocionarse más es {producto_menos_vendido},")
print("porque tiene pocas ventas.")

print(f"El mejor mes para ventas fue {mes_mas_rentable}.")