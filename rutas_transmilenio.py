import heapq

# -----------------------------
# Base de conocimiento ampliada
# -----------------------------
grafo = {
    "Portal Norte": [("Calle 100", 5)],
    "Calle 100": [("Portal Norte", 5), ("Héroes", 4)],
    "Héroes": [("Calle 100", 4), ("Calle 72", 3)],
    "Calle 72": [("Héroes", 3), ("Calle 63", 2), ("Calle 26", 6)],
    "Calle 63": [("Calle 72", 2), ("Universidades", 5)],
    "Universidades": [("Calle 63", 5), ("Museo del Oro", 3)],
    "Museo del Oro": [("Universidades", 3), ("Av Jiménez", 2)],
    "Calle 26": [("Calle 72", 6), ("Av Jiménez", 4)],
    "Av Jiménez": [("Calle 26", 4), ("Museo del Oro", 2), ("Portal Américas", 8), ("Restrepo", 6)],

    # Zona sur
    "Restrepo": [("Av Jiménez", 6), ("Venecia", 5)],
    "Venecia": [("Restrepo", 5), ("Bosa", 7)],
    "Bosa": [("Venecia", 7)],

    "Portal Américas": [("Av Jiménez", 8)]
}

# -----------------------------
# Heurística (estimación hacia Bosa)
# -----------------------------
heuristica = {
    "Portal Norte": 30,
    "Calle 100": 26,
    "Héroes": 23,
    "Calle 72": 20,
    "Calle 63": 18,
    "Universidades": 15,
    "Museo del Oro": 12,
    "Calle 26": 14,
    "Av Jiménez": 10,
    "Restrepo": 6,
    "Venecia": 3,
    "Bosa": 0,
    "Portal Américas": 9
}

# -----------------------------
# Algoritmo A*
# -----------------------------
def a_estrella(inicio, objetivo):
    cola = []
    heapq.heappush(cola, (0, inicio))

    costos = {inicio: 0}
    padres = {inicio: None}

    while cola:
        _, actual = heapq.heappop(cola)

        if actual == objetivo:
            break

        for vecino, costo in grafo[actual]:
            nuevo_costo = costos[actual] + costo

            if vecino not in costos or nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                prioridad = nuevo_costo + heuristica[vecino]
                heapq.heappush(cola, (prioridad, vecino))
                padres[vecino] = actual

    # reconstrucción de ruta
    ruta = []
    nodo = objetivo
    while nodo:
        ruta.append(nodo)
        nodo = padres[nodo]

    ruta.reverse()
    return ruta, costos.get(objetivo, None)

# -----------------------------
# Interfaz
# -----------------------------
print("\n=== SISTEMA DE RUTAS TRANSMILENIO (AMPLIADO) ===\n")

print("Estaciones disponibles:")
for estacion in grafo:
    print("-", estacion)

inicio = input("\nIngrese estación de inicio: ")
destino = input("Ingrese estación destino: ")

if inicio not in grafo or destino not in grafo:
    print("\n❌ Estación no válida")
else:
    ruta, costo = a_estrella(inicio, destino)

    if costo is None:
        print("\n⚠ No se encontró ruta")
    else:
        print("\n✅ Mejor ruta encontrada:")
        print(" → ".join(ruta))
        print("⏱ Tiempo estimado:", costo, "minutos")