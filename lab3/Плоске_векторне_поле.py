import numpy as np
import matplotlib.pyplot as plt

# векторне поле
def u(x, y):
    return 4 * np.log(x**2 + y**2) - 8 * x * y

def v(x, y):
    return 4 * np.log(x**2 + y**2) + 8 * x * y

# Значення x і y
x = np.linspace(-5, 3, 20)
y = np.linspace(-5, 3, 20)

# Створення сітки координат
X, Y = np.meshgrid(x, y)

# Обчислення значень компонент векторного поля на сітці
u_val = u(X, Y)
v_val = v(X, Y)

# Візуалізація векторного поля за допомогою стрілок
plt.quiver(X, Y, u_val, v_val)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Векторне поле')
plt.grid(True)
plt.show()
