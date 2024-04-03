import numpy as np
import matplotlib.pyplot as plt

# Дані
years = np.array([1900, 1913, 1929, 1938, 1950, 1960, 1970, 1980, 1990, 2000])
population = {
    'USA': np.array([76.4, 97.6, 122.2, 130.5, 153, 176, 200.5, 227, 247, 277]),
    'Germany': np.array([45.7, 54.7, 58.7, 62.3, 67, 72, 77, 78.5, 79, 82]),
    'France': np.array([40.8, 41.8, 42, 42, 42, 46, 50.5, 54, 56.5, 59]),
    'Japan': np.array([44, 51.6, 63.2, 71.8, 83, 93, 104, 116.8, 123.5, 127]),
    'USSR': np.array([123, 158, 171.5, 186.5, 205.5, 226.5, 247, 258.5, 290, 290])
}

# Побудова 3D стовпчикової діаграми
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Кількість країн
n_countries = len(population)

# Встановлення ширини стовпців та проміжку між ними
bar_width = 1.0
space_width = 0.05

# Переміщення по вісі x
x_offsets = np.linspace(-(bar_width + space_width) * (n_countries - 1) / 2, (bar_width + space_width) * (n_countries - 1) / 2, n_countries)

# Побудова стовпців для кожної країни
for i, (country, pop_data) in enumerate(population.items()):
    ax.bar(years + x_offsets[i], pop_data, zs=i, zdir='y', label=country, width=bar_width)

ax.set_xlabel('Рік')
ax.set_ylabel('Країна')
ax.set_zlabel('Чисельність населення, млн. чол.')
ax.set_yticks(range(n_countries))
ax.set_yticklabels(population.keys())
ax.set_title('Зростання чисельності населення')

# Вручну вставляємо легенду
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper left')

plt.tight_layout()

plt.show()
