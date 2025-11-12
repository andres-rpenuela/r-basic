# Dataset de Ejemplo: Calificaciones de Estudiantes

Este dataset contiene calificaciones de estudiantes en diferentes materias y puede ser usado para practicar estadística descriptiva.

## Estructura del Dataset

- **estudiante_id**: Identificador único del estudiante
- **nombre**: Nombre del estudiante
- **matematicas**: Calificación en Matemáticas (0-100)
- **ciencias**: Calificación en Ciencias (0-100)
- **literatura**: Calificación en Literatura (0-100)
- **horas_estudio**: Horas de estudio por semana
- **edad**: Edad del estudiante
- **genero**: Género del estudiante (M/F)

## Formato

El archivo `calificaciones.csv` contiene los datos en formato CSV (comma-separated values).

## Uso

### En R:
```r
# Leer el dataset
datos <- read.csv("data/calificaciones.csv")

# Ver las primeras filas
head(datos)

# Calcular estadísticas básicas
summary(datos)

# Media de matemáticas
mean(datos$matematicas)
```

### En Python:
```python
import pandas as pd

# Leer el dataset
datos = pd.read_csv("data/calificaciones.csv")

# Ver las primeras filas
print(datos.head())

# Estadísticas descriptivas
print(datos.describe())

# Media de matemáticas
print(datos['matematicas'].mean())
```

### En Java:
```java
// Leer línea por línea el archivo CSV
// Ver ejemplos en la carpeta Java para implementación completa
```

## Ejercicios Sugeridos

1. Calcular la media, mediana y moda de cada materia
2. Determinar qué materia tiene mayor variabilidad
3. Analizar la correlación entre horas de estudio y calificaciones
4. Identificar outliers en las calificaciones
5. Comparar el rendimiento por género
