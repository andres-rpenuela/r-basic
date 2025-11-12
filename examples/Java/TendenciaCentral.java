/**
 * ============================================
 * MEDIDAS DE TENDENCIA CENTRAL EN JAVA
 * ============================================
 * 
 * Este programa demuestra el cálculo de media, mediana y moda
 * usando Java estándar sin librerías externas.
 */

import java.util.*;

public class TendenciaCentral {
    
    public static void main(String[] args) {
        System.out.println("=".repeat(60));
        System.out.println("MEDIDAS DE TENDENCIA CENTRAL EN JAVA");
        System.out.println("=".repeat(60));
        
        // Crear datos de ejemplo - calificaciones de estudiantes
        double[] calificaciones = {85, 90, 78, 92, 88, 76, 95, 89, 84, 91,
                                   87, 93, 82, 88, 90, 86, 94, 79, 88, 92};
        
        System.out.println("\nCalificaciones de estudiantes:");
        System.out.println(Arrays.toString(calificaciones));
        System.out.println("Total de estudiantes: " + calificaciones.length);
        
        // ============================================
        // 1. MEDIA (PROMEDIO)
        // ============================================
        
        System.out.println("\n" + "=".repeat(60));
        System.out.println("MEDIA (PROMEDIO)");
        System.out.println("=".repeat(60));
        
        double media = calcularMedia(calificaciones);
        System.out.printf("Media: %.2f\n", media);
        
        // ============================================
        // 2. MEDIANA
        // ============================================
        
        System.out.println("\n" + "=".repeat(60));
        System.out.println("MEDIANA");
        System.out.println("=".repeat(60));
        
        double mediana = calcularMediana(calificaciones);
        System.out.printf("Mediana: %.2f\n", mediana);
        
        // Ejemplo con número par e impar
        double[] pares = {10, 20, 30, 40};
        double[] impares = {10, 20, 30, 40, 50};
        System.out.printf("Mediana (n par): %.2f\n", calcularMediana(pares));
        System.out.printf("Mediana (n impar): %.2f\n", calcularMediana(impares));
        
        // ============================================
        // 3. MODA
        // ============================================
        
        System.out.println("\n" + "=".repeat(60));
        System.out.println("MODA");
        System.out.println("=".repeat(60));
        
        ResultadoModa moda = calcularModa(calificaciones);
        System.out.printf("Moda: %.2f | Frecuencia: %d\n", moda.valor, moda.frecuencia);
        
        // Ejemplo con moda clara
        double[] datosModa = {5, 3, 7, 3, 9, 3, 4, 3, 6};
        ResultadoModa modaEjemplo = calcularModa(datosModa);
        System.out.printf("Moda de ejemplo: %.2f\n", modaEjemplo.valor);
        
        // ============================================
        // 4. RESUMEN ESTADÍSTICO COMPLETO
        // ============================================
        
        System.out.println("\n" + "=".repeat(60));
        System.out.println("RESUMEN ESTADÍSTICO COMPLETO");
        System.out.println("=".repeat(60));
        
        ResumenEstadistico resumen = calcularResumen(calificaciones);
        System.out.println(resumen);
        
        // ============================================
        // 5. EJEMPLO PRÁCTICO: SALARIOS
        // ============================================
        
        System.out.println("\n" + "=".repeat(60));
        System.out.println("EJEMPLO PRÁCTICO: SALARIOS");
        System.out.println("=".repeat(60));
        
        // Salarios en miles de dólares (con outlier: el CEO)
        double[] salarios = {35, 42, 38, 45, 40, 43, 37, 41, 39, 44, 250};
        
        System.out.println("Salarios (miles de $): " + Arrays.toString(salarios));
        
        double mediaSalario = calcularMedia(salarios);
        double medianaSalario = calcularMediana(salarios);
        
        System.out.printf("\nMedia de salarios: $%.2fk\n", mediaSalario);
        System.out.printf("Mediana de salarios: $%.2fk\n", medianaSalario);
        System.out.println("\nObservación: La media es mayor por el outlier (CEO con $250k)");
        System.out.println("La mediana ($41k) representa mejor el salario típico");
        
        // ============================================
        // 6. MEDIDAS RESISTENTES VS NO RESISTENTES
        // ============================================
        
        System.out.println("\n" + "=".repeat(60));
        System.out.println("RESISTENCIA A OUTLIERS");
        System.out.println("=".repeat(60));
        
        double[] datosOriginales = {10, 12, 14, 15, 16, 18, 20};
        double[] datosConOutlier = {10, 12, 14, 15, 16, 18, 100};
        
        System.out.println("Datos originales: " + Arrays.toString(datosOriginales));
        System.out.printf("  Media: %.2f\n", calcularMedia(datosOriginales));
        System.out.printf("  Mediana: %.2f\n", calcularMediana(datosOriginales));
        
        System.out.println("\nDatos con outlier (100 en lugar de 20): " + Arrays.toString(datosConOutlier));
        System.out.printf("  Media: %.2f - ¡Cambió mucho!\n", calcularMedia(datosConOutlier));
        System.out.printf("  Mediana: %.2f - Cambió poco\n", calcularMediana(datosConOutlier));
        
        // ============================================
        // 7. FUNCIONES ADICIONALES
        // ============================================
        
        System.out.println("\n" + "=".repeat(60));
        System.out.println("FUNCIONES ADICIONALES");
        System.out.println("=".repeat(60));
        
        // Media ponderada
        double[] valores = {80, 90, 85};
        double[] pesos = {0.3, 0.5, 0.2};
        double mediaPonderada = calcularMediaPonderada(valores, pesos);
        System.out.printf("Media ponderada: %.2f\n", mediaPonderada);
        
        // Media geométrica
        double[] valoresPos = {2, 4, 8};
        double mediaGeometrica = calcularMediaGeometrica(valoresPos);
        System.out.printf("Media geométrica: %.2f\n", mediaGeometrica);
        
        // Media armónica
        double mediaArmonica = calcularMediaArmonica(valoresPos);
        System.out.printf("Media armónica: %.2f\n", mediaArmonica);
        
        System.out.println("\n" + "=".repeat(60));
        System.out.println("FIN DEL PROGRAMA");
        System.out.println("=".repeat(60));
    }
    
