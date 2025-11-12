# Medidas de Dispersión

Las medidas de dispersión describen qué tan distribuidos o separados están los datos respecto a su centro.

## ¿Por qué son importantes?

Dos conjuntos de datos pueden tener la misma media pero diferente dispersión:

**Conjunto A**: [48, 49, 50, 51, 52] → Media = 50
**Conjunto B**: [10, 30, 50, 70, 90] → Media = 50

¡Misma media, pero muy diferente variabilidad!

## 1. Rango

### Definición
La diferencia entre el valor máximo y el valor mínimo.

### Fórmula
```
Rango = Máximo - Mínimo
```

### Características
- **Ventajas**: Simple, fácil de calcular
- **Desventajas**: Solo usa dos valores, sensible a outliers
- **Uso**: Primera aproximación a la variabilidad

### Ejemplo
Datos: [45, 52, 48, 60, 55]
```
Rango = 60 - 45 = 15
```

## 2. Varianza

### Definición
Promedio de las desviaciones cuadradas respecto a la media.

### Fórmula Poblacional
```
σ² = Σ(xi - μ)² / N
```

### Fórmula Muestral
```
s² = Σ(xi - x̄)² / (n - 1)
```

Donde:
- σ² (sigma cuadrado) = varianza poblacional
- s² = varianza muestral
- xi = cada valor
- μ o x̄ = media
- N o n = número de valores

### Características
- **Ventajas**: Usa todos los datos
- **Desventajas**: Unidades al cuadrado (difícil de interpretar)
- **Uso**: Base para muchos métodos estadísticos

### Ejemplo
Datos: [4, 8, 6, 5, 7]
Media = 6
```
Desviaciones: [-2, 2, 0, -1, 1]
Desviaciones²: [4, 4, 0, 1, 1]
Varianza = (4+4+0+1+1) / 4 = 2.5
```

## 3. Desviación Estándar

### Definición
La raíz cuadrada de la varianza. Mide la dispersión en las mismas unidades que los datos.

### Fórmula
```
σ = √(varianza)
s = √s²
```

### Características
- **Ventajas**: Mismas unidades que los datos, fácil de interpretar
- **Desventajas**: Sensible a outliers
- **Uso**: La medida de dispersión más común

### Ejemplo
Si varianza = 2.5
```
Desviación estándar = √2.5 ≈ 1.58
```

### Interpretación
Para distribuciones aproximadamente normales:
- **68%** de los datos están dentro de ±1σ de la media
- **95%** de los datos están dentro de ±2σ de la media
- **99.7%** de los datos están dentro de ±3σ de la media

## 4. Coeficiente de Variación (CV)

### Definición
Desviación estándar expresada como porcentaje de la media.

### Fórmula
```
CV = (s / x̄) × 100%
```

### Características
- **Ventajas**: Permite comparar variabilidad entre diferentes escalas
- **Desventajas**: No se puede calcular si la media es cero
- **Uso**: Comparar variabilidad de diferentes variables

### Ejemplo
**Grupo A**: Media = 50, DE = 5
```
CV = (5/50) × 100% = 10%
```

**Grupo B**: Media = 1000, DE = 50
```
CV = (50/1000) × 100% = 5%
```

Aunque el Grupo B tiene mayor desviación estándar, tiene menor variabilidad relativa.

## 5. Rango Intercuartílico (IQR)

### Definición
Diferencia entre el tercer cuartil (Q3) y el primer cuartil (Q1).

### Fórmula
```
IQR = Q3 - Q1
```

### Características
- **Ventajas**: Robusto a outliers
- **Desventajas**: No usa todos los datos
- **Uso**: Datos con valores extremos

### Ejemplo
Datos ordenados: [10, 15, 20, 25, 30, 35, 40, 45, 50]
```
Q1 = 17.5 (25% de los datos)
Q3 = 42.5 (75% de los datos)
IQR = 42.5 - 17.5 = 25
```

## Comparación Visual

```
    Baja Dispersión          Alta Dispersión
    
    xxx                      x
   xxxxx                    x   x
  xxxxxxx                  x     x
   xxxxx                    x   x
    xxx                      x
    
    |                        |
  Media                    Media
```

## Ejemplos Prácticos

### Calificaciones de Dos Grupos
```
Grupo A: [85, 87, 86, 88, 84]
- Media = 86
- DE = 1.58 (calificaciones consistentes)

Grupo B: [70, 90, 80, 95, 75]
- Media = 82
- DE = 10.95 (calificaciones variables)
```

### Control de Calidad
```
Máquina A: produce piezas de 10.0±0.1 cm
Máquina B: produce piezas de 10.0±0.5 cm

Misma media, pero Máquina A tiene mejor precisión.
```

## Implementación

Ver ejemplos de código en:
- [R: examples/R/02_dispersion.R](../examples/R/02_dispersion.R)
- [Python: examples/Python/02_dispersion.py](../examples/Python/02_dispersion.py)
- [Java: examples/Java/Dispersion.java](../examples/Java/Dispersion.java)

## Tabla Resumen

| Medida | Fórmula | Ventaja | Desventaja |
|--------|---------|---------|------------|
| Rango | Max - Min | Simple | Solo 2 valores |
| Varianza | Σ(x-μ)²/n | Usa todos los datos | Unidades² |
| Des. Estándar | √Varianza | Mismas unidades | Sensible a outliers |
| CV | (s/x̄)×100 | Comparación relativa | Requiere media ≠ 0 |
| IQR | Q3 - Q1 | Robusto | No usa todos los datos |

## Ejercicios

1. Calcula rango, varianza y desviación estándar de: [10, 15, 20, 25, 30]
2. ¿Qué medida usar para comparar variabilidad de temperaturas (°C) vs pesos (kg)?
3. Interpreta: Media=100, DE=15. ¿Dónde está el 95% de los datos?

## Reglas Prácticas

- **Datos sin outliers**: Usa desviación estándar
- **Datos con outliers**: Usa IQR
- **Comparar variables diferentes**: Usa coeficiente de variación
- **Primera exploración**: Usa rango
