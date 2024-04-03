import numpy as np
import matplotlib.pyplot as plt

# Задаємо значення для кута phi
phi = np.linspace(0, 2*np.pi, 100)

# Задаємо сталу 'a'
a = 1

# Обчислюємо значення рау
rho = (3 * a * np.cos(phi) * np.sin(phi)) / (np.cos(phi)**3 + np.sin(phi)**3)

# Побудова графіка у полярних координатах
plt.figure(figsize=(6, 6))
ax = plt.subplot(111, polar=True)
ax.plot(phi, rho)

plt.title('Графік у полярних координатах')

# Додавання анотації з рівнянням функції
eq = r'$\rho = \frac{{3a \cos(\phi) \sin(\phi)}}{{\cos^3(\phi) + \sin^3(\phi)}}$'
ax.text(0.5, 0.5, eq, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=12)

plt.show()
