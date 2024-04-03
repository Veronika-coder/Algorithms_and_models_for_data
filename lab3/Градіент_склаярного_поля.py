import numpy as np
import matplotlib.pyplot as plt

#скалярне поле
def u(x, y):
    return 4 * np.log(x**2 + y**2) - 8 * x * y

# Значення x і y
x = np.linspace(-5, 3, 100)
y = np.linspace(-5, 3, 100)

# Створення сітки координат
X, Y = np.meshgrid(x, y)

# Обчислення значень скалярного поля на сітці
Z = u(X, Y)

# Візуалізація скалярного поля
plt.pcolormesh(X, Y, Z, cmap='viridis')
plt.colorbar(label='Значення скалярного поля')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Скалярне поле')
plt.grid(True)
plt.show()
