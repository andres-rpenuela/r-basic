# Medidas de Tendencia Central

Las medidas de tendencia central son valores que representan el "centro" o "punto medio" de un conjunto de datos.

## 1. Media (Promedio)

### Definición
La suma de todos los valores dividida por el número de observaciones.

### Fórmula
```
μ = (Σ xi) / n
```
Donde:
- μ (mu) = media
- Σ = suma de todos los valores
- xi = cada valor individual
- n = número de valores

### Características
- **Ventajas**: Usa todos los datos, fácil de calcular
- **Desventajas**: Sensible a valores extremos (outliers)
- **Cuándo usar**: Datos simétricos sin valores atípicos

### Ejemplo
Calificaciones: [85, 90, 78, 92, 88]
```
Media = (85 + 90 + 78 + 92 + 88) / 5 = 433 / 5 = 86.6
```

## 2. Mediana

### Definición
El valor que divide los datos ordenados en dos partes iguales (50% arriba, 50% abajo).

### Cálculo
1. Ordenar los datos
2. Si n es impar: valor del medio
3. Si n es par: promedio de los dos valores centrales

### Características
- **Ventajas**: No se ve afectada por valores extremos
- **Desventajas**: No usa toda la información
- **Cuándo usar**: Datos con outliers o asimétricos

### Ejemplo
Datos: [85, 90, 78, 92, 88]
Ordenados: [78, 85, 88, 90, 92]
```
Mediana = 88 (valor central)
```

Con dato adicional: [78, 85, 88, 90, 92, 95]
```
Mediana = (88 + 90) / 2 = 89
```

## 3. Moda

### Definición
El valor que aparece con mayor frecuencia en los datos.

### Tipos
- **Unimodal**: Una sola moda
- **Bimodal**: Dos modas
- **Multimodal**: Más de dos modas
- **Amodal**: Sin moda (todos los valores son únicos)

### Características
- **Ventajas**: Única medida aplicable a datos categóricos
- **Desventajas**: Puede no existir o no ser única
- **Cuándo usar**: Datos categóricos o para identificar valores más comunes

### Ejemplo
Datos: [85, 90, 85, 92, 88, 85, 90]
```
Moda = 85 (aparece 3 veces)
```

## Comparación de Medidas

### Distribución Simétrica
```
Media ≈ Mediana ≈ Moda
    |
    85  90  95
```

### Distribución Asimétrica Positiva (sesgo a derecha)
```
Moda < Mediana < Media
    |     |      |
   80    85     92
```

### Distribución Asimétrica Negativa (sesgo a izquierda)
```
Media < Mediana < Moda
   |      |       |
  78     85      92
```

## Ejemplos Prácticos

### Salarios en una Empresa
```
Datos: [30k, 32k, 35k, 33k, 31k, 200k (CEO)]

Media = 60.2k (distorsionada por el CEO)
Mediana = 33.5k (mejor representación)
Moda = No hay (todos únicos)
```
**Conclusión**: La mediana es más apropiada aquí.

### Tallas de Camisetas Vendidas
```
Datos: [S, M, M, L, M, S, M, L]

Moda = M (la más vendida)
```
**Conclusión**: La moda es la única medida aplicable.

## Implementación

Ver ejemplos de código en:
- [R: examples/R/01_tendencia_central.R](../examples/R/01_tendencia_central.R)
- [Python: examples/Python/01_tendencia_central.py](../examples/Python/01_tendencia_central.py)
- [Java: examples/Java/TendenciaCentral.java](../examples/Java/TendenciaCentral.java)

## Ejercicios

1. Calcula media, mediana y moda de: [12, 15, 18, 12, 20, 25, 12]
2. ¿Qué medida es mejor para datos de ingresos? ¿Por qué?
3. Si todos los valores son únicos, ¿cuál medida no existe?

## Resumen

| Medida | Ventaja Principal | Limitación Principal |
|--------|------------------|---------------------|
| Media | Usa todos los datos | Sensible a outliers |
| Mediana | Robusta a outliers | No usa toda la información |
| Moda | Aplicable a categóricos | Puede no existir o no ser única |

**Regla práctica**: 
- Datos simétricos → Media
- Datos con outliers → Mediana
- Datos categóricos → Moda
