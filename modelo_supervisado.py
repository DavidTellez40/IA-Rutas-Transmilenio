import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# -----------------------------
# Dataset simulado
# -----------------------------
data = {
    "distancia": [5, 6, 4, 7, 3, 8, 6, 5],
    "trafico": ["alto", "medio", "bajo", "alto", "bajo", "medio", "alto", "medio"],
    "hora": ["pico", "normal", "normal", "pico", "normal", "pico", "pico", "normal"],
    "tiempo": [12, 10, 7, 15, 6, 14, 13, 9]
}

df = pd.DataFrame(data)

# -----------------------------
# Preprocesamiento
# -----------------------------
le_trafico = LabelEncoder()
le_hora = LabelEncoder()

df["trafico"] = le_trafico.fit_transform(df["trafico"])
df["hora"] = le_hora.fit_transform(df["hora"])

# -----------------------------
# Variables
# -----------------------------
X = df[["distancia", "trafico", "hora"]]
y = df["tiempo"]

# -----------------------------
# Entrenamiento
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

# -----------------------------
# Predicción
# -----------------------------
prediccion = modelo.predict([[6, le_trafico.transform(["alto"])[0], le_hora.transform(["pico"])[0]]])

print("Tiempo estimado:", prediccion[0])
