# ============================================
# VISUALIZACIÓN DE DATOS EN R
# ============================================

# Cargar librerías
library(ggplot2)
library(gridExtra)  # Para múltiples gráficos
# install.packages("gridExtra")  # Descomentar si necesario

# ============================================
# 1. PREPARAR DATOS
# ============================================

set.seed(42)

# Generar diferentes tipos de datos
datos_normales <- rnorm(200, mean = 75, sd = 10)
datos_sesgados <- rexp(200, rate = 0.05) + 40
datos_bimodal <- c(rnorm(100, mean = 60, sd = 5), rnorm(100, mean = 85, sd = 5))

# Datos para scatter plot
horas_estudio <- runif(50, min = 1, max = 10)
calificaciones <- 40 + 5 * horas_estudio + rnorm(50, mean = 0, sd = 5)
calificaciones <- pmin(calificaciones, 100)  # Limitar a 100

# Datos categóricos
categorias <- sample(c("A", "B", "C", "D"), 100, replace = TRUE, 
                     prob = c(0.3, 0.25, 0.25, 0.2))

# ============================================
# 2. HISTOGRAMAS
# ============================================

print("=== CREANDO HISTOGRAMAS ===")

# Histograma básico
par(mfrow = c(2, 2))

hist(datos_normales,
     main = "Distribución Normal",
     xlab = "Valores",
     ylab = "Frecuencia",
     col = "lightblue",
     border = "darkblue",
     breaks = 20)

hist(datos_sesgados,
     main = "Distribución Sesgada",
     xlab = "Valores",
     ylab = "Frecuencia",
     col = "lightcoral",
     border = "darkred",
     breaks = 20)

hist(datos_bimodal,
     main = "Distribución Bimodal",
     xlab = "Valores",
     ylab = "Frecuencia",
     col = "lightgreen",
     border = "darkgreen",
     breaks = 20)

# Histograma con densidad
hist(datos_normales,
     main = "Histograma con Curva de Densidad",
     xlab = "Valores",
     ylab = "Densidad",
     col = "lightyellow",
     border = "orange",
     probability = TRUE,
     breaks = 20)
lines(density(datos_normales), col = "red", lwd = 2)

# ============================================
# 3. HISTOGRAMAS CON GGPLOT2
# ============================================

par(mfrow = c(1, 1))

# Crear dataframe
df_hist <- data.frame(
  valores = c(datos_normales, datos_sesgados, datos_bimodal),
  tipo = rep(c("Normal", "Sesgada", "Bimodal"), each = 200)
)

# Histogramas facetados
p1 <- ggplot(df_hist, aes(x = valores, fill = tipo)) +
  geom_histogram(bins = 25, color = "white", alpha = 0.7) +
  facet_wrap(~tipo, scales = "free") +
  labs(title = "Comparación de Distribuciones",
       x = "Valores",
       y = "Frecuencia") +
  theme_minimal() +
  theme(legend.position = "none")

print(p1)

# ============================================
# 4. BOXPLOTS (DIAGRAMAS DE CAJA)
# ============================================

print("\n=== CREANDO BOXPLOTS ===")

# Boxplot básico
par(mfrow = c(1, 2))

boxplot(datos_normales,
        main = "Boxplot Simple",
        ylab = "Valores",
        col = "lightblue",
        border = "darkblue",
        notch = FALSE)

# Agregar puntos de datos
stripchart(datos_normales, 
           vertical = TRUE, 
           method = "jitter",
           add = TRUE, 
           pch = 20, 
           col = rgb(0, 0, 1, 0.2))

# Boxplot comparativo
datos_grupos <- list(
  Normal = datos_normales,
  Sesgada = datos_sesgados,
  Bimodal = datos_bimodal
)

boxplot(datos_grupos,
        main = "Comparación de Distribuciones",
        ylab = "Valores",
        col = c("lightblue", "lightcoral", "lightgreen"),
        border = c("darkblue", "darkred", "darkgreen"),
        las = 1)

# ============================================
# 5. BOXPLOTS CON GGPLOT2
# ============================================

par(mfrow = c(1, 1))

p2 <- ggplot(df_hist, aes(x = tipo, y = valores, fill = tipo)) +
  geom_boxplot(alpha = 0.7, outlier.color = "red", outlier.size = 2) +
  geom_jitter(width = 0.2, alpha = 0.1) +
  labs(title = "Boxplots con Puntos de Datos",
       x = "Tipo de Distribución",
       y = "Valores") +
  theme_minimal() +
  theme(legend.position = "none") +
  scale_fill_brewer(palette = "Set2")

