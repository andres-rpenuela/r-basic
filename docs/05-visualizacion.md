# Visualización de Datos

La visualización de datos es fundamental en estadística descriptiva para comunicar patrones, tendencias y anomalías de forma clara e intuitiva.

## Principios de Buena Visualización

1. **Claridad**: El mensaje debe ser evidente
2. **Precisión**: No distorsionar los datos
3. **Eficiencia**: Maximizar la información con mínimo esfuerzo visual
4. **Estética**: Atractivo visual sin sacrificar funcionalidad

## 1. Histograma

### ¿Qué es?
Gráfico de barras que muestra la distribución de frecuencias de datos continuos.

### Cuándo usar
- Datos numéricos continuos
- Visualizar la forma de la distribución
- Identificar simetría, asimetría, multimodalidad

### Componentes
- **Eje X**: Intervalos (bins) de valores
- **Eje Y**: Frecuencia o densidad
- **Barras**: Sin espacios entre ellas

### Interpretación
```
Distribución Normal      Asimétrica Derecha    Bimodal
                                                
    |                       |                    |
   | |                     ||                   | |  | |
  |||||                   |||                  |||||||||
 |||||||                 ||||                  |||||||||
|||||||||               |||||                 |||||||||||
```

### Ejemplo en R
```r
# Crear histograma
hist(datos, 
     main="Distribución de Calificaciones",
     xlab="Calificación", 
     ylab="Frecuencia",
     col="steelblue",
     breaks=10)
```

### Ejemplo en Python
```python
import matplotlib.pyplot as plt

plt.hist(datos, bins=10, color='steelblue', edgecolor='black')
plt.xlabel('Calificación')
plt.ylabel('Frecuencia')
plt.title('Distribución de Calificaciones')
plt.show()
```

## 2. Diagrama de Caja (Boxplot)

### ¿Qué es?
Representación gráfica de los cuartiles y valores atípicos.

### Componentes
```
        ○  ← Outlier (valor atípico)
        
        ┬  ← Máximo (sin outliers)
        │
    ┌───┴───┐
    │   │   │  ← Q3 (tercer cuartil)
    │───┼───│  ← Mediana (Q2)
    │   │   │  ← Q1 (primer cuartil)
    └───┬───┘
        │
        ┴  ← Mínimo (sin outliers)
        
        ○  ← Outlier
```

### Cuándo usar
- Comparar distribuciones entre grupos
- Identificar valores atípicos
- Visualizar simetría de datos

### Interpretación
- **Caja**: Contiene el 50% central de los datos (IQR)
- **Línea en la caja**: Mediana
- **Bigotes**: Extienden hasta 1.5×IQR
- **Puntos fuera**: Valores atípicos

### Ejemplo en R
```r
boxplot(datos ~ grupos,
        main="Calificaciones por Grupo",
        xlab="Grupo",
        ylab="Calificación",
        col=c("lightblue", "lightgreen"))
```

### Ejemplo en Python
```python
import seaborn as sns

sns.boxplot(x='grupo', y='calificacion', data=df)
plt.title('Calificaciones por Grupo')
plt.show()
```

## 3. Gráfico de Dispersión (Scatter Plot)

### ¿Qué es?
Muestra la relación entre dos variables numéricas.

### Cuándo usar
- Explorar correlaciones
- Identificar patrones o tendencias
- Detectar outliers bivariados

### Tipos de Relación
```
Positiva           Negativa          Sin Relación
    •                  •              •   •
  •   •              •   •            • •   •
•       •          •       •          •  • •
                                      • •   •
```

### Interpretación
- **Correlación positiva**: A mayor X, mayor Y
- **Correlación negativa**: A mayor X, menor Y
- **Sin correlación**: No hay patrón claro

### Ejemplo en R
```r
plot(x, y,
     main="Relación entre Estudio y Calificación",
     xlab="Horas de Estudio",
     ylab="Calificación",
     pch=19,
     col="darkblue")
abline(lm(y ~ x), col="red", lwd=2)  # Línea de tendencia
```

