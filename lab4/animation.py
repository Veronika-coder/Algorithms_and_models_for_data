import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


# Задаємо початкові параметри
rectangle_width = 10
rectangle_height = 5

center_x = rectangle_width / 2
center_y = rectangle_height / 2

start_radius = min(rectangle_width, rectangle_height) / 4
start_angle = 0

# Список для зберігання кадрів
frames = []

def update(frame):
    # Зміна кута сектора кожні 5градусів
    angle = frame * np.pi / 36
    
    # Зміна радіуса сектора
    radius = start_radius + frame / 10

    # Обчислення координат кінця сектора
    end_x = center_x + radius * np.cos(start_angle + angle)
    end_y = center_y + radius * np.sin(start_angle + angle)
    
    # Очищення попереднього графіку
    plt.clf()

    # Відображення прямокутника
    plt.plot([0, rectangle_width, rectangle_width, 0, 0], [0, 0, rectangle_height, rectangle_height, 0], 'b-')

    # Відображення сектора круга
    plt.fill_between([center_x, end_x], [center_y, end_y], center_y, color='orange')

    # Встановлення меж вісей
    plt.axis([0, rectangle_width, 0, rectangle_height])
    plt.gca().set_aspect('equal', adjustable='box')
   
    plt.title('Рухаючийся сектор круга')
    
    # Додавання поточного кадру до списку кадрів
    frames.append(plt.gcf())


ani = animation.FuncAnimation(plt.gcf(), update, frames=72, interval=100)

ani.save('D:/8semestr/Algorithms_and_models_for_data/lab4/animation.gif', writer='imagemagick', fps=30)

plt.show()
