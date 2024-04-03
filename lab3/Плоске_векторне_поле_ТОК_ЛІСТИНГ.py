import numpy as np
import matplotlib.pyplot as plt

def F(x, y):
    return np.array([x**2 - 2*y, y**2 - 2*x])

def create_stream_line(x0, y0, F, t0=0, t1=10, dt=0.001):
    t = np.arange(t0, t1, dt)
    xx_new = np.zeros_like(t)
    yy_new = np.zeros_like(t)
    xx_new[0] = x0
    yy_new[0] = y0
    for i in range(1, t.size):
        dx, dy = F(x0, y0)
        norm = np.sqrt(dx**2 + dy**2)
        xx_new[i] = x0 + dx / norm * dt
        yy_new[i] = y0 + dy / norm * dt
        x0, y0 = xx_new[i], yy_new[i]
    return xx_new, yy_new

for i in range(1, 10):
    x1, y1 = create_stream_line(i, 0, F)
    plt.plot(x1, y1)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Лінії току')
plt.grid(True)
plt.show()
