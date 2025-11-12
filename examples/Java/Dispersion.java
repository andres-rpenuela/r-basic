/**
 * ============================================
 * MEDIDAS DE DISPERSIÓN EN JAVA
 * ============================================
 * 
 * Este programa demuestra el cálculo de medidas de dispersión:
 * - Rango
 * - Varianza
 * - Desviación Estándar
 * - Coeficiente de Variación
 * - Rango Intercuartílico (IQR)
 */

import java.util.*;

public class Dispersion {
    
    public static void main(String[] args) {
        System.out.println("=".repeat(60));
        System.out.println("MEDIDAS DE DISPERSIÓN EN JAVA");
        System.out.println("=".repeat(60));
        
        // Dos grupos con misma media pero diferente dispersión
        double[] grupoA = {48, 49, 50, 51, 52};  // Baja dispersión
        double[] grupoB = {10, 30, 50, 70, 90};  // Alta dispersión
        
        System.out.println("\n=== COMPARACIÓN DE DISPERSIÓN ===");
        System.out.printf("Grupo A - Media: %.2f\n", calcularMedia(grupoA));
        System.out.printf("Grupo B - Media: %.2f\n", calcularMedia(grupoB));
        System.out.println("Ambos grupos tienen la misma media, pero diferente dispersión\n");
        
        // ============================================
        // 1. RANGO
        // ============================================
        
        System.out.println("=".repeat(60));
        System.out.println("RANGO");
        System.out.println("=".repeat(60));
        
        double rangoA = calcularRango(grupoA);
        double rangoB = calcularRango(grupoB);
        
        System.out.printf("Rango Grupo A: %.2f\n", rangoA);
        System.out.printf("Rango Grupo B: %.2f\n", rangoB);
        
        // Calificaciones de ejemplo
        double[] calificaciones = {85, 90, 78, 92, 88, 76, 95, 89, 84, 91};
        System.out.printf("\nRango de calificaciones: %.2f\n", calcularRango(calificaciones));
        System.out.printf("Min: %.2f | Max: %.2f\n", encontrarMin(calificaciones), encontrarMax(calificaciones));
        
        // ============================================
        // 2. VARIANZA
        // ============================================
        
        System.out.println("\n" + "=".repeat(60));
        System.out.println("VARIANZA");
        System.out.println("=".repeat(60));
        
        double varA = calcularVarianza(grupoA, true);  // muestral
        double varB = calcularVarianza(grupoB, true);
        
        System.out.printf("Varianza Muestral Grupo A: %.2f\n", varA);
        System.out.printf("Varianza Muestral Grupo B: %.2f\n", varB);
        
        // Ejemplo paso a paso
        double[] datosEjemplo = {4, 8, 6, 5, 7};
        System.out.println("\n--- Cálculo Paso a Paso ---");
        System.out.println("Datos: " + Arrays.toString(datosEjemplo));
        
        double media = calcularMedia(datosEjemplo);
        System.out.printf("Media: %.2f\n", media);
        
        System.out.print("Desviaciones: ");
        for (double valor : datosEjemplo) {
            System.out.printf("%.2f ", valor - media);
        }
        System.out.println();
        
        System.out.print("Desviaciones²: ");
        double sumaCuadrados = 0;
        for (double valor : datosEjemplo) {
            double desv = valor - media;
            System.out.printf("%.2f ", desv * desv);
            sumaCuadrados += desv * desv;
        }
        System.out.println();
        
        System.out.printf("Suma de desviaciones²: %.2f\n", sumaCuadrados);
        System.out.printf("Varianza muestral: %.2f\n", calcularVarianza(datosEjemplo, true));
        
        // ============================================
        // 3. DESVIACIÓN ESTÁNDAR
        // ============================================
        
        System.out.println("\n" + "=".repeat(60));
        System.out.println("DESVIACIÓN ESTÁNDAR");
        System.out.println("=".repeat(60));
        
        double sdA = calcularDesviacionEstandar(grupoA, true);
        double sdB = calcularDesviacionEstandar(grupoB, true);
        
        System.out.printf("Desviación Estándar Grupo A: %.2f\n", sdA);
        System.out.printf("Desviación Estándar Grupo B: %.2f\n", sdB);
        
        // Simulación de regla 68-95-99.7
        System.out.println("\n--- Regla 68-95-99.7 (conceptual) ---");
        System.out.println("En una distribución normal:");
        System.out.println("  ~68% de los datos están dentro de ±1 DE");
        System.out.println("  ~95% de los datos están dentro de ±2 DE");
        System.out.println("  ~99.7% de los datos están dentro de ±3 DE");
        
        // ============================================
        // 4. COEFICIENTE DE VARIACIÓN
        // ============================================
        
        System.out.println("\n" + "=".repeat(60));
        System.out.println("COEFICIENTE DE VARIACIÓN");
        System.out.println("=".repeat(60));
        
        double cvA = calcularCoeficienteVariacion(grupoA);
        double cvB = calcularCoeficienteVariacion(grupoB);
        
        System.out.printf("CV Grupo A: %.2f%%\n", cvA);
        System.out.printf("CV Grupo B: %.2f%%\n", cvB);
        
        // Ejemplo práctico: comparar variables en diferentes escalas
        double[] alturasCm = {170, 175, 168, 180, 172};  // en cm
        double[] pesosKg = {70, 75, 68, 80, 72};         // en kg
        
        System.out.println("\n--- Comparación de Variables Diferentes ---");
        System.out.printf("Alturas - Media: %.2f cm | DE: %.2f cm\n", 
                         calcularMedia(alturasCm), calcularDesviacionEstandar(alturasCm, true));
        System.out.printf("         CV: %.2f%%\n", calcularCoeficienteVariacion(alturasCm));
        System.out.printf("Pesos   - Media: %.2f kg | DE: %.2f kg\n", 
                         calcularMedia(pesosKg), calcularDesviacionEstandar(pesosKg, true));
        System.out.printf("         CV: %.2f%%\n", calcularCoeficienteVariacion(pesosKg));
        
        // ============================================
        // 5. RANGO INTERCUARTÍLICO (IQR)
        // ============================================
        
        System.out.println("\n" + "=".repeat(60));
        System.out.println("RANGO INTERCUARTÍLICO");
        System.out.println("=".repeat(60));
        
        double q1 = calcularCuartil(calificaciones, 25);
        double q2 = calcularCuartil(calificaciones, 50);
        double q3 = calcularCuartil(calificaciones, 75);
        double iqr = q3 - q1;
        
        System.out.printf("Cuartil 1 (Q1): %.2f\n", q1);
        System.out.printf("Cuartil 2 (Q2/Mediana): %.2f\n", q2);
        System.out.printf("Cuartil 3 (Q3): %.2f\n", q3);
        System.out.printf("IQR (Q3 - Q1): %.2f\n", iqr);
        
        // ============================================
        // 6. RESUMEN COMPLETO
        // ============================================
        
        System.out.println("\n" + "=".repeat(60));
        System.out.println("RESUMEN COMPLETO DE DISPERSIÓN");
        System.out.println("=".repeat(60));
        
        imprimirResumenDispersion(calificaciones, "Calificaciones");
        imprimirResumenDispersion(grupoA, "Grupo A (baja dispersión)");
        imprimirResumenDispersion(grupoB, "Grupo B (alta dispersión)");
        
        // ============================================
        // 7. DETECCIÓN DE OUTLIERS
        // ============================================
        
        System.out.println("\n" + "=".repeat(60));
        System.out.println("DETECCIÓN DE OUTLIERS");
        System.out.println("=".repeat(60));
        
        double[] datosOutlier = {10, 12, 14, 15, 16, 18, 20, 100};
        System.out.println("Datos con outlier evidente: " + Arrays.toString(datosOutlier));
        detectarOutliers(datosOutlier);
        
        // ============================================
        // 8. EJEMPLO: CONTROL DE CALIDAD
        // ============================================
        
        System.out.println("\n" + "=".repeat(60));
        System.out.println("EJEMPLO: CONTROL DE CALIDAD");
        System.out.println("=".repeat(60));
        
        // Simulación: mediciones de piezas manufacturadas (en mm)
        // En producción real, estos datos vendrían de mediciones
        double[] maquinaA = {10.0, 10.1, 9.9, 10.0, 10.1, 9.9, 10.0, 10.1};
        double[] maquinaB = {10.0, 10.5, 9.5, 10.0, 10.5, 9.5, 10.0, 10.5};
        
        System.out.println("Máquina A:");
        System.out.printf("  Media: %.3f mm\n", calcularMedia(maquinaA));
        System.out.printf("  DE: %.3f mm\n", calcularDesviacionEstandar(maquinaA, true));
        System.out.printf("  CV: %.2f%%\n", calcularCoeficienteVariacion(maquinaA));
        
        System.out.println("\nMáquina B:");
        System.out.printf("  Media: %.3f mm\n", calcularMedia(maquinaB));
        System.out.printf("  DE: %.3f mm\n", calcularDesviacionEstandar(maquinaB, true));
        System.out.printf("  CV: %.2f%%\n", calcularCoeficienteVariacion(maquinaB));
        
        System.out.println("\nConclusión: Máquina A tiene mayor precisión (menor variabilidad)");
        
        System.out.println("\n" + "=".repeat(60));
        System.out.println("FIN DEL PROGRAMA");
        System.out.println("=".repeat(60));
    }
    
