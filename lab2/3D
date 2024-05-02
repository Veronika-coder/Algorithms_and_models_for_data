import numpy as np

years = np.array([1900, 1913, 1929, 1938, 1950, 1960, 1970, 1980, 1990, 2000])
population = {
    'USA': np.array([76.4, 97.6, 122.2, 130.5, 153, 176, 200.5, 227, 247, 277]),
    'Germany': np.array([45.7, 54.7, 58.7, 62.3, 67, 72, 77, 78.5, 79, 82]),
    'France': np.array([40.8, 41.8, 42, 42, 42, 46, 50.5, 54, 56.5, 59]),
    'Japan': np.array([44, 51.6, 63.2, 71.8, 83, 93, 104, 116.8, 123.5, 127]),
    'USSR': np.array([123, 158, 171.5, 186.5, 205.5, 226.5, 247, 258.5, 290, 290])
}

with open('d:/8semestr/Algorithms_and_models_for_data/lab2/population_data_3d.csv', 'w') as f:
    f.write('Year,USA,Germany,France,Japan,USSR\n')
    for i in range(len(years)):
        f.write(f"{years[i]},{population['USA'][i]},{population['Germany'][i]},{population['France'][i]},{population['Japan'][i]},{population['USSR'][i]}\n")

print("Данные сохранены в population_data_3d.csv")