print(p2)

# ============================================
# 6. GRÁFICOS DE DISPERSIÓN (SCATTER PLOTS)
# ============================================

print("\n=== CREANDO SCATTER PLOTS ===")

# Scatter plot básico
par(mfrow = c(1, 2))

plot(horas_estudio, calificaciones,
     main = "Relación: Estudio vs Calificación",
     xlab = "Horas de Estudio",
     ylab = "Calificación",
     pch = 19,
     col = rgb(0, 0, 1, 0.5),
     cex = 1.5)

# Agregar línea de tendencia
modelo <- lm(calificaciones ~ horas_estudio)
abline(modelo, col = "red", lwd = 2)

# Agregar grid
grid()

# Correlación
correlacion <- cor(horas_estudio, calificaciones)
text(2, 95, paste("r =", round(correlacion, 3)), cex = 1.2)

# Scatter plot con categorías de tamaño
plot(horas_estudio, calificaciones,
     main = "Con Categorías de Rendimiento",
     xlab = "Horas de Estudio",
     ylab = "Calificación",
     pch = 21,
     bg = ifelse(calificaciones >= 80, "green", 
                 ifelse(calificaciones >= 60, "yellow", "red")),
     cex = 1.5)

legend("bottomright",
       legend = c("Alto (≥80)", "Medio (60-79)", "Bajo (<60)"),
       pch = 21,
       pt.bg = c("green", "yellow", "red"),
       cex = 0.8)

# ============================================
# 7. SCATTER PLOT CON GGPLOT2
# ============================================

par(mfrow = c(1, 1))

df_scatter <- data.frame(
  horas = horas_estudio,
  notas = calificaciones
)

p3 <- ggplot(df_scatter, aes(x = horas, y = notas)) +
  geom_point(alpha = 0.6, size = 3, color = "steelblue") +
  geom_smooth(method = "lm", color = "red", se = TRUE, fill = "pink") +
  labs(title = "Relación entre Horas de Estudio y Calificación",
       subtitle = paste("Correlación:", round(correlacion, 3)),
       x = "Horas de Estudio",
       y = "Calificación") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5),
        plot.subtitle = element_text(hjust = 0.5))

print(p3)

# ============================================
# 8. GRÁFICOS DE BARRAS
# ============================================

print("\n=== CREANDO GRÁFICOS DE BARRAS ===")

# Contar frecuencias
tabla_categorias <- table(categorias)

# Gráfico de barras básico
par(mfrow = c(2, 2))

barplot(tabla_categorias,
        main = "Distribución de Categorías",
        xlab = "Categoría",
        ylab = "Frecuencia",
        col = rainbow(length(tabla_categorias)),
        border = "white")

# Gráfico de barras horizontal
barplot(tabla_categorias,
        main = "Barras Horizontales",
        xlab = "Frecuencia",
        ylab = "Categoría",
        col = heat.colors(length(tabla_categorias)),
        border = "white",
        horiz = TRUE)

# Gráfico de barras con porcentajes
porcentajes <- prop.table(tabla_categorias) * 100
barplot(porcentajes,
        main = "Distribución en Porcentaje",
        xlab = "Categoría",
        ylab = "Porcentaje (%)",
        col = terrain.colors(length(porcentajes)),
        border = "white",
        ylim = c(0, max(porcentajes) * 1.2))

# Agregar etiquetas de porcentaje
text(x = seq_along(porcentajes) * 1.2 - 0.5,
     y = porcentajes + 2,
     labels = paste0(round(porcentajes, 1), "%"),
     cex = 0.8)

# Gráfico de pastel
pie(tabla_categorias,
    main = "Gráfico de Pastel",
    col = rainbow(length(tabla_categorias)),
    labels = paste(names(tabla_categorias), "\n", tabla_categorias, 
                   " (", round(porcentajes, 1), "%)", sep = ""))

# ============================================
# 9. GRÁFICOS DE BARRAS CON GGPLOT2
# ============================================

par(mfrow = c(1, 1))

df_barras <- data.frame(categoria = categorias)

p4 <- ggplot(df_barras, aes(x = categoria, fill = categoria)) +
  geom_bar() +
  geom_text(stat = 'count', aes(label = after_stat(count)), vjust = -0.5) +
  labs(title = "Distribución de Categorías",
       x = "Categoría",
       y = "Frecuencia") +
  theme_minimal() +
  scale_fill_brewer(palette = "Set3") +
  theme(legend.position = "none")

