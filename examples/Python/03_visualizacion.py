"""
============================================
VISUALIZACIÓN DE DATOS EN PYTHON
============================================
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Configurar estilo
sns.set_style("whitegrid")
sns.set_palette("husl")

print("=" * 60)
print("VISUALIZACIÓN DE DATOS EN PYTHON")
print("=" * 60)

# ============================================
# 1. PREPARAR DATOS
# ============================================

np.random.seed(42)

# Diferentes tipos de datos
datos_normales = np.random.normal(75, 10, 200)
datos_sesgados = np.random.exponential(10, 200) + 40
datos_bimodal = np.concatenate([
    np.random.normal(60, 5, 100),
    np.random.normal(85, 5, 100)
])

# Datos para scatter plot
horas_estudio = np.random.uniform(1, 10, 50)
calificaciones = 40 + 5 * horas_estudio + np.random.normal(0, 5, 50)
calificaciones = np.clip(calificaciones, 0, 100)

# Datos categóricos
categorias = np.random.choice(['A', 'B', 'C', 'D'], size=100, 
                              p=[0.3, 0.25, 0.25, 0.2])

print("Datos generados exitosamente")

# ============================================
# 2. HISTOGRAMAS
# ============================================

print("\n" + "=" * 60)
print("CREANDO HISTOGRAMAS")
print("=" * 60)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Análisis con Histogramas', fontsize=16, fontweight='bold')

# Histograma 1: Normal
axes[0, 0].hist(datos_normales, bins=25, color='lightblue', edgecolor='darkblue', alpha=0.7)
axes[0, 0].axvline(np.mean(datos_normales), color='red', linestyle='--', 
                   linewidth=2, label=f'Media = {np.mean(datos_normales):.1f}')
axes[0, 0].set_title('Distribución Normal')
axes[0, 0].set_xlabel('Valores')
axes[0, 0].set_ylabel('Frecuencia')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# Histograma 2: Sesgada
axes[0, 1].hist(datos_sesgados, bins=25, color='lightcoral', edgecolor='darkred', alpha=0.7)
axes[0, 1].axvline(np.mean(datos_sesgados), color='red', linestyle='--', linewidth=2)
axes[0, 1].axvline(np.median(datos_sesgados), color='green', linestyle='--', linewidth=2)
axes[0, 1].set_title('Distribución Sesgada')
axes[0, 1].set_xlabel('Valores')
axes[0, 1].set_ylabel('Frecuencia')
axes[0, 1].grid(True, alpha=0.3)

# Histograma 3: Bimodal
axes[1, 0].hist(datos_bimodal, bins=25, color='lightgreen', edgecolor='darkgreen', alpha=0.7)
axes[1, 0].set_title('Distribución Bimodal')
axes[1, 0].set_xlabel('Valores')
axes[1, 0].set_ylabel('Frecuencia')
axes[1, 0].grid(True, alpha=0.3)

# Histograma 4: Con densidad
axes[1, 1].hist(datos_normales, bins=30, density=True, color='lightyellow', 
                edgecolor='orange', alpha=0.7, label='Histograma')
# Agregar curva de densidad
from scipy.stats import gaussian_kde
density = gaussian_kde(datos_normales)
xs = np.linspace(datos_normales.min(), datos_normales.max(), 200)
axes[1, 1].plot(xs, density(xs), 'r-', linewidth=2, label='Densidad')
axes[1, 1].set_title('Histograma con Curva de Densidad')
axes[1, 1].set_xlabel('Valores')
axes[1, 1].set_ylabel('Densidad')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/tmp/histogramas_python.png', dpi=150, bbox_inches='tight')
print("Histogramas guardados en: /tmp/histogramas_python.png")

# ============================================
# 3. BOXPLOTS (DIAGRAMAS DE CAJA)
# ============================================

print("\n" + "=" * 60)
print("CREANDO BOXPLOTS")
print("=" * 60)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Boxplot simple
axes[0].boxplot(datos_normales, vert=True)
axes[0].set_ylabel('Valores')
axes[0].set_title('Boxplot Simple')
axes[0].grid(True, alpha=0.3, axis='y')

# Boxplot comparativo
datos_comp = [datos_normales, datos_sesgados, datos_bimodal]
bp = axes[1].boxplot(datos_comp, labels=['Normal', 'Sesgada', 'Bimodal'],
                     patch_artist=True)
# Colorear cajas
colors = ['lightblue', 'lightcoral', 'lightgreen']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
axes[1].set_ylabel('Valores')
axes[1].set_title('Comparación de Distribuciones')
axes[1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('/tmp/boxplots_python.png', dpi=150, bbox_inches='tight')
print("Boxplots guardados en: /tmp/boxplots_python.png")

# ============================================
# 4. BOXPLOTS CON SEABORN
# ============================================

# Crear DataFrame
df_dist = pd.DataFrame({
    'valores': np.concatenate([datos_normales, datos_sesgados, datos_bimodal]),
    'tipo': ['Normal']*200 + ['Sesgada']*200 + ['Bimodal']*200
})

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.boxplot(x='tipo', y='valores', data=df_dist, palette='Set2')
plt.title('Boxplot con Seaborn')
plt.ylabel('Valores')
plt.xlabel('Tipo de Distribución')
plt.grid(True, alpha=0.3, axis='y')

plt.subplot(1, 2, 2)
sns.violinplot(x='tipo', y='valores', data=df_dist, palette='Set2')
plt.title('Violin Plot')
plt.ylabel('Valores')
plt.xlabel('Tipo de Distribución')
plt.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('/tmp/seaborn_boxplots.png', dpi=150, bbox_inches='tight')
print("Boxplots seaborn guardados en: /tmp/seaborn_boxplots.png")

# ============================================
# 5. GRÁFICOS DE DISPERSIÓN
# ============================================

print("\n" + "=" * 60)
print("CREANDO SCATTER PLOTS")
print("=" * 60)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Scatter plot básico
axes[0].scatter(horas_estudio, calificaciones, s=80, alpha=0.6, color='steelblue')
# Línea de tendencia
z = np.polyfit(horas_estudio, calificaciones, 1)
p = np.poly1d(z)
axes[0].plot(horas_estudio, p(horas_estudio), "r--", linewidth=2, label='Tendencia')
axes[0].set_xlabel('Horas de Estudio')
axes[0].set_ylabel('Calificación')
axes[0].set_title('Relación: Estudio vs Calificación')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Calcular correlación
correlacion = np.corrcoef(horas_estudio, calificaciones)[0, 1]
axes[0].text(2, 95, f'r = {correlacion:.3f}', fontsize=12, 
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Scatter plot con categorías
categorias_rend = pd.cut(calificaciones, bins=[0, 60, 80, 100], 
                         labels=['Bajo', 'Medio', 'Alto'])
colors_rend = {'Bajo': 'red', 'Medio': 'yellow', 'Alto': 'green'}

for cat in ['Bajo', 'Medio', 'Alto']:
    mask = categorias_rend == cat
    axes[1].scatter(horas_estudio[mask], calificaciones[mask], 
                   s=80, alpha=0.6, color=colors_rend[cat], label=cat)

axes[1].set_xlabel('Horas de Estudio')
axes[1].set_ylabel('Calificación')
axes[1].set_title('Con Categorías de Rendimiento')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/tmp/scatter_plots.png', dpi=150, bbox_inches='tight')
print("Scatter plots guardados en: /tmp/scatter_plots.png")

# ============================================
# 6. SCATTER PLOT CON SEABORN
# ============================================

df_scatter = pd.DataFrame({
    'Horas de Estudio': horas_estudio,
    'Calificación': calificaciones
})

plt.figure(figsize=(10, 6))
sns.regplot(x='Horas de Estudio', y='Calificación', data=df_scatter,
            scatter_kws={'s': 80, 'alpha': 0.6}, color='steelblue')
plt.title(f'Relación entre Estudio y Calificación (r = {correlacion:.3f})')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('/tmp/seaborn_scatter.png', dpi=150, bbox_inches='tight')
print("Scatter seaborn guardado en: /tmp/seaborn_scatter.png")

# ============================================
# 7. GRÁFICOS DE BARRAS
# ============================================

print("\n" + "=" * 60)
print("CREANDO GRÁFICOS DE BARRAS")
print("=" * 60)

# Contar frecuencias
valores_unicos, conteos = np.unique(categorias, return_counts=True)
porcentajes = (conteos / len(categorias)) * 100

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Barras verticales
axes[0, 0].bar(valores_unicos, conteos, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A'],
               edgecolor='black', alpha=0.7)
axes[0, 0].set_xlabel('Categoría')
axes[0, 0].set_ylabel('Frecuencia')
axes[0, 0].set_title('Distribución de Categorías')
axes[0, 0].grid(True, alpha=0.3, axis='y')

# Barras horizontales
axes[0, 1].barh(valores_unicos, conteos, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A'],
                edgecolor='black', alpha=0.7)
axes[0, 1].set_ylabel('Categoría')
axes[0, 1].set_xlabel('Frecuencia')
axes[0, 1].set_title('Barras Horizontales')
axes[0, 1].grid(True, alpha=0.3, axis='x')

# Barras con porcentajes
bars = axes[1, 0].bar(valores_unicos, porcentajes, 
                      color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A'],
                      edgecolor='black', alpha=0.7)
axes[1, 0].set_xlabel('Categoría')
axes[1, 0].set_ylabel('Porcentaje (%)')
axes[1, 0].set_title('Distribución en Porcentaje')
axes[1, 0].grid(True, alpha=0.3, axis='y')

# Agregar etiquetas
for bar, pct in zip(bars, porcentajes):
    height = bar.get_height()
    axes[1, 0].text(bar.get_x() + bar.get_width()/2., height + 1,
                    f'{pct:.1f}%', ha='center', va='bottom', fontweight='bold')

# Gráfico de pastel
axes[1, 1].pie(conteos, labels=valores_unicos, autopct='%1.1f%%',
               colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A'],
               startangle=90, explode=[0.05]*len(valores_unicos))
axes[1, 1].set_title('Gráfico de Pastel')

plt.tight_layout()
plt.savefig('/tmp/graficos_barras.png', dpi=150, bbox_inches='tight')
print("Gráficos de barras guardados en: /tmp/graficos_barras.png")

# ============================================
# 8. GRÁFICOS DE LÍNEAS (SERIES TEMPORALES)
# ============================================

print("\n" + "=" * 60)
print("CREANDO GRÁFICOS DE LÍNEAS")
print("=" * 60)

# Simular serie temporal
tiempo = np.arange(1, 101)
tendencia = 50 + 0.3 * tiempo
estacionalidad = 10 * np.sin(tiempo / 5)
ruido = np.random.normal(0, 3, 100)
serie_temporal = tendencia + estacionalidad + ruido

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(tiempo, serie_temporal, 'b-', linewidth=2, label='Datos observados', alpha=0.7)
plt.plot(tiempo, tendencia, 'r--', linewidth=2, label='Tendencia')
plt.scatter(tiempo, serie_temporal, s=20, alpha=0.3, color='blue')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.title('Serie Temporal con Tendencia')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.plot(tiempo, estacionalidad, 'g-', linewidth=2, label='Componente estacional')
plt.plot(tiempo, ruido, 'orange', alpha=0.5, label='Ruido')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.title('Componentes de la Serie')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/tmp/series_temporales.png', dpi=150, bbox_inches='tight')
print("Series temporales guardadas en: /tmp/series_temporales.png")

# ============================================
# 9. HEATMAP (MATRIZ DE CORRELACIÓN)
# ============================================

print("\n" + "=" * 60)
print("CREANDO HEATMAP DE CORRELACIÓN")
print("=" * 60)

# Crear datos multivariados con correlaciones
np.random.seed(999)
n = 100
var1 = np.random.randn(n)
var2 = var1 * 0.8 + np.random.randn(n) * 0.4
var3 = -var1 * 0.6 + np.random.randn(n) * 0.5
var4 = np.random.randn(n)

df_multi = pd.DataFrame({
    'Variable 1': var1,
    'Variable 2': var2,
    'Variable 3': var3,
    'Variable 4': var4
})

# Calcular matriz de correlación
matriz_cor = df_multi.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(matriz_cor, annot=True, fmt='.2f', cmap='coolwarm', 
            center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('Matriz de Correlación', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('/tmp/heatmap_correlacion.png', dpi=150, bbox_inches='tight')
print("Heatmap guardado en: /tmp/heatmap_correlacion.png")

# ============================================
# 10. PANEL COMBINADO
# ============================================

print("\n" + "=" * 60)
print("CREANDO PANEL COMBINADO")
print("=" * 60)

fig = plt.figure(figsize=(16, 12))
gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

# Histograma
ax1 = fig.add_subplot(gs[0, :2])
ax1.hist(datos_normales, bins=30, color='lightblue', edgecolor='darkblue', alpha=0.7)
ax1.set_title('Histograma', fontweight='bold')
ax1.set_xlabel('Valores')
ax1.set_ylabel('Frecuencia')
ax1.grid(True, alpha=0.3)

# Boxplot
ax2 = fig.add_subplot(gs[0, 2])
ax2.boxplot([datos_normales, datos_sesgados], labels=['Normal', 'Sesgada'])
ax2.set_title('Boxplots', fontweight='bold')
ax2.grid(True, alpha=0.3, axis='y')

# Scatter
ax3 = fig.add_subplot(gs[1, :2])
ax3.scatter(horas_estudio, calificaciones, s=60, alpha=0.6, color='steelblue')
ax3.plot(horas_estudio, p(horas_estudio), 'r--', linewidth=2)
ax3.set_title('Scatter Plot', fontweight='bold')
ax3.set_xlabel('Horas de Estudio')
ax3.set_ylabel('Calificación')
ax3.grid(True, alpha=0.3)

# Barras
ax4 = fig.add_subplot(gs[1, 2])
ax4.bar(valores_unicos, conteos, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A'], alpha=0.7)
ax4.set_title('Gráfico de Barras', fontweight='bold')
ax4.grid(True, alpha=0.3, axis='y')

# Serie temporal
ax5 = fig.add_subplot(gs[2, :])
ax5.plot(tiempo, serie_temporal, 'b-', linewidth=2, alpha=0.7)
ax5.plot(tiempo, tendencia, 'r--', linewidth=2)
ax5.set_title('Serie Temporal', fontweight='bold')
ax5.set_xlabel('Tiempo')
ax5.set_ylabel('Valor')
ax5.grid(True, alpha=0.3)

fig.suptitle('Panel Integrado de Visualizaciones', fontsize=16, fontweight='bold')
plt.savefig('/tmp/panel_completo.png', dpi=150, bbox_inches='tight')
print("Panel completo guardado en: /tmp/panel_completo.png")

print("\n" + "=" * 60)
print("FIN DEL SCRIPT")
print("Todos los gráficos han sido generados exitosamente")
print("=" * 60)

# plt.show()  # Descomentar para mostrar gráficos interactivos
