import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Задаємо параметри еліпсоїда
a = 1
b = 2
c = 3

# Параметризація еліпсоїда
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)
u, v = np.meshgrid(u, v)

x = a * np.cos(u) * np.sin(v)
y = b * np.sin(u) * np.sin(v)
z = c * np.cos(v)

# Побудова графіка
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

# Налаштування вісей та міток
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.title('Поверхня еліпсоїда')

# Додавання анотації з рівнянням функції
eq = r'$\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$'
ax.text2D(0.05, 0.95, eq, transform=ax.transAxes, fontsize=12)

plt.show()
