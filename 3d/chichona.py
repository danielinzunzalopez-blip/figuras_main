import numpy as np
import matplotlib.pyplot as plt

def loft(ax, z, rx, ry, color, cx=0.0, cy=0.0, n=70):
    """Cuerpo hecho de secciones elípticas; rx=ancho, ry=profundidad."""
    zz = np.linspace(z[0], z[-1], 160)
    def f(v):  # interpola y suaviza el perfil
        r = np.interp(zz, z, v)
        k = 25
        p = np.pad(r, k//2, mode="edge")
        return np.convolve(p, np.ones(k)/k, mode="valid")
    cxf = f(cx) if np.ndim(cx) else cx + 0*zz
    cyf = f(cy) if np.ndim(cy) else cy + 0*zz
    t = np.linspace(0, 2*np.pi, n)
    X = cxf[:, None] + f(rx)[:, None]*np.cos(t)
    Y = cyf[:, None] + f(ry)[:, None]*np.sin(t)
    Z = np.tile(zz[:, None], (1, n))
    # Sombreado con normales de la superficie
    dz = np.gradient(Z, axis=0); dt = np.gradient(np.stack([X, Y], -1), axis=1)
    du = np.stack([np.gradient(X, axis=0), np.gradient(Y, axis=0), dz], -1)
    dv = np.stack([dt[..., 0], dt[..., 1], np.zeros_like(Z)], -1)
    nrm = np.cross(dv, du)
    nrm /= np.linalg.norm(nrm, axis=-1, keepdims=True) + 1e-9
    luz = np.array([-0.5, -0.7, 0.6]); luz /= np.linalg.norm(luz)
    inten = np.clip(nrm @ luz, 0, 1)*0.65 + 0.35
    rgb = np.clip(np.asarray(color)[None, None, :]*inten[..., None], 0, 1)
    ax.plot_surface(X, Y, Z, facecolors=rgb, linewidth=0, antialiased=True, shade=False)

def elip(ax, c, a, b, h, color):
    u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:30j]
    ax.plot_surface(c[0]+a*np.cos(u)*np.sin(v), c[1]+b*np.sin(u)*np.sin(v),
                    c[2]+h*np.cos(v), color=color, linewidth=0, antialiased=True)

piel  = np.array([0.85, 0.65, 0.55])
pelo  = "#2a1810"
tacon = np.array([0.12, 0.12, 0.12])

fig = plt.figure(figsize=(6, 10))
ax = fig.add_subplot(111, projection="3d")

# Piernas
for s in (-1, 1):
    z  = [0.14, 0.30, 0.52, 0.60, 0.75, 0.95, 1.10, 1.18]
    rx = [0.022, 0.040, 0.050, 0.048, 0.068, 0.090, 0.092, 0.085]
    ry = [0.022, 0.040, 0.048, 0.046, 0.070, 0.090, 0.095, 0.090]
    cx = [0.050, 0.052, 0.050, 0.050, 0.055, 0.062, 0.066, 0.066]
    loft(ax, z, rx, ry, piel, cx=s*np.array(cx))
    # pie y tacón
    loft(ax, [0.0, 0.05, 0.14], [0.012, 0.022, 0.024], [0.012, 0.02, 0.022],
         tacon, cx=s*0.050, cy=[-0.015, -0.015, 0.0])
    elip(ax, (s*0.050, -0.04, 0.04), 0.022, 0.06, 0.025, tacon)

# Torso
loft(ax, [1.05, 1.15, 1.25, 1.36, 1.46, 1.55, 1.63, 1.70],
         [0.150, 0.150, 0.115, 0.100, 0.125, 0.145, 0.150, 0.075],
         [0.100, 0.115, 0.085, 0.080, 0.100, 0.105, 0.080, 0.050], piel)

# Cuello y cabeza
loft(ax, [1.68, 1.76, 1.82], [0.040, 0.034, 0.034], [0.040, 0.034, 0.034], piel)
elip(ax, (0, 0, 1.93), 0.078, 0.090, 0.108, piel)
elip(ax, (0, 0.014, 1.95), 0.084, 0.095, 0.098, pelo)
elip(ax, (0, 0.025, 2.07), 0.040, 0.040, 0.036, pelo)

# Brazos
for s in (-1, 1):
    loft(ax, [1.10, 1.25, 1.40, 1.52, 1.62],
             [0.022, 0.028, 0.034, 0.036, 0.040],
             [0.022, 0.028, 0.034, 0.036, 0.040], piel,
         cx=s*np.array([0.245, 0.215, 0.190, 0.175, 0.160]))

ax.text(0, 0, 2.25, "Claudia Shembaun", ha="center", fontsize=22, fontweight="bold")  # <- única línea nueva

ax.set_box_aspect((1, 1, 2.2))
ax.set_xlim(-0.5, 0.5); ax.set_ylim(-0.5, 0.5); ax.set_zlim(0, 2.2)
ax.set_axis_off()
ax.view_init(elev=8, azim=-60)
plt.show()