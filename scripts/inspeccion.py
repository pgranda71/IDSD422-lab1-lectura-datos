# inspeccion.py — Tipos, columna derivada e indicadores (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/inspeccion.py

# TODO 1: carga data/ventas.csv
# TODO 2: imprime los tipos (dtypes) de cada columna
# TODO 3: crea la columna derivada "ticket" = ventas / clientes
# TODO 4: calcula e imprime:
#         - venta promedio por sucursal
#         - ticket promedio (ventas totales / clientes totales)
#         - sucursal con mayor y menor venta
#         - región con mayor venta total

import pandas as pd

# TODO 1: Cargar data/ventas.csv
ventas = pd.read_csv("data/ventas.csv")

# TODO 2: Imprimir los tipos de cada columna
print("\n--- TIPOS DE DATOS ---")
print(ventas.dtypes)

# TODO 3: Crear la columna ticket = ventas / clientes
ventas["ticket"] = ventas["ventas"] / ventas["clientes"]

print("\n--- PRIMERAS FILAS CON TICKET ---")
print(ventas.head())

# TODO 4: Calcular e imprimir resultados

# Venta promedio por sucursal
print("\n--- VENTA PROMEDIO POR SUCURSAL ---")
print(ventas.groupby("sucursal")["ventas"].mean())

# Ticket promedio (ventas totales / clientes totales)
print("\n--- TICKET PROMEDIO GENERAL ---")
print(ventas["ventas"].sum() / ventas["clientes"].sum())

# Sucursal con mayor y menor venta total
ventas_sucursal = ventas.groupby("sucursal")["ventas"].sum()

print("\n--- SUCURSAL CON MAYOR VENTA TOTAL ---")
print(ventas_sucursal.idxmax())
print("Venta total:", ventas_sucursal.max())

print("\n--- SUCURSAL CON MENOR VENTA TOTAL ---")
print(ventas_sucursal.idxmin())
print("Venta total:", ventas_sucursal.min())

# Región con mayor venta total
ventas_region = ventas.groupby("region")["ventas"].sum()

print("\n--- REGIÓN CON MAYOR VENTA TOTAL ---")
print(ventas_region.idxmax())
print("Venta total:", ventas_region.max())