    // ============================================
    // MÉTODOS DE CÁLCULO
    // ============================================
    
    public static double calcularMedia(double[] datos) {
        double suma = 0;
        for (double valor : datos) {
            suma += valor;
        }
        return suma / datos.length;
    }
    
    public static double calcularRango(double[] datos) {
        return encontrarMax(datos) - encontrarMin(datos);
    }
    
    public static double encontrarMin(double[] datos) {
        double min = datos[0];
        for (double valor : datos) {
            if (valor < min) min = valor;
        }
        return min;
    }
    
    public static double encontrarMax(double[] datos) {
        double max = datos[0];
        for (double valor : datos) {
            if (valor > max) max = valor;
        }
        return max;
    }
    
    /**
     * Calcula la varianza
     * @param muestral true para varianza muestral (n-1), false para poblacional (n)
     */
    public static double calcularVarianza(double[] datos, boolean muestral) {
        double media = calcularMedia(datos);
        double sumaCuadrados = 0;
        
        for (double valor : datos) {
            double desviacion = valor - media;
            sumaCuadrados += desviacion * desviacion;
        }
        
        int divisor = muestral ? datos.length - 1 : datos.length;
        return sumaCuadrados / divisor;
    }
    
    /**
     * Calcula la desviación estándar
     */
    public static double calcularDesviacionEstandar(double[] datos, boolean muestral) {
        return Math.sqrt(calcularVarianza(datos, muestral));
    }
    
