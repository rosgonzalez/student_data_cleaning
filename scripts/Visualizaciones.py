import pandas as pd
import matplotlib.pyplot as plt

def graficar_histograma(data, columna, titulo):
    """
    Generar un histograma para una columna específica del dataset.
    """
    plt.figure(figsize=(10, 5))
    plt.hist(data[columna], bins=20, color='blue', alpha=0.7)
    plt.title(titulo)
    plt.xlabel(columna)
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Cargar el dataset limpio
    dataset_limpio = pd.read_csv('Inicial/student_data_cleaning/output/dataset_limpio.csv')
    
    # Visualizar la distribución de las calificaciones
    graficar_histograma(dataset_limpio, 'Previous Grades', 'Distribución de Calificaciones después de la Limpieza')

    # Visualizar la distribución de la asistencia
    graficar_histograma(dataset_limpio, 'Attendance Rate', 'Distribución de Tasa de Asistencia después de la Limpieza')
    
    print("Visualizaciones completadas.")