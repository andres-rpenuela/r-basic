# ============================================
# MEDIDAS DE DISPERSIÓN EN R
# ============================================

# Cargar librerías
library(ggplot2)

# ============================================
# 1. CREAR DATOS DE EJEMPLO
# ============================================

# Dos grupos con misma media pero diferente dispersión
set.seed(123)
grupo_a <- c(48, 49, 50, 51, 52)  # Baja dispersión
grupo_b <- c(10, 30, 50, 70, 90)  # Alta dispersión

print("=== COMPARACIÓN DE DISPERSIÓN ===")
print(paste("Grupo A - Media:", mean(grupo_a)))
print(paste("Grupo B - Media:", mean(grupo_b)))
print("Ambos grupos tienen la misma media, pero diferente dispersión\n")

# ============================================
# 2. RANGO
# ============================================

calcular_rango <- function(x) {
  return(max(x) - min(x))
}

rango_a <- calcular_rango(grupo_a)
rango_b <- calcular_rango(grupo_b)

print("=== RANGO ===")
print(paste("Rango Grupo A:", rango_a))
print(paste("Rango Grupo B:", rango_b))

# Calificaciones de ejemplo
calificaciones <- c(85, 90, 78, 92, 88, 76, 95, 89, 84, 91)
print(paste("\nRango de calificaciones:", calcular_rango(calificaciones)))
print(paste("Min:", min(calificaciones), "| Max:", max(calificaciones)))

# ============================================
# 3. VARIANZA
# ============================================

print("\n=== VARIANZA ===")

# Varianza poblacional (dividir por n)
varianza_poblacional <- function(x) {
  n <- length(x)
  media <- mean(x)
  return(sum((x - media)^2) / n)
}

# Varianza muestral (dividir por n-1) - función nativa de R
var_muestra_a <- var(grupo_a)
var_muestra_b <- var(grupo_b)

print(paste("Varianza Grupo A:", round(var_muestra_a, 2)))
print(paste("Varianza Grupo B:", round(var_muestra_b, 2)))

# Ejemplo paso a paso
datos_ejemplo <- c(4, 8, 6, 5, 7)
media_ej <- mean(datos_ejemplo)
desviaciones <- datos_ejemplo - media_ej
desviaciones_cuadrado <- desviaciones^2

print("\n--- Cálculo Paso a Paso ---")
print(paste("Datos:", paste(datos_ejemplo, collapse = ", ")))
print(paste("Media:", media_ej))
print(paste("Desviaciones:", paste(round(desviaciones, 2), collapse = ", ")))
print(paste("Desviaciones²:", paste(round(desviaciones_cuadrado, 2), collapse = ", ")))
print(paste("Suma de desviaciones²:", sum(desviaciones_cuadrado)))
print(paste("Varianza muestral:", var(datos_ejemplo)))

# ============================================
# 4. DESVIACIÓN ESTÁNDAR
# ============================================

print("\n=== DESVIACIÓN ESTÁNDAR ===")

# Desviación estándar
sd_a <- sd(grupo_a)
sd_b <- sd(grupo_b)

print(paste("Desviación Estándar Grupo A:", round(sd_a, 2)))
print(paste("Desviación Estándar Grupo B:", round(sd_b, 2)))

# Interpretación con datos normales
set.seed(456)
datos_normales <- rnorm(1000, mean = 100, sd = 15)

media_norm <- mean(datos_normales)
sd_norm <- sd(datos_normales)

# Regla 68-95-99.7
dentro_1sd <- sum(abs(datos_normales - media_norm) <= sd_norm)
dentro_2sd <- sum(abs(datos_normales - media_norm) <= 2*sd_norm)
dentro_3sd <- sum(abs(datos_normales - media_norm) <= 3*sd_norm)

