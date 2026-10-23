import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Папка, де лежить
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "Варіант_9_spotify.csv")

# =====================================================
# Завдання 1. Зміна температури повітря (варіант 7)
# =====================================================
time = [3, 5, 7, 9, 10, 11, 12, 13, 15, 17, 19, 20, 21, 22, 23]
temp1 = [22, 22, 22.3, 23, 24, 24, 24, 24, 24.5, 24, 23.5, 23.5, 23, 22.8, 22]

plt.figure(figsize=(9, 5))
plt.plot(time, temp1, color="tomato", marker="o", linestyle="-", linewidth=2,
        markersize=6, label="Температура")
plt.title("Зміна температури повітря протягом доби")
plt.xlabel("Час, год")
plt.ylabel("Температура, °C")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, "task1_temperature.png"), dpi=150)
plt.show()

# =====================================================
# Завдання 2. y = sin x, z = cos x на [-6; 6], крок 0.2
# =====================================================
x = np.arange(-6, 6 + 0.2, 0.2)
y = np.sin(x)
z = np.cos(x)

plt.figure(figsize=(9, 5))
plt.plot(x, y, color="royalblue", linewidth=2, label="y = sin(x)")
plt.plot(x, z, color="darkorange", linewidth=2, linestyle="--", label="z = cos(x)")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.title("Графіки функцій y = sin(x) та z = cos(x)")
plt.xlabel("x")
plt.ylabel("y, z")
plt.grid(True, alpha=0.5)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, "task2_sin_cos.png"), dpi=150)
plt.show()

# =====================================================
# Завдання 3. Поверхня z = 2x*sin(x) + 3y*cos(y) на [-6; 6], крок 0.2
# =====================================================
def surface(X, Y):
    return 2 * X * np.sin(X) + 3 * Y * np.cos(Y)


# 3.1 np.arange()
xa = np.arange(-6, 6 + 0.2, 0.2)
ya = np.arange(-6, 6 + 0.2, 0.2)
Xa, Ya = np.meshgrid(xa, ya)
Za = surface(Xa, Ya)

fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection="3d")
surf = ax.plot_surface(Xa, Ya, Za, cmap="viridis", edgecolor="none")
fig.colorbar(surf, shrink=0.6, pad=0.1)
ax.set_title("z = 2x·sin(x) + 3y·cos(y)  (np.arange)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, "task3_surface_arange.png"), dpi=150)
plt.show()

# 3.2 np.linspace(): (12 / 0.2) + 1 = 61 точка -> крок 0.2
xl = np.linspace(-6, 6, 61)
yl = np.linspace(-6, 6, 61)
Xl, Yl = np.meshgrid(xl, yl)
Zl = surface(Xl, Yl)

fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection="3d")
surf = ax.plot_surface(Xl, Yl, Zl, cmap="plasma", edgecolor="none")
fig.colorbar(surf, shrink=0.6, pad=0.1)
ax.set_title("z = 2x·sin(x) + 3y·cos(y)  (np.linspace)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, "task3_surface_linspace.png"), dpi=150)
plt.show()

# =====================================================
# Завдання 4-5. Набір даних (з лабораторної роботи №4)
# =====================================================
df = pd.read_csv(DATA_FILE, encoding="utf-8-sig")
df.columns = df.columns.str.strip()

# Числові ознаки
num_cols = df.select_dtypes(include="number").columns.tolist()

# ---- Завдання 4. Кругова діаграма ----
# Частки - сума прослуховувань по кожній пісні
values = df[num_cols].sum()

# explode: виділяємо ознаку з найменшим значенням
explode = [0.15 if v == values.min() else 0 for v in values]

plt.figure(figsize=(8, 8))
plt.pie(values, labels=values.index, explode=explode, autopct="%1.1f%%",
        startangle=90, shadow=True,
        colors=plt.cm.Set3.colors[:len(values)])
plt.title("Кругова діаграма (сума прослуховувань по піснях)")
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, "task4_pie.png"), dpi=150)
plt.show()

# ---- Завдання 5. Гістограма ----
#пісня HUMBLE.
column = [c for c in df.columns if "HUMBLE" in c.upper()][0]

plt.figure(figsize=(9, 5))
plt.hist(df[column].dropna(), bins=10, color="seagreen", edgecolor="black", alpha=0.8)
plt.title(f"Гістограма ознаки «{column}»")
plt.xlabel("Кількість прослуховувань за день")
plt.ylabel("Частота (кількість днів)")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, "task5_hist.png"), dpi=150)
plt.show()