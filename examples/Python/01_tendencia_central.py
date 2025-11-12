"""
============================================
MEDIDAS DE TENDENCIA CENTRAL EN PYTHON
============================================
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# Configurar estilo de gráficos
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# ============================================
# 1. CREAR DATOS DE EJEMPLO
# ============================================

# Dataset de calificaciones de estudiantes
calificaciones = np.array([85, 90, 78, 92, 88, 76, 95, 89, 84, 91,
                           87, 93, 82, 88, 90, 86, 94, 79, 88, 92])

print("=" * 50)
print("CALIFICACIONES DE ESTUDIANTES")
print("=" * 50)
print(f"Calificaciones: {calificaciones}")
print(f"Total de estudiantes: {len(calificaciones)}")

# ============================================
# 2. MEDIA (PROMEDIO)
# ============================================

print("\n" + "=" * 50)
print("MEDIA (PROMEDIO)")
print("=" * 50)

# Calcular la media
media = np.mean(calificaciones)
print(f"Media: {media:.2f}")

# Media con pandas
df = pd.DataFrame({'calificaciones': calificaciones})
media_pandas = df['calificaciones'].mean()
print(f"Media (usando pandas): {media_pandas:.2f}")

# Media con valores faltantes
calificaciones_na = np.array([85, 90, 78, np.nan, 88, np.nan, 95])
media_na = np.nanmean(calificaciones_na)  # Ignora NaN
print(f"Media (ignorando NaN): {media_na:.2f}")

# ============================================
# 3. MEDIANA
# ============================================

print("\n" + "=" * 50)
print("MEDIANA")
print("=" * 50)

# Calcular la mediana
mediana = np.median(calificaciones)
print(f"Mediana: {mediana}")

# Ejemplo con número par e impar
pares = np.array([10, 20, 30, 40])
impares = np.array([10, 20, 30, 40, 50])
print(f"Mediana (n par): {np.median(pares)}")  # (20+30)/2 = 25
print(f"Mediana (n impar): {np.median(impares)}")  # 30

# ============================================
# 4. MODA
# ============================================

print("\n" + "=" * 50)
print("MODA")
print("=" * 50)

# Calcular la moda con scipy
moda_result = stats.mode(calificaciones, keepdims=True)
moda_valor = moda_result.mode[0]
moda_freq = moda_result.count[0]
print(f"Moda: {moda_valor} | Frecuencia: {moda_freq}")

# Ejemplo con moda clara
datos_moda = np.array([5, 3, 7, 3, 9, 3, 4, 3, 6])
moda_ejemplo = stats.mode(datos_moda, keepdims=True).mode[0]
print(f"Moda de ejemplo: {moda_ejemplo}")

# Moda con pandas (más robusto para multimodal)
serie = pd.Series(calificaciones)
moda_pandas = serie.mode()
print(f"Moda(s) con pandas: {moda_pandas.values}")

# ============================================
# 5. RESUMEN ESTADÍSTICO COMPLETO
# ============================================

print("\n" + "=" * 50)
print("RESUMEN ESTADÍSTICO COMPLETO")
print("=" * 50)

# Con pandas
print(df['calificaciones'].describe())

# Resumen personalizado
print(f"\nCount: {len(calificaciones)}")
print(f"Mean:  {np.mean(calificaciones):.2f}")
print(f"Median: {np.median(calificaciones):.2f}")
print(f"Mode:  {moda_valor}")
print(f"Min:   {np.min(calificaciones)}")
print(f"Max:   {np.max(calificaciones)}")

# ============================================
# 6. VISUALIZACIÓN
# ============================================

print("\n" + "=" * 50)
print("GENERANDO VISUALIZACIONES")
print("=" * 50)

# Crear figura con subplots
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Análisis de Tendencia Central', fontsize=16, fontweight='bold')

# Subplot 1: Histograma con líneas de media y mediana
axes[0, 0].hist(calificaciones, bins=10, color='lightblue', 
                edgecolor='darkblue', alpha=0.7)
axes[0, 0].axvline(media, color='red', linestyle='--', linewidth=2, label=f'Media = {media:.2f}')
axes[0, 0].axvline(mediana, color='green', linestyle='--', linewidth=2, label=f'Mediana = {mediana}')
axes[0, 0].set_xlabel('Calificación')
axes[0, 0].set_ylabel('Frecuencia')
axes[0, 0].set_title('Distribución de Calificaciones')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# Subplot 2: Boxplot
axes[0, 1].boxplot(calificaciones, vert=True)
axes[0, 1].set_ylabel('Calificación')
axes[0, 1].set_title('Diagrama de Caja')
axes[0, 1].grid(True, alpha=0.3)

# Subplot 3: Gráfico de barras de frecuencias
valores_unicos, frecuencias = np.unique(calificaciones, return_counts=True)
axes[1, 0].bar(valores_unicos, frecuencias, color='coral', edgecolor='darkred', alpha=0.7)
axes[1, 0].set_xlabel('Calificación')
axes[1, 0].set_ylabel('Frecuencia')
axes[1, 0].set_title('Frecuencia de Calificaciones')
axes[1, 0].grid(True, alpha=0.3, axis='y')

# Subplot 4: Gráfico de violín con seaborn
sns.violinplot(y=calificaciones, ax=axes[1, 1], color='lightgreen')
axes[1, 1].set_ylabel('Calificación')
axes[1, 1].set_title('Gráfico de Violín')
axes[1, 1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('/tmp/tendencia_central_python.png', dpi=150, bbox_inches='tight')
print("Gráfico guardado en: /tmp/tendencia_central_python.png")

# ============================================
# 7. COMPARACIÓN DE DISTRIBUCIONES
# ============================================

print("\n" + "=" * 50)
print("COMPARACIÓN DE DISTRIBUCIONES")
print("=" * 50)

# Crear tres distribuciones diferentes
np.random.seed(42)
dist_normal = np.random.normal(75, 10, 100)
dist_sesgada = np.random.exponential(10, 100) + 50
dist_uniforme = np.random.uniform(60, 90, 100)

# Calcular estadísticas
distribuciones = {
    'Normal': dist_normal,
    'Sesgada': dist_sesgada,
    'Uniforme': dist_uniforme
}

for nombre, datos in distribuciones.items():
    print(f"\n{nombre}:")
    print(f"  Media: {np.mean(datos):.2f}")
    print(f"  Mediana: {np.median(datos):.2f}")
    print(f"  Moda: {stats.mode(datos, keepdims=True).mode[0]:.2f}")

# Visualizar comparación
plt.figure(figsize=(14, 5))

for i, (nombre, datos) in enumerate(distribuciones.items(), 1):
    plt.subplot(1, 3, i)
    plt.hist(datos, bins=20, color=['lightblue', 'lightcoral', 'lightgreen'][i-1],
             edgecolor='black', alpha=0.7)
    plt.axvline(np.mean(datos), color='red', linestyle='--', 
                linewidth=2, label=f'Media = {np.mean(datos):.1f}')
    plt.axvline(np.median(datos), color='green', linestyle='--', 
                linewidth=2, label=f'Mediana = {np.median(datos):.1f}')
    plt.title(f'Distribución {nombre}')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.legend()
    plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/tmp/comparacion_distribuciones.png', dpi=150, bbox_inches='tight')
print("\nGráfico de comparación guardado en: /tmp/comparacion_distribuciones.png")

# ============================================
# 8. EJEMPLO PRÁCTICO: SALARIOS
# ============================================

print("\n" + "=" * 50)
print("EJEMPLO PRÁCTICO: SALARIOS")
print("=" * 50)

# Salarios en miles de dólares (con outlier: el CEO)
salarios = np.array([35, 42, 38, 45, 40, 43, 37, 41, 39, 44, 250])

print("Salarios (miles de $):", salarios)

media_salario = np.mean(salarios)
mediana_salario = np.median(salarios)

print(f"\nMedia de salarios: ${media_salario:.2f}k")
print(f"Mediana de salarios: ${mediana_salario}k")
print("\nObservación: La media es mayor por el outlier (CEO con $250k)")
print("La mediana ($41k) representa mejor el salario típico")

# Visualizar
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.boxplot(salarios, vert=True)
plt.ylabel('Salarios (miles de $)')
plt.title('Distribución de Salarios\n(note el outlier)')
plt.grid(True, alpha=0.3, axis='y')

plt.subplot(1, 2, 2)
plt.hist(salarios, bins=15, color='lightgreen', edgecolor='darkgreen', alpha=0.7)
plt.axvline(media_salario, color='red', linestyle='--', 
            linewidth=2, label=f'Media = ${media_salario:.1f}k')
plt.axvline(mediana_salario, color='green', linestyle='--', 
            linewidth=2, label=f'Mediana = ${mediana_salario}k')
plt.xlabel('Salarios (miles de $)')
plt.ylabel('Frecuencia')
plt.title('Histograma de Salarios')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/tmp/salarios_ejemplo.png', dpi=150, bbox_inches='tight')
print("Gráfico de salarios guardado en: /tmp/salarios_ejemplo.png")

# ============================================
# 9. MEDIDAS RESISTENTES VS NO RESISTENTES
# ============================================

print("\n" + "=" * 50)
print("RESISTENCIA A OUTLIERS")
print("=" * 50)

datos_originales = np.array([10, 12, 14, 15, 16, 18, 20])
datos_con_outlier = np.array([10, 12, 14, 15, 16, 18, 100])

print("Datos originales:", datos_originales)
print(f"  Media: {np.mean(datos_originales):.2f}")
print(f"  Mediana: {np.median(datos_originales):.2f}")

print("\nDatos con outlier (100 en lugar de 20):", datos_con_outlier)
print(f"  Media: {np.mean(datos_con_outlier):.2f} - ¡Cambió mucho!")
print(f"  Mediana: {np.median(datos_con_outlier):.2f} - Cambió poco")

# ============================================
# 10. FUNCIONES ÚTILES ADICIONALES
# ============================================

print("\n" + "=" * 50)
print("FUNCIONES ADICIONALES")
print("=" * 50)

# Media ponderada
valores = np.array([80, 90, 85])
pesos = np.array([0.3, 0.5, 0.2])
media_ponderada = np.average(valores, weights=pesos)
print(f"Media ponderada: {media_ponderada:.2f}")

# Media geométrica (para tasas de crecimiento)
valores_pos = np.array([2, 4, 8])
media_geometrica = stats.gmean(valores_pos)
print(f"Media geométrica: {media_geometrica:.2f}")

# Media armónica (para velocidades/tasas)
media_armonica = stats.hmean(valores_pos)
print(f"Media armónica: {media_armonica:.2f}")

# Media truncada (elimina extremos)
datos_truncar = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 100])
media_truncada = stats.trim_mean(datos_truncar, proportiontocut=0.1)  # Elimina 10% de cada extremo
print(f"Media truncada (10%): {media_truncada:.2f}")

print("\n" + "=" * 50)
print("FIN DEL SCRIPT")
print("=" * 50)

# Mostrar todos los gráficos
# plt.show()  # Descomentar para mostrar gráficos en modo interactivo
