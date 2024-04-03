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

# Побудова стовпчикової діаграми
plt.figure(figsize=(10, 6))

# Розташовуємо стовпці рівномірно вздовж вісі X
n_countries = len(population)
bar_width = 0.15  # Ширина стовпців
space_width = 0.05  # Проміжок між групами стовпців
group_width = bar_width * n_countries + space_width * (n_countries - 1)
bar_positions = np.arange(len(years)) - group_width / 2

# Перебір по країнам та побудова стовпчиків
for i, (country, pop_data) in enumerate(population.items()):
    plt.bar(bar_positions + i * (bar_width + space_width), pop_data, label=country, width=bar_width)

plt.title('Зростання чисельності населення')
plt.xlabel('Рік')
plt.ylabel('Чисельність населення, млн. чол.')
plt.xticks(bar_positions + group_width / 2, years)
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()