print("\n--- Regla 68-95-99.7 (datos normales) ---")
print(paste("Dentro de ±1 DE:", round(100*dentro_1sd/1000, 1), "% (esperado ~68%)"))
print(paste("Dentro de ±2 DE:", round(100*dentro_2sd/1000, 1), "% (esperado ~95%)"))
print(paste("Dentro de ±3 DE:", round(100*dentro_3sd/1000, 1), "% (esperado ~99.7%)"))

# ============================================
# 5. COEFICIENTE DE VARIACIÓN
# ============================================

print("\n=== COEFICIENTE DE VARIACIÓN ===")

coef_variacion <- function(x) {
  return((sd(x) / mean(x)) * 100)
}

cv_a <- coef_variacion(grupo_a)
cv_b <- coef_variacion(grupo_b)

print(paste("CV Grupo A:", round(cv_a, 2), "%"))
print(paste("CV Grupo B:", round(cv_b, 2), "%"))

# Ejemplo práctico: comparar variables en diferentes escalas
alturas_cm <- c(170, 175, 168, 180, 172)  # en cm
pesos_kg <- c(70, 75, 68, 80, 72)         # en kg

print("\n--- Comparación de Variables Diferentes ---")
print(paste("Alturas - Media:", mean(alturas_cm), "cm | DE:", round(sd(alturas_cm), 2), "cm"))
print(paste("         CV:", round(coef_variacion(alturas_cm), 2), "%"))
print(paste("Pesos   - Media:", mean(pesos_kg), "kg | DE:", round(sd(pesos_kg), 2), "kg"))
print(paste("         CV:", round(coef_variacion(pesos_kg), 2), "%"))

# ============================================
# 6. RANGO INTERCUARTÍLICO (IQR)
# ============================================

print("\n=== RANGO INTERCUARTÍLICO ===")

# IQR (Interquartile Range)
iqr_cal <- IQR(calificaciones)
q1 <- quantile(calificaciones, 0.25)
q3 <- quantile(calificaciones, 0.75)

print(paste("Cuartil 1 (Q1):", q1))
print(paste("Cuartil 3 (Q3):", q3))
print(paste("IQR (Q3 - Q1):", iqr_cal))

# Cuartiles completos
cuartiles <- quantile(calificaciones)
print("\nTodos los cuartiles:")
print(cuartiles)

# ============================================
# 7. VISUALIZACIONES
# ============================================

# Boxplot comparativo
par(mfrow = c(1, 2))

# Boxplot de grupos A y B
boxplot(list(A = grupo_a, B = grupo_b),
        main = "Comparación de Dispersión\n(misma media)",
        ylab = "Valores",
        col = c("lightblue", "lightcoral"))

# Boxplot de calificaciones con IQR
boxplot(calificaciones,
        main = "Calificaciones\n(mostrando IQR)",
        ylab = "Calificación",
        col = "lightgreen")

# Agregar anotaciones
text(1.3, q1, paste("Q1 =", q1), cex = 0.8)
text(1.3, median(calificaciones), paste("Mediana =", median(calificaciones)), cex = 0.8)
text(1.3, q3, paste("Q3 =", q3), cex = 0.8)

# ============================================
# 8. HISTOGRAMAS CON DESVIACIÓN ESTÁNDAR
# ============================================

# Resetear disposición de gráficos
par(mfrow = c(1, 1))

# Generar datos normales
set.seed(789)
datos_hist <- rnorm(500, mean = 50, sd = 10)

# Histograma
hist(datos_hist,
     main = "Distribución Normal\ncon Media ± DE",
     xlab = "Valores",
     ylab = "Frecuencia",
     col = "skyblue",
     border = "white",
     breaks = 30)

# Líneas de media y desviaciones estándar
media_h <- mean(datos_hist)
sd_h <- sd(datos_hist)

abline(v = media_h, col = "red", lwd = 2)
abline(v = c(media_h - sd_h, media_h + sd_h), col = "orange", lwd = 2, lty = 2)
abline(v = c(media_h - 2*sd_h, media_h + 2*sd_h), col = "blue", lwd = 2, lty = 3)