### Ejemplo en Python
```python
plt.scatter(x, y, color='darkblue', alpha=0.6)
plt.xlabel('Horas de Estudio')
plt.ylabel('Calificación')
plt.title('Relación entre Estudio y Calificación')

# Línea de tendencia
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), "r--")
plt.show()
```

## 4. Gráfico de Barras

### ¿Qué es?
Muestra frecuencias de categorías discretas.

### Cuándo usar
- Datos categóricos
- Comparar frecuencias entre grupos
- Mostrar conteos o proporciones

### Ejemplo en R
```r
barplot(table(categorias),
        main="Distribución de Categorías",
        xlab="Categoría",
        ylab="Frecuencia",
        col=rainbow(length(unique(categorias))))
```

### Ejemplo en Python
```python
df['categoria'].value_counts().plot(kind='bar', color='coral')
plt.xlabel('Categoría')
plt.ylabel('Frecuencia')
plt.title('Distribución de Categorías')
plt.show()
```

## 5. Gráfico de Líneas

### ¿Qué es?
Muestra tendencias a lo largo del tiempo u orden secuencial.

### Cuándo usar
- Series temporales
- Datos ordenados
- Mostrar tendencias

### Ejemplo en R
```r
plot(tiempo, valores,
     type="l",
     main="Evolución Temporal",
     xlab="Tiempo",
     ylab="Valor",
     col="blue",
     lwd=2)
```

## 6. Mapa de Calor (Heatmap)

### ¿Qué es?
Representa valores en una matriz usando colores.

### Cuándo usar
- Matrices de correlación
- Datos multivariados
- Identificar patrones en tablas

### Ejemplo en Python
```python
import seaborn as sns

sns.heatmap(correlation_matrix, 
            annot=True, 
            cmap='coolwarm',
            center=0)
plt.title('Matriz de Correlación')
plt.show()
```

## Guía de Selección de Gráficos

| Tipo de Datos | Objetivo | Gráfico Recomendado |
|---------------|----------|---------------------|
| 1 variable continua | Distribución | Histograma, Densidad |
| 1 variable categórica | Frecuencias | Barras, Pastel |
| 1 continua + 1 categórica | Comparar grupos | Boxplot, Violin |
| 2 variables continuas | Relación | Dispersión |
| Serie temporal | Tendencia | Líneas |
| Múltiples variables | Correlaciones | Heatmap |

## Mejores Prácticas

### ✅ Hacer
- Usar títulos descriptivos
- Etiquetar ejes claramente
- Elegir colores apropiados
- Mantener proporciones adecuadas
- Incluir leyendas cuando sea necesario

### ❌ Evitar
- Gráficos 3D innecesarios
- Demasiados colores
- Escalas distorsionadas
- Exceso de información
- Ejes que no comienzan en cero (en barras)

## Herramientas por Lenguaje

### R
- **Base R**: Gráficos básicos rápidos
- **ggplot2**: Visualizaciones avanzadas y personalizables
- **plotly**: Gráficos interactivos

### Python
- **matplotlib**: Librería base, máximo control
- **seaborn**: Gráficos estadísticos elegantes
- **plotly**: Visualizaciones interactivas

### Java
- **JFreeChart**: Biblioteca completa de gráficos
- **XChart**: Simple y ligera

## Ejemplos Completos

Ver implementaciones en:
- [R: examples/R/03_visualizacion.R](../examples/R/03_visualizacion.R)
- [Python: examples/Python/03_visualizacion.py](../examples/Python/03_visualizacion.py)

## Ejercicios

1. Crea un histograma de 100 números aleatorios normales
2. Genera boxplots comparando tres grupos diferentes
3. Crea un scatter plot mostrando correlación positiva
4. Diseña un gráfico de barras con datos categóricos

## Resumen

La visualización efectiva:
- Facilita la comprensión de patrones
- Revela relaciones entre variables
- Identifica anomalías y outliers
- Comunica resultados de forma clara

**Regla de oro**: El gráfico correcto depende del tipo de datos y el mensaje que quieres transmitir.
