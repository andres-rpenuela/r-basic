"""
============================================
MEDIDAS DE DISPERSIÓN EN PYTHON
============================================
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Configurar estilo de gráficos
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 10)

# ============================================
# 1. CREAR DATOS DE EJEMPLO
# ============================================

# Dos grupos con misma media pero diferente dispersión
np.random.seed(123)
grupo_a = np.array([48, 49, 50, 51, 52])  # Baja dispersión
grupo_b = np.array([10, 30, 50, 70, 90])  # Alta dispersión

print("=" * 60)
print("COMPARACIÓN DE DISPERSIÓN")
print("=" * 60)
print(f"Grupo A - Media: {np.mean(grupo_a):.2f}")
print(f"Grupo B - Media: {np.mean(grupo_b):.2f}")
print("Ambos grupos tienen la misma media, pero diferente dispersión\n")

# ============================================
# 2. RANGO
# ============================================

print("=" * 60)
print("RANGO")
print("=" * 60)

rango_a = np.ptp(grupo_a)  # ptp = peak-to-peak (max - min)
rango_b = np.ptp(grupo_b)

print(f"Rango Grupo A: {rango_a}")
print(f"Rango Grupo B: {rango_b}")

# Calificaciones de ejemplo
calificaciones = np.array([85, 90, 78, 92, 88, 76, 95, 89, 84, 91])
rango_cal = np.ptp(calificaciones)
print(f"\nRango de calificaciones: {rango_cal}")
print(f"Min: {np.min(calificaciones)} | Max: {np.max(calificaciones)}")

# ============================================
# 3. VARIANZA
# ============================================

print("\n" + "=" * 60)
print("VARIANZA")
print("=" * 60)

# Varianza poblacional (ddof=0)
var_pob_a = np.var(grupo_a, ddof=0)
var_pob_b = np.var(grupo_b, ddof=0)

# Varianza muestral (ddof=1) - por defecto en pandas
var_muestra_a = np.var(grupo_a, ddof=1)
var_muestra_b = np.var(grupo_b, ddof=1)

print(f"Varianza Poblacional Grupo A: {var_pob_a:.2f}")
print(f"Varianza Poblacional Grupo B: {var_pob_b:.2f}")
print(f"\nVarianza Muestral Grupo A: {var_muestra_a:.2f}")
print(f"Varianza Muestral Grupo B: {var_muestra_b:.2f}")

# Ejemplo paso a paso
datos_ejemplo = np.array([4, 8, 6, 5, 7])
media_ej = np.mean(datos_ejemplo)
desviaciones = datos_ejemplo - media_ej
desviaciones_cuadrado = desviaciones ** 2

print("\n--- Cálculo Paso a Paso ---")
print(f"Datos: {datos_ejemplo}")
print(f"Media: {media_ej}")
print(f"Desviaciones: {desviaciones}")
print(f"Desviaciones²: {desviaciones_cuadrado}")
print(f"Suma de desviaciones²: {np.sum(desviaciones_cuadrado)}")
print(f"Varianza muestral: {np.var(datos_ejemplo, ddof=1):.2f}")

# ============================================
# 4. DESVIACIÓN ESTÁNDAR
# ============================================

print("\n" + "=" * 60)
print("DESVIACIÓN ESTÁNDAR")
print("=" * 60)

# Desviación estándar
sd_a = np.std(grupo_a, ddof=1)
sd_b = np.std(grupo_b, ddof=1)

print(f"Desviación Estándar Grupo A: {sd_a:.2f}")
print(f"Desviación Estándar Grupo B: {sd_b:.2f}")

# Interpretación con datos normales
np.random.seed(456)
datos_normales = np.random.normal(loc=100, scale=15, size=1000)

media_norm = np.mean(datos_normales)
sd_norm = np.std(datos_normales, ddof=1)

# Regla 68-95-99.7
dentro_1sd = np.sum(np.abs(datos_normales - media_norm) <= sd_norm)
dentro_2sd = np.sum(np.abs(datos_normales - media_norm) <= 2*sd_norm)
dentro_3sd = np.sum(np.abs(datos_normales - media_norm) <= 3*sd_norm)

print("\n--- Regla 68-95-99.7 (datos normales) ---")
print(f"Dentro de ±1 DE: {100*dentro_1sd/1000:.1f}% (esperado ~68%)")
print(f"Dentro de ±2 DE: {100*dentro_2sd/1000:.1f}% (esperado ~95%)")
print(f"Dentro de ±3 DE: {100*dentro_3sd/1000:.1f}% (esperado ~99.7%)")

# ============================================
# 5. COEFICIENTE DE VARIACIÓN
# ============================================

print("\n" + "=" * 60)
print("COEFICIENTE DE VARIACIÓN")
print("=" * 60)

def coef_variacion(x):
    """Calcula el coeficiente de variación"""
    return (np.std(x, ddof=1) / np.mean(x)) * 100

cv_a = coef_variacion(grupo_a)
cv_b = coef_variacion(grupo_b)

print(f"CV Grupo A: {cv_a:.2f}%")
print(f"CV Grupo B: {cv_b:.2f}%")

# Ejemplo práctico: comparar variables en diferentes escalas
alturas_cm = np.array([170, 175, 168, 180, 172])  # en cm
pesos_kg = np.array([70, 75, 68, 80, 72])         # en kg

print("\n--- Comparación de Variables Diferentes ---")
print(f"Alturas - Media: {np.mean(alturas_cm):.2f} cm | DE: {np.std(alturas_cm, ddof=1):.2f} cm")
print(f"         CV: {coef_variacion(alturas_cm):.2f}%")
print(f"Pesos   - Media: {np.mean(pesos_kg):.2f} kg | DE: {np.std(pesos_kg, ddof=1):.2f} kg")
print(f"         CV: {coef_variacion(pesos_kg):.2f}%")

# ============================================
# 6. RANGO INTERCUARTÍLICO (IQR)
# ============================================

print("\n" + "=" * 60)
print("RANGO INTERCUARTÍLICO")
print("=" * 60)

# IQR (Interquartile Range)
q1 = np.percentile(calificaciones, 25)
q3 = np.percentile(calificaciones, 75)
iqr = q3 - q1

print(f"Cuartil 1 (Q1): {q1}")
print(f"Cuartil 3 (Q3): {q3}")
print(f"IQR (Q3 - Q1): {iqr}")

# Usando scipy
iqr_scipy = stats.iqr(calificaciones)
print(f"IQR (scipy): {iqr_scipy}")

# Cuartiles completos
cuartiles = np.percentile(calificaciones, [0, 25, 50, 75, 100])
print(f"\nCuartiles completos:")
print(f"  Mínimo: {cuartiles[0]}")
print(f"  Q1: {cuartiles[1]}")
print(f"  Q2 (Mediana): {cuartiles[2]}")
print(f"  Q3: {cuartiles[3]}")
print(f"  Máximo: {cuartiles[4]}")

# ============================================
# 7. VISUALIZACIONES
# ============================================

print("\n" + "=" * 60)
print("GENERANDO VISUALIZACIONES")
print("=" * 60)

# Crear figura con múltiples subplots
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('Análisis de Dispersión', fontsize=16, fontweight='bold')

# Subplot 1: Boxplot comparativo
datos_grupos = [grupo_a, grupo_b]
axes[0, 0].boxplot(datos_grupos, labels=['Grupo A', 'Grupo B'])
axes[0, 0].set_title('Comparación de Dispersión\n(misma media)')
axes[0, 0].set_ylabel('Valores')
axes[0, 0].grid(True, alpha=0.3, axis='y')

# Subplot 2: Histogramas superpuestos
axes[0, 1].hist(grupo_a, alpha=0.7, label='Grupo A (baja dispersión)', 
                bins=5, color='lightblue', edgecolor='darkblue')
axes[0, 1].hist(grupo_b, alpha=0.7, label='Grupo B (alta dispersión)', 
                bins=5, color='lightcoral', edgecolor='darkred')
axes[0, 1].axvline(np.mean(grupo_a), color='blue', linestyle='--', linewidth=2)
axes[0, 1].axvline(np.mean(grupo_b), color='red', linestyle='--', linewidth=2)
axes[0, 1].set_title('Distribuciones Comparadas')
axes[0, 1].set_xlabel('Valores')
axes[0, 1].set_ylabel('Frecuencia')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)

# Subplot 3: Gráfico de dispersión de puntos
axes[0, 2].scatter(np.ones(len(grupo_a)), grupo_a, s=100, alpha=0.6, 
                   label='Grupo A', color='blue')
axes[0, 2].scatter(np.ones(len(grupo_b))*2, grupo_b, s=100, alpha=0.6, 
                   label='Grupo B', color='red')
axes[0, 2].hlines(np.mean(grupo_a), 0.5, 1.5, colors='blue', linestyles='dashed', linewidth=2)
axes[0, 2].hlines(np.mean(grupo_b), 1.5, 2.5, colors='red', linestyles='dashed', linewidth=2)
axes[0, 2].set_title('Puntos de Datos')
axes[0, 2].set_ylabel('Valores')
axes[0, 2].set_xticks([1, 2])
axes[0, 2].set_xticklabels(['Grupo A', 'Grupo B'])
axes[0, 2].legend()
axes[0, 2].grid(True, alpha=0.3, axis='y')

# Subplot 4: Distribución normal con desviaciones estándar
axes[1, 0].hist(datos_normales, bins=50, color='skyblue', 
                edgecolor='white', alpha=0.7, density=True)
x_range = np.linspace(datos_normales.min(), datos_normales.max(), 100)
axes[1, 0].plot(x_range, stats.norm.pdf(x_range, media_norm, sd_norm), 
                'r-', lw=2, label='Curva normal')
axes[1, 0].axvline(media_norm, color='red', linestyle='-', linewidth=2, label='Media')
axes[1, 0].axvline(media_norm - sd_norm, color='orange', linestyle='--', linewidth=2)
axes[1, 0].axvline(media_norm + sd_norm, color='orange', linestyle='--', linewidth=2, label='±1 DE')
axes[1, 0].axvline(media_norm - 2*sd_norm, color='blue', linestyle=':', linewidth=2)
axes[1, 0].axvline(media_norm + 2*sd_norm, color='blue', linestyle=':', linewidth=2, label='±2 DE')
axes[1, 0].set_title('Distribución Normal con DE')
axes[1, 0].set_xlabel('Valores')
axes[1, 0].set_ylabel('Densidad')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)

# Subplot 5: Violinplot
df_violin = pd.DataFrame({
    'Grupo': ['A']*len(grupo_a) + ['B']*len(grupo_b),
    'Valores': np.concatenate([grupo_a, grupo_b])
})
sns.violinplot(x='Grupo', y='Valores', data=df_violin, ax=axes[1, 1], palette='Set2')
axes[1, 1].set_title('Gráfico de Violín')
axes[1, 1].grid(True, alpha=0.3, axis='y')

# Subplot 6: Comparación de CV
grupos_nombres = ['Grupo A', 'Grupo B', 'Alturas\n(cm)', 'Pesos\n(kg)']
cvs = [cv_a, cv_b, coef_variacion(alturas_cm), coef_variacion(pesos_kg)]
colors = ['lightblue', 'lightcoral', 'lightgreen', 'lightyellow']
axes[1, 2].bar(grupos_nombres, cvs, color=colors, edgecolor='black')
axes[1, 2].set_title('Coeficiente de Variación')
axes[1, 2].set_ylabel('CV (%)')
axes[1, 2].grid(True, alpha=0.3, axis='y')
for i, cv in enumerate(cvs):
    axes[1, 2].text(i, cv + 1, f'{cv:.1f}%', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('/tmp/dispersion_python.png', dpi=150, bbox_inches='tight')
print("Gráfico principal guardado en: /tmp/dispersion_python.png")

# ============================================
# 8. DETECCIÓN DE OUTLIERS CON IQR
# ============================================

print("\n" + "=" * 60)
print("DETECCIÓN DE OUTLIERS")
print("=" * 60)

def detectar_outliers(x):
    """Detecta outliers usando el método IQR"""
    q1 = np.percentile(x, 25)
    q3 = np.percentile(x, 75)
    iqr = q3 - q1
    
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    
    outliers = x[(x < limite_inferior) | (x > limite_superior)]
    
    print(f"Límite inferior: {limite_inferior:.2f}")
    print(f"Límite superior: {limite_superior:.2f}")
    print(f"Outliers encontrados: {len(outliers)}")
    if len(outliers) > 0:
        print(f"Valores: {outliers}")
    
    return outliers, limite_inferior, limite_superior

# Datos con outlier
datos_outlier = np.array([10, 12, 14, 15, 16, 18, 20, 100])
print("Datos con outlier evidente:")
print(datos_outlier)
outliers, lim_inf, lim_sup = detectar_outliers(datos_outlier)

# Visualizar outliers
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.boxplot(datos_outlier)
plt.title('Boxplot mostrando Outliers')
plt.ylabel('Valores')
plt.grid(True, alpha=0.3, axis='y')

plt.subplot(1, 2, 2)
plt.scatter(range(len(datos_outlier)), datos_outlier, s=100, alpha=0.6)
plt.axhline(lim_inf, color='red', linestyle='--', label='Límite inferior')
plt.axhline(lim_sup, color='red', linestyle='--', label='Límite superior')
# Resaltar outliers
outlier_indices = np.where((datos_outlier < lim_inf) | (datos_outlier > lim_sup))[0]
plt.scatter(outlier_indices, datos_outlier[outlier_indices], 
            s=200, color='red', alpha=0.6, label='Outliers')
plt.title('Detección de Outliers')
plt.xlabel('Índice')
plt.ylabel('Valores')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/tmp/outliers_python.png', dpi=150, bbox_inches='tight')
print("\nGráfico de outliers guardado en: /tmp/outliers_python.png")

# ============================================
# 9. RESUMEN DE DISPERSIÓN
# ============================================

print("\n" + "=" * 60)
print("RESUMEN COMPLETO DE DISPERSIÓN")
print("=" * 60)

def resumen_dispersion(x, nombre="Datos"):
    """Calcula y muestra todas las medidas de dispersión"""
    print(f"\n--- {nombre} ---")
    print(f"Rango: {np.ptp(x):.2f}")
    print(f"Varianza: {np.var(x, ddof=1):.2f}")
    print(f"Desviación Estándar: {np.std(x, ddof=1):.2f}")
    print(f"Coeficiente de Variación: {coef_variacion(x):.2f}%")
    print(f"IQR: {stats.iqr(x):.2f}")

resumen_dispersion(calificaciones, "Calificaciones")
resumen_dispersion(grupo_a, "Grupo A (baja dispersión)")
resumen_dispersion(grupo_b, "Grupo B (alta dispersión)")

# ============================================
# 10. EJEMPLO PRÁCTICO: CONTROL DE CALIDAD
# ============================================

print("\n" + "=" * 60)
print("EJEMPLO: CONTROL DE CALIDAD")
print("=" * 60)

# Mediciones de piezas manufacturadas (en mm)
np.random.seed(999)
maquina_a = np.random.normal(10.0, 0.1, 100)
maquina_b = np.random.normal(10.0, 0.5, 100)

print("Máquina A:")
print(f"  Media: {np.mean(maquina_a):.3f} mm")
print(f"  DE: {np.std(maquina_a, ddof=1):.3f} mm")
print(f"  CV: {coef_variacion(maquina_a):.2f}%")

print("\nMáquina B:")
print(f"  Media: {np.mean(maquina_b):.3f} mm")
print(f"  DE: {np.std(maquina_b, ddof=1):.3f} mm")
print(f"  CV: {coef_variacion(maquina_b):.2f}%")

print("\nConclusión: Máquina A tiene mayor precisión (menor variabilidad)")

# Visualizar control de calidad
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(maquina_a, bins=20, alpha=0.7, label='Máquina A', 
         color='lightblue', edgecolor='darkblue')
plt.hist(maquina_b, bins=20, alpha=0.7, label='Máquina B', 
         color='lightcoral', edgecolor='darkred')
plt.axvline(10.0, color='green', linestyle='--', linewidth=2, label='Objetivo')
plt.title('Distribución de Mediciones')
plt.xlabel('Medición (mm)')
plt.ylabel('Frecuencia')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.boxplot([maquina_a, maquina_b], labels=['Máquina A', 'Máquina B'])
plt.axhline(10.0, color='green', linestyle='--', linewidth=2, label='Objetivo')
plt.title('Comparación de Precisión')
plt.ylabel('Medición (mm)')
plt.legend()
plt.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('/tmp/control_calidad.png', dpi=150, bbox_inches='tight')
print("\nGráfico de control de calidad guardado en: /tmp/control_calidad.png")

print("\n" + "=" * 60)
print("FIN DEL SCRIPT")
print("=" * 60)

# plt.show()  # Descomentar para mostrar gráficos en modo interactivo
