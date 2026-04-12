#  Proyecto de Inteligencia Artificial - Sistema de Rutas TransMilenio

##  Descripción del Proyecto

Este proyecto desarrolla un sistema inteligente aplicado al transporte masivo tipo TransMilenio, integrando técnicas de inteligencia artificial para:

* Determinar rutas óptimas entre estaciones
* Predecir tiempos de viaje mediante aprendizaje supervisado
* Identificar patrones y agrupaciones de estaciones mediante aprendizaje no supervisado

El objetivo es simular un sistema capaz de apoyar la toma de decisiones en movilidad urbana.

---

##  Componentes del Proyecto

### 🔹 1. Sistema de Búsqueda de Rutas (IA Clásica)

Se implementa un sistema basado en grafos que permite encontrar la mejor ruta entre dos estaciones.

* Uso de algoritmos de búsqueda
* Representación de estaciones como nodos
* Conexiones como aristas

📄 Archivo:

* `rutas_transmilenio.py`

---

### 🔹 2. Métodos de Aprendizaje Supervisado (M_A_S)

Se desarrolló un modelo que permite predecir el tiempo estimado de viaje con base en:

* Distancia
* Nivel de tráfico
* Hora del día

📦 Tecnologías utilizadas:

* Python
* pandas
* scikit-learn

📄 Archivos:

* `modelo_supervisado.py`
* `dataset_MAS.csv`
* `descripcion_datosMAS.md`
* `pruebasMAS.md`

---

### 🔹 3. Métodos de Aprendizaje No Supervisado (M_A_N_S)

Se implementó un modelo de clustering utilizando K-Means para agrupar estaciones según sus características.

Variables utilizadas:

* Distancia al centro
* Flujo de pasajeros
* Número de conexiones

📊 Resultado:

* Agrupación automática de estaciones en clusters
* Visualización gráfica de los grupos

📦 Tecnologías utilizadas:

* Python
* pandas
* scikit-learn
* matplotlib

📄 Archivos:

* `modelo_no_supervisado.py`
* `dataset_MANS.csv`
* `descripcion_datosMANS.md`
* `pruebasMANS.md`

---

## ⚙️ Instalación y Ejecución

### 🔹 1. Requisitos

* Python 3.x

Instalar dependencias:

```bash
python -m pip install pandas scikit-learn matplotlib
```

---

### 🔹 2. Ejecución de los programas

#### ✔ Sistema de rutas:

```bash
python rutas_transmilenio.py
```

#### ✔ Modelo supervisado:

```bash
python modelo_supervisado.py
```

#### ✔ Modelo no supervisado:

```bash
python modelo_no_supervisado.py
```

---

## 📊 Resultados

* Determinación de rutas óptimas entre estaciones
* Predicción de tiempos de viaje
* Identificación de patrones en estaciones mediante clustering
* Visualización gráfica de agrupaciones

---

## 👥 Autores

* Edgar David Tellez
* David Mora Martinez