legend("topright",
       legend = c("Media", "±1 DE", "±2 DE"),
       col = c("red", "orange", "blue"),
       lty = c(1, 2, 3),
       lwd = 2)

# ============================================
# 9. COMPARACIÓN VISUAL CON GGPLOT2
# ============================================

# Crear dataframe
datos_comp <- data.frame(
  grupo = rep(c("Baja Dispersión", "Alta Dispersión"), each = 5),
  valor = c(grupo_a, grupo_b)
)

# Gráfico de violín
ggplot(datos_comp, aes(x = grupo, y = valor, fill = grupo)) +
  geom_violin(alpha = 0.7) +
  geom_boxplot(width = 0.2, fill = "white") +
  geom_jitter(width = 0.1, alpha = 0.5) +
  labs(title = "Comparación de Dispersión",
       subtitle = "Misma media (50), diferente variabilidad",
       x = "Grupo",
       y = "Valor") +
  theme_minimal() +
  theme(legend.position = "none")

# ============================================
# 10. RESUMEN ESTADÍSTICO COMPLETO
# ============================================

print("\n=== RESUMEN COMPLETO DE DISPERSIÓN ===")

resumen_dispersion <- function(x, nombre = "Datos") {
  cat(paste("\n---", nombre, "---\n"))
  cat(paste("Rango:", calcular_rango(x), "\n"))
  cat(paste("Varianza:", round(var(x), 2), "\n"))
  cat(paste("Desviación Estándar:", round(sd(x), 2), "\n"))
  cat(paste("Coeficiente de Variación:", round(coef_variacion(x), 2), "%\n"))
  cat(paste("IQR:", round(IQR(x), 2), "\n"))
}

resumen_dispersion(calificaciones, "Calificaciones")
resumen_dispersion(grupo_a, "Grupo A (baja dispersión)")
resumen_dispersion(grupo_b, "Grupo B (alta dispersión)")

# ============================================
# 11. DETECCIÓN DE OUTLIERS CON IQR
# ============================================

print("\n=== DETECCIÓN DE OUTLIERS ===")

detectar_outliers <- function(x) {
  q1 <- quantile(x, 0.25)
  q3 <- quantile(x, 0.75)
  iqr <- q3 - q1
  
  limite_inferior <- q1 - 1.5 * iqr
  limite_superior <- q3 + 1.5 * iqr
  
  outliers <- x[x < limite_inferior | x > limite_superior]
  
  cat(paste("Límite inferior:", limite_inferior, "\n"))
  cat(paste("Límite superior:", limite_superior, "\n"))
  cat(paste("Outliers encontrados:", length(outliers), "\n"))
  if (length(outliers) > 0) {
    cat(paste("Valores:", paste(outliers, collapse = ", "), "\n"))
  }
}

# Datos con outlier
datos_outlier <- c(10, 12, 14, 15, 16, 18, 20, 100)
print("Datos con outlier evidente:")
detectar_outliers(datos_outlier)

# ============================================
# 12. EJEMPLO PRÁCTICO: CONTROL DE CALIDAD
# ============================================

print("\n=== EJEMPLO: CONTROL DE CALIDAD ===")

# Mediciones de piezas manufacturadas (en mm)
maquina_a <- rnorm(100, mean = 10.0, sd = 0.1)
maquina_b <- rnorm(100, mean = 10.0, sd = 0.5)

print("Máquina A:")
print(paste("  Media:", round(mean(maquina_a), 3), "mm"))
print(paste("  DE:", round(sd(maquina_a), 3), "mm"))
print(paste("  CV:", round(coef_variacion(maquina_a), 2), "%"))

print("\nMáquina B:")
print(paste("  Media:", round(mean(maquina_b), 3), "mm"))
print(paste("  DE:", round(sd(maquina_b), 3), "mm"))
print(paste("  CV:", round(coef_variacion(maquina_b), 2), "%"))

print("\nConclusión: Máquina A tiene mayor precisión (menor variabilidad)")

print("\n=== FIN DEL SCRIPT ===")
