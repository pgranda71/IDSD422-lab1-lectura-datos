
# Informe técnico — Consolidación de reportes de ventas

**Para:** Gerencia de RetailAndina S.A.  
**De:** Equipo de Business Intelligence  
**Fecha:** 16/10/2026  
**Asunto:** Primer análisis de los reportes de ventas (semana 39)

---

## Resumen ejecutivo

Se analizaron los reportes de ventas provenientes del ERP de sucursales, la API de fidelización y el consolidado de finanzas, disponibles en formatos CSV, JSON y Excel. Mediante Python y R se confirmó que los tres archivos contienen cinco registros y cuatro columnas, con información equivalente. Los resultados permitieron identificar las sucursales y regiones con mayores y menores ventas. Se recomienda implementar controles de calidad y automatizar el procesamiento de los datos para facilitar la toma de decisiones.

## 1. ¿Los tres formatos contienen la misma información?

Se cargaron los archivos CSV, JSON y Excel utilizando Python y R, con el objetivo de comparar sus dimensiones, estructura y contenido. Los resultados obtenidos fueron los siguientes:

| Formato | Origen | Filas | Columnas | Lectura en código |
|---|---|---|---|---|
| CSV | ERP de sucursales | 5 | 4 | Python: `pd.read_csv()` / R: `read.csv()` |
| JSON | API de fidelización | 5 | 4 | Python: `json.load()` y `pd.json_normalize()` / R: `fromJSON()` |
| Excel | Consolidado de finanzas | 5 | 4 | Python: `pd.read_excel()` / R: `read_excel()` |

**¿La estructura interna del archivo cambia el contenido?**

No necesariamente. Aunque los tres formatos almacenan la información de manera diferente, se observó que contienen los mismos registros y variables. CSV utiliza texto plano organizado mediante separadores, JSON permite representar información mediante objetos y arreglos, mientras que Excel almacena los datos en hojas de cálculo.

Estas diferencias influyen en la forma de leer y procesar los archivos, pero no modifican necesariamente los datos. En este caso, Python y R permitieron obtener estructuras tabulares equivalentes a partir de los tres formatos.

## 2. Tipos de datos y calidad

Al inspeccionar los archivos en Python y R, se identificaron los siguientes tipos de datos:

| Variable | Tipo inferido (Python) | Tipo inferido (R) | Interpretación |
|---|---|---|---|
| `ventas` | `int64` | `integer` / `numeric` | Valores numéricos de las ventas |
| `clientes` | `int64` | `integer` / `numeric` | Cantidad de clientes registrados |
| `sucursal` | `object` | `character` | Nombre de cada sucursal |
| `region` | `object` | `character` | Región geográfica de la sucursal |

En Python, las columnas `ventas` y `clientes` fueron identificadas como números enteros de tipo `int64`, mientras que `sucursal` y `region` se representaron como `object`.

En R, las variables de texto se identificaron como `character`. Las variables numéricas se representaron como `integer` al leer CSV y JSON, y como `numeric` (`double`) al importar Excel mediante `readxl`.

Los tipos identificados son adecuados para realizar cálculos y agrupaciones, ya que las ventas y los clientes son valores numéricos, mientras que las sucursales y regiones representan categorías.

**¿Qué habría indicado un dato sucio si `ventas` llegara como texto?**

Si la columna `ventas` hubiera sido identificada como texto, podría indicar problemas en la calidad de los datos, como espacios adicionales, símbolos monetarios, caracteres especiales o valores no numéricos.

Esto dificultaría operaciones como sumas y promedios, por lo que sería necesario realizar una limpieza y conversión de tipos antes de calcular los indicadores comerciales.

## 3. Particularidades técnicas encontradas

**CSV:** Se utilizó `pd.read_csv()` en Python y `read.csv()` en R. Ambos lenguajes permitieron cargar directamente los datos en una estructura tabular, identificando correctamente las columnas y sus tipos. Este formato resultó sencillo de procesar debido a su estructura de texto plano.

**JSON:** En Python fue necesario utilizar `json.load()` para cargar el archivo y `pd.json_normalize()` para transformarlo en un DataFrame. En R se utilizó `fromJSON()` de la librería `jsonlite`, obteniendo una estructura tabular. Esto demuestra que JSON puede requerir un proceso de transformación dependiendo de cómo estén organizados sus datos.

