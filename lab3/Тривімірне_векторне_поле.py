import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# векторне поля
def F(x, y, z):
    u = y / 2 + 2 * x
    v = x / z
    w = x * y / z**2
    return u, v, w

# Генерування точок у тривимірному просторі
x = np.linspace(-5, 3, 10)  
y = np.linspace(-5, 3, 10)
z = np.linspace(-5, 3, 10)
X, Y, Z = np.meshgrid(x, y, z)

# Обчислення компонент векторного поля
U, V, W = F(X, Y, Z)

# Побудова
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(X, Y, Z, U, V, W, length=0.2, normalize=True, color='black')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Тривимірне векторне поле')
plt.show()
