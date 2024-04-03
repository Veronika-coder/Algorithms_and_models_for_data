import numpy as np
import matplotlib.pyplot as plt

# Визначення функцій
def z_negative(x):
    return (1 + x**2) / np.sqrt(1 + x**4)

def z_positive(x):
    return (2 * x + np.sin(x)**2) / (2 + x)

# Задання значень для x
x_negative = np.linspace(-10, 0, 100)
x_positive = np.linspace(0.01, 10, 100)

# Обчислення значень z для кожного діапазону x
z_neg_values = z_negative(x_negative)
z_pos_values = z_positive(x_positive)

# Побудова графіка для зони x <= 0
plt.figure(figsize=(8, 6))
plt.polar(x_negative, z_neg_values, label=r'$z = \frac{{1 + x^2}}{{\sqrt{1 + x^4}}}$', color='blue')
plt.title('Графік $z$ у полярних координатах для $x \leq 0$')
plt.legend(loc='lower right')
plt.grid(True)
plt.xlabel('$x$')
plt.ylabel('$z$')
plt.show()

# Побудова графіка для зони x > 0
plt.figure(figsize=(8, 6))
plt.polar(x_positive, z_pos_values, label=r'$z = \frac{{2x + \sin^2(x)}}{{2 + x}}$', color='red')
plt.title('Графік $z$ у полярних координатах для $x > 0$')
plt.legend(loc='lower right')
plt.grid(True)
plt.xlabel('$x$')
plt.ylabel('$z$')
plt.show()