**Excel:** En Python se utilizó `pd.read_excel()` y en R la función `read_excel()` de la librería `readxl`. En ambos casos se indicó la hoja denominada `ventas` para cargar la información correspondiente. A diferencia de CSV, Excel puede contener múltiples hojas y requiere seleccionar la información que se desea analizar.

**Variables categóricas:** En Python, las columnas `sucursal` y `region` se representaron mediante el tipo `object`. En R se identificaron como `character`, aunque también pueden convertirse a `factor` cuando se necesita trabajar con categorías definidas.

En general, las diferencias encontradas estuvieron relacionadas con las funciones de lectura, las librerías utilizadas y la representación de los tipos de datos, sin afectar los valores observados.

## 4. Indicadores para la reunión del lunes

Se calcularon los principales indicadores comerciales a partir de los cinco registros de ventas.

| Indicador | Valor |
|---|---|
| Venta promedio por sucursal | 12.008 |
| Ticket promedio (ventas totales ÷ clientes totales) | 38,08 |
| Sucursal con mayor venta | Guayaquil Centro (15.200) |
| Sucursal con menor venta | Cuenca (8.540) |
| Región con mayor venta total | Sierra (30.860) |

### Análisis de los indicadores

**Venta promedio por sucursal:**

El promedio general de ventas de las cinco sucursales fue de 12.008. Los valores registrados fueron:

| Sucursal | Venta |
|---|---:|
| Quito Norte | 12.450 |
| Quito Sur | 9.870 |
| Guayaquil Centro | 15.200 |
| Guayaquil Norte | 13.980 |
| Cuenca | 8.540 |

Cada sucursal tiene un único registro, por lo que su venta promedio coincide con la venta registrada.

**Ticket promedio:**

El ticket promedio general obtenido fue de **38,07**, calculado mediante la división de las ventas totales entre el número total de clientes.

Este indicador representa el valor promedio de ventas generado por cada cliente y permite evaluar el comportamiento comercial de las sucursales.


**Sucursal con mayor y menor venta:**

Guayaquil Centro presentó el mayor valor de ventas, con 15.200, mientras que Cuenca registró el menor, con 8.540. Esta diferencia permite identificar oportunidades para evaluar el desempeño comercial de cada sucursal.

**Región con mayor venta total:**

La región Sierra registró ventas acumuladas de 30.860, mientras que la región Costa alcanzó 29.180.

Por lo tanto, Sierra fue la región con mayor venta total, aunque la sucursal individual con mayores ventas pertenece a la Costa.

## 5. Conclusiones y recomendaciones

### Conclusiones

1. **Consistencia de la información:** Los archivos CSV, JSON y Excel contienen los mismos cinco registros y cuatro columnas. Al procesarlos en Python y R se obtuvieron resultados equivalentes, lo que demuestra que es posible trabajar con diferentes formatos sin alterar la información original.

2. **Tipos de datos y procesamiento:** Ambos lenguajes identificaron correctamente las variables numéricas y de texto, aunque utilizan diferentes representaciones para algunos tipos de datos. Se comprobó que cada formato requiere métodos de lectura específicos, pero todos permiten obtener información tabular adecuada para realizar análisis comerciales.

3. **Análisis de indicadores:** Los resultados permitieron identificar a Guayaquil Centro como la sucursal con mayores ventas, a Cuenca como la de menores ventas y a Sierra como la región con mayor venta acumulada. Estos indicadores proporcionan información útil para comparar el desempeño comercial entre sucursales y regiones.

### Recomendaciones

- **Validar la consistencia de los datos:** Comprobar que los registros de las diferentes fuentes coincidan antes de consolidarlos, evitando duplicaciones o inconsistencias que puedan afectar los resultados.

- **Implementar controles de calidad:** Verificar los tipos de datos, identificar valores nulos, detectar registros duplicados y revisar posibles errores en las variables numéricas antes de realizar los cálculos.

- **Automatizar el análisis:** Utilizar Python o R para automatizar la lectura de archivos y el cálculo de indicadores, reduciendo el trabajo manual y facilitando la actualización periódica de los reportes.

- **Dar seguimiento al desempeño comercial:** Comparar las ventas entre sucursales y regiones en distintos períodos para identificar tendencias, oportunidades de mejora y posibles cambios en el comportamiento de los clientes.
