import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# -----------------------------
# Dataset
# -----------------------------
data = {
    "estacion": ["Portal Norte", "Calle 100", "Héroes", "Calle 72", "Av Jiménez",
                 "Restrepo", "Venecia", "Bosa", "Terreros", "San Mateo"],
    
    "distancia_centro": [15, 12, 10, 8, 5, 7, 12, 20, 22, 25],
    "flujo_pasajeros": [9000, 7000, 6500, 8000, 12000, 8500, 7500, 8000, 7000, 6000],
    "conexiones": [3, 2, 2, 3, 4, 3, 2, 2, 1, 1]
}

df = pd.DataFrame(data)

# -----------------------------
# Variables para clustering
# -----------------------------
X = df[["distancia_centro", "flujo_pasajeros"]]

# -----------------------------
# Modelo K-Means
# -----------------------------
kmeans = KMeans(n_clusters=3, random_state=0)
df["cluster"] = kmeans.fit_predict(X)

# -----------------------------
# Mostrar resultados
# -----------------------------
print("\nClasificación de estaciones:\n")
print(df[["estacion", "cluster"]])

# -----------------------------
# Gráfica de clusters
# -----------------------------
plt.scatter(df["distancia_centro"], df["flujo_pasajeros"])

# Etiquetas
for i in range(len(df)):
    plt.text(df["distancia_centro"][i], df["flujo_pasajeros"][i], df["estacion"][i])

plt.xlabel("Distancia al centro")
plt.ylabel("Flujo de pasajeros")
plt.title("Clusters de estaciones")

plt.show()
