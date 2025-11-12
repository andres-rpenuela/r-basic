# ============================================
# MEDIDAS DE TENDENCIA CENTRAL EN R
# ============================================

# Cargar librerías necesarias
# install.packages("ggplot2")  # Descomentar si no está instalado
library(ggplot2)

# ============================================
# 1. CREAR DATOS DE EJEMPLO
# ============================================

# Dataset de calificaciones de estudiantes
calificaciones <- c(85, 90, 78, 92, 88, 76, 95, 89, 84, 91, 
                    87, 93, 82, 88, 90, 86, 94, 79, 88, 92)

print("Calificaciones de estudiantes:")
print(calificaciones)
print(paste("Total de estudiantes:", length(calificaciones)))

# ============================================
# 2. MEDIA (PROMEDIO)
# ============================================

# Calcular la media
media <- mean(calificaciones)
print(paste("Media:", round(media, 2)))

# Media con valores faltantes (NA)
calificaciones_na <- c(calificaciones, NA, NA)
media_na <- mean(calificaciones_na, na.rm = TRUE)  # na.rm elimina NA
print(paste("Media (ignorando NA):", round(media_na, 2)))

# ============================================
# 3. MEDIANA
# ============================================

# Calcular la mediana
mediana <- median(calificaciones)
print(paste("Mediana:", mediana))

# Ejemplo con número par e impar de elementos
pares <- c(10, 20, 30, 40)
impares <- c(10, 20, 30, 40, 50)
print(paste("Mediana (n par):", median(pares)))    # (20+30)/2 = 25
print(paste("Mediana (n impar):", median(impares))) # 30

# ============================================
# 4. MODA
# ============================================

# R no tiene función nativa para moda, crear una
calcular_moda <- function(x) {
  tabla <- table(x)
  moda_valor <- names(tabla)[which.max(tabla)]
  moda_freq <- max(tabla)
  return(list(valor = as.numeric(moda_valor), frecuencia = moda_freq))
}

moda_result <- calcular_moda(calificaciones)
print(paste("Moda:", moda_result$valor, "| Frecuencia:", moda_result$frecuencia))

# Ejemplo con moda clara
datos_moda <- c(5, 3, 7, 3, 9, 3, 4, 3, 6)
print(paste("Moda de ejemplo:", calcular_moda(datos_moda)$valor))

# ============================================
# 5. RESUMEN ESTADÍSTICO COMPLETO
# ============================================

print("Resumen estadístico completo:")
print(summary(calificaciones))

# ============================================
# 6. VISUALIZACIÓN
# ============================================

# Histograma con líneas de media y mediana
hist(calificaciones,
     main = "Distribución de Calificaciones\ncon Media y Mediana",
     xlab = "Calificación",
     ylab = "Frecuencia",
     col = "lightblue",
     border = "darkblue",
     breaks = 10)

# Agregar líneas verticales
abline(v = media, col = "red", lwd = 2, lty = 2)
abline(v = mediana, col = "green", lwd = 2, lty = 2)

# Leyenda
legend("topleft", 
       legend = c(paste("Media =", round(media, 2)), 
                  paste("Mediana =", mediana)),
       col = c("red", "green"),
       lty = 2, lwd = 2)

# ============================================
# 7. COMPARACIÓN DE DISTRIBUCIONES
# ============================================

# Crear tres distribuciones diferentes
set.seed(42)  # Para reproducibilidad
dist_normal <- rnorm(100, mean = 75, sd = 10)
dist_sesgada <- rexp(100, rate = 0.1) + 50
dist_uniforme <- runif(100, min = 60, max = 90)

# Crear dataframe para ggplot2
datos_comp <- data.frame(
  valores = c(dist_normal, dist_sesgada, dist_uniforme),
  tipo = rep(c("Normal", "Sesgada", "Uniforme"), each = 100)
)

# Gráfico de densidad con ggplot2
ggplot(datos_comp, aes(x = valores, fill = tipo)) +
  geom_density(alpha = 0.5) +
  geom_vline(data = aggregate(valores ~ tipo, datos_comp, mean),
             aes(xintercept = valores, color = tipo),
             linetype = "dashed", size = 1) +
  labs(title = "Comparación de Distribuciones",
       subtitle = "Líneas punteadas muestran la media de cada distribución",
       x = "Valores",
       y = "Densidad") +
  theme_minimal()

# ============================================
# 8. EJEMPLO PRÁCTICO: SALARIOS
# ============================================

# Salarios en miles de dólares (con un outlier: el CEO)
salarios <- c(35, 42, 38, 45, 40, 43, 37, 41, 39, 44, 250)

print("\n=== ANÁLISIS DE SALARIOS ===")
print("Salarios (miles de $):")
print(salarios)

media_salario <- mean(salarios)
mediana_salario <- median(salarios)

print(paste("Media de salarios: $", round(media_salario, 2), "k"))
print(paste("Mediana de salarios: $", mediana_salario, "k"))
print("\nObservación: La media es mayor por el outlier (CEO con $250k)")
print("La mediana ($41k) representa mejor el salario típico")

# Boxplot para visualizar outlier
boxplot(salarios,
        main = "Distribución de Salarios\n(note el outlier)",
        ylab = "Salarios (miles de $)",
        col = "lightgreen",
        horizontal = FALSE)

# ============================================
# 9. MEDIDAS RESISTENTES VS NO RESISTENTES
# ============================================

datos_originales <- c(10, 12, 14, 15, 16, 18, 20)
datos_con_outlier <- c(10, 12, 14, 15, 16, 18, 100)

print("\n=== RESISTENCIA A OUTLIERS ===")
print("Datos originales:")
print(paste("Media:", mean(datos_originales)))
print(paste("Mediana:", median(datos_originales)))

print("\nDatos con outlier (100 en lugar de 20):")
print(paste("Media:", mean(datos_con_outlier), "- ¡Cambió mucho!"))
print(paste("Mediana:", median(datos_con_outlier), "- Cambió poco"))

# ============================================
# 10. EJERCICIOS PRÁCTICOS
# ============================================

print("\n=== EJERCICIOS ===")

# Ejercicio 1: Temperaturas
temperaturas <- c(22, 24, 23, 25, 22, 26, 24, 23, 22, 25)
print("1. Temperaturas diarias (°C):")
print(paste("   Media:", mean(temperaturas), "°C"))
print(paste("   Mediana:", median(temperaturas), "°C"))
print(paste("   Moda:", calcular_moda(temperaturas)$valor, "°C"))

# Ejercicio 2: Edades
edades <- c(25, 30, 28, 35, 32, 29, 31, 27, 33, 30)
print("\n2. Edades de un grupo:")
print(paste("   Media:", mean(edades), "años"))
print(paste("   Mediana:", median(edades), "años"))

# ============================================
# FUNCIONES ÚTILES ADICIONALES
# ============================================

# Media ponderada
valores <- c(80, 90, 85)
pesos <- c(0.3, 0.5, 0.2)
media_ponderada <- weighted.mean(valores, pesos)
print(paste("\nMedia ponderada:", media_ponderada))

# Media geométrica (para tasas de crecimiento)
valores_pos <- c(2, 4, 8)
media_geometrica <- exp(mean(log(valores_pos)))
print(paste("Media geométrica:", media_geometrica))

# Media armónica (para velocidades/tasas)
media_armonica <- 1 / mean(1 / valores_pos)
print(paste("Media armónica:", media_armonica))

print("\n=== FIN DEL SCRIPT ===")
