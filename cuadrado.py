import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


# =========================================================
# FIGURA 1: CUADRADO
# =========================================================

A = (-0.5, 1, 0)
B = (1, 2, 0)
C = (2.5, 1, 0)
D = (1, 0, 0)

vertices1 = [A, B, C, D]

fig = plt.figure(figsize=(15, 10))


# =========================================================
# FIGURA 2: TRIÁNGULO
# =========================================================

E = (0, 0, 0)
F = (2, 0, 0)
G = (1, 2, 0)

vertices2 = [E, F, G]


# =========================================================
# FIGURA 3: RECTÁNGULO
# =========================================================

H = (0, 0, 0)
I = (3, 0, 0)
J = (3, 1.5, 0)
K = (0, 1.5, 0)

vertices3 = [H, I, J, K]


# =========================================================
# FIGURA 4: PENTÁGONO
# =========================================================

L = (0, 1, 0)
M = (0.8, 2, 0)
N = (2, 1.6, 0)
O = (1.7, 0.3, 0)
P = (0.5, 0, 0)

vertices4 = [L, M, N, O, P]


# =========================================================
# FIGURA 5: CUBO
# =========================================================

A1 = (0, 0, 0)
B1 = (2, 0, 0)
C1 = (2, 2, 0)
D1 = (0, 2, 0)

E1 = (0, 0, 2)
F1 = (2, 0, 2)
G1 = (2, 2, 2)
H1 = (0, 2, 2)

vertices5 = [A1, B1, C1, D1, E1, F1, G1, H1]


# =========================================================
# FUNCIÓN PARA DIBUJAR FIGURAS PLANAS
# =========================================================

def dibujar_figura(ax, vertices, nombre_vertices, aristas, titulo):

    # ----------------------------
    # Dibujar la cara
    # ----------------------------

    cara = Poly3DCollection(
        [vertices],
        alpha=0.4,
        edgecolor="black"
    )

    ax.add_collection3d(cara)

    # ----------------------------
    # Dibujar los vértices
    # ----------------------------

    for nombre, vertice in zip(nombre_vertices, vertices):

        x, y, z = vertice

        ax.scatter(x, y, z, s=80)

        ax.text(
            x,
            y,
            z + 0.1,
            nombre,
            fontsize=12
        )

    # ----------------------------
    # Dibujar las aristas
    # ----------------------------

    for inicio, fin in aristas:

        ax.plot(
            [inicio[0], fin[0]],
            [inicio[1], fin[1]],
            [inicio[2], fin[2]],
            linewidth=2
        )

    # ----------------------------
    # Configurar escena
    # ----------------------------

    ax.set_xlim(-1, 3)
    ax.set_ylim(-1, 3)
    ax.set_zlim(-1, 3)

    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_zlabel("Eje Z")

    ax.set_title(titulo)


# =========================================================
# DIBUJAR FIGURA 1: CUADRADO
# =========================================================

ax1 = fig.add_subplot(231, projection='3d')

aristas1 = [
    (A, B),
    (B, C),
    (C, D),
    (D, A)
]

dibujar_figura(
    ax1,
    vertices1,
    ["A", "B", "C", "D"],
    aristas1,
    "Figura 1: Cuadrado"
)


# =========================================================
# DIBUJAR FIGURA 2: TRIÁNGULO
# =========================================================

ax2 = fig.add_subplot(232, projection='3d')

aristas2 = [
    (E, F),
    (F, G),
    (G, E)
]

dibujar_figura(
    ax2,
    vertices2,
    ["E", "F", "G"],
    aristas2,
    "Figura 2: Triángulo"
)


# =========================================================
# DIBUJAR FIGURA 3: RECTÁNGULO
# =========================================================

ax3 = fig.add_subplot(233, projection='3d')

aristas3 = [
    (H, I),
    (I, J),
    (J, K),
    (K, H)
]

dibujar_figura(
    ax3,
    vertices3,
    ["H", "I", "J", "K"],
    aristas3,
    "Figura 3: Rectángulo"
)


# =========================================================
# DIBUJAR FIGURA 4: PENTÁGONO
# =========================================================

ax4 = fig.add_subplot(234, projection='3d')

aristas4 = [
    (L, M),
    (M, N),
    (N, O),
    (O, P),
    (P, L)
]

dibujar_figura(
    ax4,
    vertices4,
    ["L", "M", "N", "O", "P"],
    aristas4,
    "Figura 4: Pentágono"
)


# =========================================================
# FIGURA 5: CUBO
# =========================================================

ax5 = fig.add_subplot(235, projection='3d')

# Caras del cubo

caras_cubo = [
    [A1, B1, C1, D1],
    [E1, F1, G1, H1],
    [A1, B1, F1, E1],
    [B1, C1, G1, F1],
    [C1, D1, H1, G1],
    [D1, A1, E1, H1]
]

cara_cubo = Poly3DCollection(
    caras_cubo,
    alpha=0.4,
    edgecolor="black"
)

ax5.add_collection3d(cara_cubo)


# ----------------------------
# Vértices del cubo
# ----------------------------

nombres_cubo = [
    "A", "B", "C", "D",
    "E", "F", "G", "H"
]

for nombre, vertice in zip(nombres_cubo, vertices5):

    x, y, z = vertice

    ax5.scatter(x, y, z, s=80)

    ax5.text(
        x,
        y,
        z + 0.1,
        nombre,
        fontsize=12
    )


# ----------------------------
# Aristas del cubo
# ----------------------------

aristas_cubo = [
    (A1, B1),
    (B1, C1),
    (C1, D1),
    (D1, A1),

    (E1, F1),
    (F1, G1),
    (G1, H1),
    (H1, E1),

    (A1, E1),
    (B1, F1),
    (C1, G1),
    (D1, H1)
]

for inicio, fin in aristas_cubo:

    ax5.plot(
        [inicio[0], fin[0]],
        [inicio[1], fin[1]],
        [inicio[2], fin[2]],
        linewidth=2
    )


ax5.set_xlim(-1, 3)
ax5.set_ylim(-1, 3)
ax5.set_zlim(-1, 3)

ax5.set_xlabel("Eje X")
ax5.set_ylabel("Eje Y")
ax5.set_zlabel("Eje Z")

ax5.set_title("Figura 5: Cubo")


# =========================================================
# MOSTRAR LAS 5 FIGURAS
# =========================================================

plt.tight_layout()

plt.show()