print(p4)

# ============================================
# 10. GRÁFICOS DE LÍNEAS (SERIES TEMPORALES)
# ============================================

print("\n=== CREANDO GRÁFICOS DE LÍNEAS ===")

# Simular serie temporal
tiempo <- 1:100
tendencia <- 50 + 0.3 * tiempo
estacionalidad <- 10 * sin(tiempo / 5)
ruido <- rnorm(100, mean = 0, sd = 3)
serie_temporal <- tendencia + estacionalidad + ruido

par(mfrow = c(1, 1))

plot(tiempo, serie_temporal,
     type = "l",
     main = "Serie Temporal con Tendencia",
     xlab = "Tiempo",
     ylab = "Valor",
     col = "blue",
     lwd = 2)

# Agregar línea de tendencia
lines(tiempo, tendencia, col = "red", lwd = 2, lty = 2)

# Agregar puntos
points(tiempo, serie_temporal, pch = 20, col = rgb(0, 0, 1, 0.3))

legend("topleft",
       legend = c("Datos observados", "Tendencia"),
       col = c("blue", "red"),
       lty = c(1, 2),
       lwd = 2)

grid()

# ============================================
# 11. GRÁFICOS DE DENSIDAD
# ============================================

print("\n=== CREANDO GRÁFICOS DE DENSIDAD ===")

par(mfrow = c(1, 1))

# Gráfico de densidad con ggplot2
p5 <- ggplot(df_hist, aes(x = valores, fill = tipo)) +
  geom_density(alpha = 0.5) +
  geom_vline(data = aggregate(valores ~ tipo, df_hist, mean),
             aes(xintercept = valores, color = tipo),
             linetype = "dashed", size = 1) +
  labs(title = "Curvas de Densidad Comparativas",
       subtitle = "Líneas verticales muestran la media",
       x = "Valores",
       y = "Densidad") +
  theme_minimal() +
  scale_fill_brewer(palette = "Set1")

print(p5)

# ============================================
# 12. GRÁFICOS COMBINADOS (PANEL)
# ============================================

print("\n=== CREANDO PANEL DE GRÁFICOS ===")

# Crear múltiples gráficos con ggplot2
p_panel1 <- ggplot(df_hist, aes(x = valores, fill = tipo)) +
  geom_histogram(bins = 20, alpha = 0.7) +
  facet_wrap(~tipo, scales = "free") +
  theme_minimal() +
  theme(legend.position = "none")

p_panel2 <- ggplot(df_hist, aes(x = tipo, y = valores, fill = tipo)) +
  geom_violin(alpha = 0.7) +
  theme_minimal() +
  theme(legend.position = "none")

p_panel3 <- ggplot(df_scatter, aes(x = horas, y = notas)) +
  geom_point(color = "steelblue", alpha = 0.6) +
  geom_smooth(method = "lm", color = "red") +
  theme_minimal()

p_panel4 <- ggplot(df_barras, aes(x = categoria, fill = categoria)) +
  geom_bar() +
  theme_minimal() +
  theme(legend.position = "none")

# Combinar en grid
grid.arrange(p_panel1, p_panel2, p_panel3, p_panel4, ncol = 2)

# ============================================
# 13. MATRIZ DE CORRELACIÓN (HEATMAP)
# ============================================

print("\n=== CREANDO HEATMAP DE CORRELACIÓN ===")

# Crear datos multivariados
set.seed(999)
n <- 100
datos_multi <- data.frame(
  var1 = rnorm(n),
  var2 = rnorm(n),
  var3 = rnorm(n),
  var4 = rnorm(n)
)

# Agregar correlaciones
datos_multi$var2 <- datos_multi$var1 * 0.8 + rnorm(n, sd = 0.4)
datos_multi$var3 <- -datos_multi$var1 * 0.6 + rnorm(n, sd = 0.5)

# Calcular matriz de correlación
matriz_cor <- cor(datos_multi)

# Heatmap básico
library(reshape2)
matriz_cor_melted <- melt(matriz_cor)

p6 <- ggplot(matriz_cor_melted, aes(Var1, Var2, fill = value)) +
  geom_tile(color = "white") +
  geom_text(aes(label = round(value, 2)), color = "black") +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", 
                       midpoint = 0, limit = c(-1, 1)) +
  labs(title = "Matriz de Correlación",
       x = "",
       y = "",
       fill = "Correlación") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

print(p6)

print("\n=== FIN DEL SCRIPT ===")
print("Todos los gráficos han sido generados exitosamente")
