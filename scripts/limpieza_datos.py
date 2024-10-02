import pandas as pd
import os

def cargar_datos(ruta):
   
    return pd.read_csv(ruta)


def manejar_valores_faltantes(data):
   # Explorar las primeras filas del dataset
    print(data.head())

    # Obtener información básica sobre las columnas y tipos de datos
    print(data.info())

    # 1)¿Cómo identifico los valores faltantes en mi dataset?
    # Antes de realizar cualquier transformación, es importante saber qué columnas tienen valores faltantes.
    # Mostrar la cantidad de valores faltantes por columna
    missing_values = data.isnull().sum()
    print(missing_values)

    # 2¿Cómo manejo los valores faltantes?
    # Para los valores faltantes, puedes elegir 
    # eliminar las filas o imputar valores según el tipo de datos

    # Opc1:Eliminar filas con cualquier valor faltante
    # df_cleaned = df.dropna()

    # Opc2: # Eliminar filas con valores faltantes en columnas clave
    df_cleaned = data.dropna(subset=['Previous Grades', 'Attendance Rate'])

    # Opc3: Imputación de valores faltantes (por ejemplo, para una columna específica)
    df_cleaned = df_cleaned.copy()  # Asegúrate de trabajar con una copia
    df_cleaned['Attendance Rate'] = df_cleaned['Attendance Rate'].fillna(df_cleaned['Attendance Rate'].mean())

    return df_cleaned

def corregir_datos_incorrectos(data):
    """
    Corregir valores fuera de rango o inconsistentes en el dataset.
    """
    # Corregir tasas de asistencia fuera de rango (0-100)
    data['Attendance Rate'] = data['Attendance Rate'].apply(lambda x: 100 if x > 100 else (0 if x < 0 else x))
    
    return data



if __name__ == "__main__":
    # Cargar el archivo CSV
    data = cargar_datos('/Users/rosanagonzalez/Inicial/Inicial/student_data_cleaning/data/student_performance_prediction.csv')
    
    # Manejar valores faltantes
    dataset_limpio = manejar_valores_faltantes(data)
    
    # Corregir datos incorrectos
    dataset_limpio = corregir_datos_incorrectos(dataset_limpio)
    
    # Guardar el dataset limpio
    if not os.path.exists('Inicial/student_data_cleaning/output/'):
        os.makedirs('Inicial/student_data_cleaning/output/')
    dataset_limpio.to_csv('Inicial/student_data_cleaning/output/dataset_limpio.csv', index=False)
    print("Limpieza completada y archivo guardado.")