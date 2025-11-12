# Guía de Inicio Rápido

Esta guía te ayudará a comenzar con el curso de estadística descriptiva.

## 📋 Requisitos Previos

### Para R:
1. Instalar R: https://cran.r-project.org/
2. Instalar RStudio: https://www.rstudio.com/products/rstudio/download/
3. Instalar paquetes necesarios:
```r
install.packages("ggplot2")
install.packages("dplyr")
install.packages("gridExtra")
```

### Para Python:
1. Instalar Python 3.x: https://www.python.org/downloads/
2. Instalar paquetes necesarios:
```bash
pip install numpy pandas matplotlib seaborn scipy
```

### Para Java:
1. Instalar JDK 8 o superior: https://www.oracle.com/java/technologies/downloads/
2. No se requieren librerías adicionales (ejemplos usan Java estándar)

## 🚀 Primeros Pasos

### 1. Leer la Documentación

Comienza leyendo los documentos en orden:

1. [Introducción a la Estadística Descriptiva](docs/01-introduccion.md)
2. [Tipos de Datos y Variables](docs/02-tipos-de-datos.md)
3. [Medidas de Tendencia Central](docs/03-tendencia-central.md)
4. [Medidas de Dispersión](docs/04-dispersion.md)
5. [Visualización de Datos](docs/05-visualizacion.md)

### 2. Ejecutar los Ejemplos

#### R:
```r
# En RStudio, abre y ejecuta:
source("examples/R/01_tendencia_central.R")
source("examples/R/02_dispersion.R")
source("examples/R/03_visualizacion.R")
```

#### Python:
```bash
# En la terminal:
cd examples/Python
python 01_tendencia_central.py
python 02_dispersion.py
python 03_visualizacion.py
```

#### Java:
```bash
# En la terminal:
cd examples/Java
javac TendenciaCentral.java
java TendenciaCentral

javac Dispersion.java
java Dispersion
```

### 3. Practicar con el Dataset

Usa el dataset de ejemplo para practicar:

#### En R:
```r
# Cargar el dataset
datos <- read.csv("data/calificaciones.csv")

# Explorar
head(datos)
summary(datos)

# Calcular estadísticas
mean(datos$matematicas)
median(datos$matematicas)
sd(datos$matematicas)

# Visualizar
hist(datos$matematicas, main="Calificaciones de Matemáticas")
boxplot(matematicas ~ genero, data=datos)
```

#### En Python:
```python
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
datos = pd.read_csv("data/calificaciones.csv")

# Explorar
print(datos.head())
print(datos.describe())

# Calcular estadísticas
print(datos['matematicas'].mean())
print(datos['matematicas'].median())
print(datos['matematicas'].std())

# Visualizar
datos['matematicas'].hist()
plt.show()

datos.boxplot(column='matematicas', by='genero')
plt.show()
```

## 📊 Ejercicios Sugeridos

1. **Análisis Básico:**
   - Calcula la media, mediana y moda de cada materia
   - Determina qué materia tiene mayor variabilidad
   - Identifica outliers en las calificaciones

2. **Comparaciones:**
   - Compara el rendimiento entre géneros
   - Analiza la correlación entre horas de estudio y calificaciones
   - Compara las tres materias

3. **Visualización:**
   - Crea histogramas para cada materia
   - Genera boxplots comparativos
   - Crea scatter plots de horas de estudio vs calificaciones

## 🎓 Ruta de Aprendizaje

### Nivel Principiante:
1. Lee la introducción y los conceptos básicos
2. Ejecuta los ejemplos en tu lenguaje preferido
3. Practica con el dataset de ejemplo
4. Completa los ejercicios básicos

### Nivel Intermedio:
1. Compara las implementaciones en diferentes lenguajes
2. Crea tus propias visualizaciones
3. Analiza datasets más complejos
4. Combina múltiples técnicas

### Nivel Avanzado:
1. Implementa funciones estadísticas personalizadas
2. Crea dashboards interactivos
3. Analiza datasets del mundo real
4. Integra con otras técnicas de análisis de datos

## 💡 Consejos

- **Practica regularmente**: La estadística se aprende haciéndola
- **Visualiza siempre**: Los gráficos revelan patrones ocultos
- **Comprende antes de calcular**: Entiende qué mide cada estadística
- **Interpreta los resultados**: No solo calcules números, entiende qué significan
- **Compara lenguajes**: Ver las diferencias te ayuda a entender mejor

## 🔗 Recursos Adicionales

### R:
- [R for Data Science](https://r4ds.had.co.nz/)
- [ggplot2 Documentation](https://ggplot2.tidyverse.org/)
- [R Graphics Cookbook](https://r-graphics.org/)

### Python:
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)

### Java:
- [Apache Commons Math](https://commons.apache.org/proper/commons-math/)
- [JFreeChart](http://www.jfree.org/jfreechart/)

### Estadística General:
- [Khan Academy - Estadística](https://es.khanacademy.org/math/statistics-probability)
- [Seeing Theory - Visualización de Estadística](https://seeing-theory.brown.edu/)

## ❓ Preguntas Frecuentes

**P: ¿En qué orden debo aprender los lenguajes?**
R: Comienza con el que te sea más familiar. R es excelente para análisis estadístico, Python es versátil para data science, y Java es útil si necesitas integración con sistemas empresariales.

**P: ¿Necesito instalar todo para comenzar?**
R: No, puedes comenzar con un solo lenguaje. Recomendamos Python o R para principiantes.

**P: ¿Los ejemplos funcionan en mi sistema operativo?**
R: Sí, todos los ejemplos son multiplataforma (Windows, Mac, Linux).

**P: ¿Puedo usar estos materiales para enseñar?**
R: Sí, los materiales son de acceso libre. Por favor, da el crédito apropiado.

## 🆘 Obtener Ayuda

Si encuentras problemas:
1. Verifica que todas las dependencias estén instaladas
2. Revisa los mensajes de error cuidadosamente
3. Consulta la documentación de las librerías
4. Abre un issue en el repositorio con detalles del problema

---

¡Feliz aprendizaje! 📚✨
