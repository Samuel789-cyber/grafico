import pandas as pd
import matplotlib.pyplot as plt

file_path = "C:/Users/MINEDUCYT/Downloads/DATA/df_data_analisis.csv"
df = pd.read_csv(file_path)

print("Primeras filas del dataset:")
print(df.head())

columns_to_plot = ['precio', 'bateria', 'calificacion']

for col in columns_to_plot:
    if col not in df.columns:
        print(f"La columna {col} no se encuentra en el dataset.")

# Gráfico de dispersión entre precio y capacidad de batería
plt.figure(figsize=(10, 6))
plt.scatter(df['precio'], df['bateria'], c=df['calificacion'], cmap='viridis', alpha=0.7)
plt.colorbar(label='Calificación')
plt.title('Relación entre Precio, Capacidad de Batería y Calificación')
plt.xlabel('Precio (en unidades monetarias)')
plt.ylabel('Capacidad de Batería (mAh)')
plt.grid(True)
plt.show()

# Gráfico de barras de los 10 smartphones más caros
top_10_expensive = df.sort_values(by='precio', ascending=False).head(10)
plt.figure(figsize=(12, 8))
plt.barh(top_10_expensive['modelo'], top_10_expensive['precio'], color='teal')
plt.title('Top 10 Smartphones Más Caros')
plt.xlabel('Precio (en unidades monetarias)')
plt.ylabel('Modelo')
plt.gca().invert_yaxis()
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

# Gráfico de distribución de capacidades de batería
plt.figure(figsize=(10, 6))
plt.hist(df['bateria'].dropna(), bins=15, color='orange', edgecolor='black')
plt.title('Distribución de Capacidades de Batería')
plt.xlabel('Capacidad de Batería (mAh)')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()