    // ============================================
    // MÉTODOS DE CÁLCULO
    // ============================================
    
    /**
     * Calcula la media (promedio) de un array de números
     */
    public static double calcularMedia(double[] datos) {
        if (datos == null || datos.length == 0) {
            throw new IllegalArgumentException("El array no puede estar vacío");
        }
        
        double suma = 0;
        for (double valor : datos) {
            suma += valor;
        }
        return suma / datos.length;
    }
    
    /**
     * Calcula la mediana de un array de números
     */
    public static double calcularMediana(double[] datos) {
        if (datos == null || datos.length == 0) {
            throw new IllegalArgumentException("El array no puede estar vacío");
        }
        
        // Copiar y ordenar el array
        double[] datosOrdenados = datos.clone();
        Arrays.sort(datosOrdenados);
        
        int n = datosOrdenados.length;
        if (n % 2 == 0) {
            // Si n es par, promedio de los dos valores centrales
            return (datosOrdenados[n/2 - 1] + datosOrdenados[n/2]) / 2.0;
        } else {
            // Si n es impar, valor central
            return datosOrdenados[n/2];
        }
    }
    
    /**
     * Calcula la moda (valor más frecuente)
     */
    public static ResultadoModa calcularModa(double[] datos) {
        if (datos == null || datos.length == 0) {
            throw new IllegalArgumentException("El array no puede estar vacío");
        }
        
        // Usar un mapa para contar frecuencias
        Map<Double, Integer> frecuencias = new HashMap<>();
        for (double valor : datos) {
            frecuencias.put(valor, frecuencias.getOrDefault(valor, 0) + 1);
        }
        
        // Encontrar el valor con mayor frecuencia
        double moda = datos[0];
        int maxFrecuencia = 0;
        
        for (Map.Entry<Double, Integer> entry : frecuencias.entrySet()) {
            if (entry.getValue() > maxFrecuencia) {
                maxFrecuencia = entry.getValue();
                moda = entry.getKey();
            }
        }
        
        return new ResultadoModa(moda, maxFrecuencia);
    }
    
    /**
     * Calcula un resumen estadístico completo
     */
    public static ResumenEstadistico calcularResumen(double[] datos) {
        double[] datosOrdenados = datos.clone();
        Arrays.sort(datosOrdenados);
        
        return new ResumenEstadistico(
            datos.length,
            calcularMedia(datos),
            calcularMediana(datos),
            calcularModa(datos).valor,
            datosOrdenados[0],  // mínimo
            datosOrdenados[datosOrdenados.length - 1]  // máximo
        );
    }
    
    /**
     * Calcula la media ponderada
     */
    public static double calcularMediaPonderada(double[] valores, double[] pesos) {
        if (valores.length != pesos.length) {
            throw new IllegalArgumentException("Los arrays deben tener la misma longitud");
        }
        
        double sumaProductos = 0;
        double sumaPesos = 0;
        
        for (int i = 0; i < valores.length; i++) {
            sumaProductos += valores[i] * pesos[i];
            sumaPesos += pesos[i];
        }
        
        return sumaProductos / sumaPesos;
    }
    
    /**
     * Calcula la media geométrica
     */
    public static double calcularMediaGeometrica(double[] datos) {
        double producto = 1;
        for (double valor : datos) {
            if (valor <= 0) {
                throw new IllegalArgumentException("Todos los valores deben ser positivos");
            }
            producto *= valor;
        }
        return Math.pow(producto, 1.0 / datos.length);
    }
    
    /**
     * Calcula la media armónica
     */
    public static double calcularMediaArmonica(double[] datos) {
        double sumaReciprocas = 0;
        for (double valor : datos) {
            if (valor == 0) {
                throw new IllegalArgumentException("No puede haber valores cero");
            }
            sumaReciprocas += 1.0 / valor;
        }
        return datos.length / sumaReciprocas;
    }
    
    // ============================================
    // CLASES AUXILIARES
    // ============================================
    
    /**
     * Clase para almacenar el resultado de la moda
     */
    static class ResultadoModa {
        double valor;
        int frecuencia;
        
        ResultadoModa(double valor, int frecuencia) {
            this.valor = valor;
            this.frecuencia = frecuencia;
        }
    }
    
    /**
     * Clase para almacenar un resumen estadístico
     */
    static class ResumenEstadistico {
        int count;
        double media;
        double mediana;
        double moda;
        double min;
        double max;
        
        ResumenEstadistico(int count, double media, double mediana, 
                          double moda, double min, double max) {
            this.count = count;
            this.media = media;
            this.mediana = mediana;
            this.moda = moda;
            this.min = min;
            this.max = max;
        }
        
        @Override
        public String toString() {
            return String.format(
                "Count:   %d\n" +
                "Mean:    %.2f\n" +
                "Median:  %.2f\n" +
                "Mode:    %.2f\n" +
                "Min:     %.2f\n" +
                "Max:     %.2f",
                count, media, mediana, moda, min, max
            );
        }
    }
}
