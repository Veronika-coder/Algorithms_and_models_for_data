import numpy as np

phi = np.linspace(0, 2*np.pi, 100)

# Задаємо сталу 'a'
a = 1

rho = (3 * a * np.cos(phi) * np.sin(phi)) / (np.cos(phi)**3 + np.sin(phi)**3)

data = np.column_stack((phi, rho))
np.savetxt('d:/8semestr/Algorithms_and_models_for_data/lab2/polar_data.csv', data, delimiter=',', header='phi,rho', comments='')

print("Данные сохранены в polar_data.csv")
