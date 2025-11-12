# Tipos de Datos y Variables

## Clasificación de Variables

### Variables Cualitativas (Categóricas)

Representan cualidades o características no numéricas.

#### 1. Nominales
Sin orden inherente.
- **Ejemplos**: Color (rojo, azul, verde), Género (masculino, femenino), País

#### 2. Ordinales
Con orden o jerarquía.
- **Ejemplos**: Nivel educativo (primaria, secundaria, universidad), Satisfacción (bajo, medio, alto)

### Variables Cuantitativas (Numéricas)

Representan cantidades medibles.

#### 1. Discretas
Valores contables, números enteros.
- **Ejemplos**: Número de hijos, Cantidad de productos vendidos, Edad en años

#### 2. Continuas
Pueden tomar cualquier valor en un intervalo.
- **Ejemplos**: Altura (1.75m), Peso (68.5kg), Temperatura (23.7°C)

## Escalas de Medición

### Escala Nominal
- Solo clasificación
- No tiene orden
- **Operaciones**: Conteo, moda

### Escala Ordinal
- Clasificación con orden
- Distancia entre valores no es constante
- **Operaciones**: Mediana, percentiles

### Escala de Intervalo
- Orden y distancia constante
- No tiene cero absoluto
- **Ejemplos**: Temperatura en Celsius
- **Operaciones**: Media, desviación estándar

### Escala de Razón
- Orden, distancia constante y cero absoluto
- **Ejemplos**: Altura, peso, ingresos
- **Operaciones**: Todas las estadísticas

## Importancia en el Análisis

El tipo de variable determina:
1. **Qué estadísticas calcular**
   - Variables categóricas: frecuencias, moda
   - Variables numéricas: media, mediana, desviación estándar

2. **Qué gráficos usar**
   - Categóricas: barras, pastel
   - Numéricas: histograma, boxplot, dispersión

3. **Qué métodos estadísticos aplicar**
   - Diferentes pruebas según el tipo de dato

## Ejemplos en Programación

### R
```r
# Variable categórica
colores <- factor(c("rojo", "azul", "verde", "rojo"))

# Variable numérica continua
alturas <- c(1.75, 1.68, 1.82, 1.70)

# Variable numérica discreta
num_hijos <- c(2, 0, 3, 1)
```

### Python
```python
import pandas as pd

# Variable categórica
colores = pd.Categorical(["rojo", "azul", "verde", "rojo"])

# Variable numérica
alturas = [1.75, 1.68, 1.82, 1.70]
num_hijos = [2, 0, 3, 1]
```

### Java
```java
// Variable categórica (enum)
enum Color { ROJO, AZUL, VERDE }

// Variables numéricas
double[] alturas = {1.75, 1.68, 1.82, 1.70};
int[] numHijos = {2, 0, 3, 1};
```

## Conversión de Tipos

A veces es necesario convertir entre tipos:
- **Discretización**: Convertir continua → discreta (ej: edad → grupo etario)
- **Codificación**: Convertir categórica → numérica (ej: bajo=1, medio=2, alto=3)

## Conclusión

Entender los tipos de datos es crucial porque:
- Guía la elección de métodos estadísticos
- Determina las visualizaciones apropiadas
- Afecta la interpretación de resultados
