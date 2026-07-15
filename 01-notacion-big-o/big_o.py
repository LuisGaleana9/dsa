"""
Demostración de Complejidad Temporal (Notación Big O)
------------------------------------------------------
La Notación Big O describe el "peor escenario posible".
Nos dice cómo crece el tiempo de ejecución de un algoritmo 
a medida que aumenta el tamaño de los datos de entrada (n).
"""

# Datos de prueba simulando registros en una base de datos
nombres = ["Emmanuel", "Luis", "Aleydis", "Juan", "Miguel"]

# ---------------------------------------------------------
# 1. O(1) - Tiempo Constante
# ---------------------------------------------------------
# No importa si hay 5 nombres o 5 millones, acceder a un 
# índice específico siempre toma exactamente 1 operación.
def obtener_primer_elemento(lista):
    print(f"O(1): El primer nombre es {lista[0]}")

# ---------------------------------------------------------
# 2. O(n) - Tiempo Lineal
# ---------------------------------------------------------
# El número de operaciones crece proporcionalmente a los datos.
# Si buscamos "Miguel", el bucle tiene que dar 5 vueltas.
# Si hubiera 1 millón de registros, en el peor caso daría 1 millón de vueltas.
def buscar_elemento(lista, objetivo):
    operaciones = 0
    for elemento in lista:
        operaciones += 1
        if elemento == objetivo:
            print(f"O(n): Encontrado '{objetivo}' en {operaciones} operaciones.")
            return
    print("No encontrado.")

# ---------------------------------------------------------
# 3. O(n^2) - Tiempo Cuadrático
# ---------------------------------------------------------
# Un bucle anidado dentro de otro bucle. 
# Si n=5, hace 5x5 = 25 operaciones. 
# Si n=1,000, hace 1,000,000 de operaciones.
def mostrar_pares_posibles(lista):
    operaciones = 0
    print("O(n^2): Generando pares...")
    for i in lista:
        for j in lista:
            operaciones += 1
            # print(f"Par: {i} - {j}") 
    print(f"Total de operaciones para {len(lista)} elementos: {operaciones}")

# --- Ejecución de prueba ---
obtener_primer_elemento(nombres)
buscar_elemento(nombres, "Luis")
mostrar_pares_posibles(nombres)