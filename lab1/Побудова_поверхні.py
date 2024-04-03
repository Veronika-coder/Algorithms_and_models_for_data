import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Задаємо проміжки для x та y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Задаємо функцію z
z = x**2 * np.sin(x) - 2 * y**3

# Побудова графіка
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Побудова поверхні
surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Налаштування вісей
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Додавання колірної смуги
fig.colorbar(surf, shrink=0.5, aspect=5)

# Додавання анотації з рівнянням функції
eq = r'$z = x^2 \sin(x) - 2y^3$'
ax.text2D(0.05, 0.95, eq, transform=ax.transAxes, fontsize=12)

plt.show()