    /**
     * Calcula el coeficiente de variación
     */
    public static double calcularCoeficienteVariacion(double[] datos) {
        double media = calcularMedia(datos);
        double sd = calcularDesviacionEstandar(datos, true);
        return (sd / media) * 100;
    }
    
    /**
     * Calcula un cuartil específico
     * @param percentil el percentil deseado (25, 50, 75, etc.)
     */
    public static double calcularCuartil(double[] datos, double percentil) {
        double[] datosOrdenados = datos.clone();
        Arrays.sort(datosOrdenados);
        
        double posicion = (percentil / 100.0) * (datosOrdenados.length - 1);
        int indiceInferior = (int) Math.floor(posicion);
        int indiceSuperior = (int) Math.ceil(posicion);
        
        if (indiceInferior == indiceSuperior) {
            return datosOrdenados[indiceInferior];
        }
        
        double fraccion = posicion - indiceInferior;
        return datosOrdenados[indiceInferior] * (1 - fraccion) + 
               datosOrdenados[indiceSuperior] * fraccion;
    }
    
    /**
     * Imprime un resumen completo de dispersión
     */
    public static void imprimirResumenDispersion(double[] datos, String nombre) {
        System.out.println("\n--- " + nombre + " ---");
        System.out.printf("Rango: %.2f\n", calcularRango(datos));
        System.out.printf("Varianza: %.2f\n", calcularVarianza(datos, true));
        System.out.printf("Desviación Estándar: %.2f\n", calcularDesviacionEstandar(datos, true));
        System.out.printf("Coeficiente de Variación: %.2f%%\n", calcularCoeficienteVariacion(datos));
        
        double q1 = calcularCuartil(datos, 25);
        double q3 = calcularCuartil(datos, 75);
        System.out.printf("IQR: %.2f\n", q3 - q1);
    }
    
    /**
     * Detecta outliers usando el método IQR
     */
    public static void detectarOutliers(double[] datos) {
        double q1 = calcularCuartil(datos, 25);
        double q3 = calcularCuartil(datos, 75);
        double iqr = q3 - q1;
        
        double limiteInferior = q1 - 1.5 * iqr;
        double limiteSuperior = q3 + 1.5 * iqr;
        
        System.out.printf("Límite inferior: %.2f\n", limiteInferior);
        System.out.printf("Límite superior: %.2f\n", limiteSuperior);
        
        List<Double> outliers = new ArrayList<>();
        for (double valor : datos) {
            if (valor < limiteInferior || valor > limiteSuperior) {
                outliers.add(valor);
            }
        }
        
        System.out.printf("Outliers encontrados: %d\n", outliers.size());
        if (!outliers.isEmpty()) {
            System.out.println("Valores: " + outliers);
        }
    }
}
