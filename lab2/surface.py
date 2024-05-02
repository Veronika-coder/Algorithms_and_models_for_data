import numpy as np

# Определение функции z
def z(x, y):
    return x**2 * np.sin(x) - 2 * y**3

# Задание промежутков для x и y с использованием arange
x = np.arange(-5, 5.01, 0.1)
y = np.arange(-5, 5.01, 0.1)
x, y = np.meshgrid(x, y)

# Вычисление значений z для каждой комбинации (x, y)
z_values = z(x, y)

# Сохранение данных в CSV файл
data = np.column_stack((x.flatten(), y.flatten(), z_values.flatten()))
np.savetxt('d:/8semestr/Algorithms_and_models_for_data/lab1/surface_data.csv', data, delimiter=',', header='x,y,z', comments='')

print("Данные сохранены в surface_data.csv")
