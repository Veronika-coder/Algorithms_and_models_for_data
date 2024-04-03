import numpy as np
import matplotlib.pyplot as plt

def create_stream_line(x0, y0, z0, F, t0=0, t1=10, dt=0.01):
    t = np.arange(t0, t1, dt)
    xx_new = np.zeros_like(t)
    yy_new = np.zeros_like(t)
    zz_new = np.zeros_like(t)
    xx_new[0] = x0
    yy_new[0] = y0
    zz_new[0] = z0
    for i in range(1, t.size):
        dx, dy, dz = F(xx_new[i-1], yy_new[i-1], zz_new[i-1])
        norm = np.sqrt(dx**2 + dy**2 + dz**2)
        xx_new[i] = xx_new[i-1] + dx / norm * dt
        yy_new[i] = yy_new[i-1] + dy / norm * dt
        zz_new[i] = zz_new[i-1] + dz / norm * dt
    return xx_new, yy_new, zz_new

def plot_stream_lines(F, start_points, t0=0, t1=10, dt=0.01):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for point in start_points:
        x, y, z = create_stream_line(point[0], point[1], point[2], F, t0, t1, dt)
        ax.plot(x, y, z)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Лінії току в тривимірному просторі')
    plt.show()

def F(x, y, z):
    u = y / 2 + 2 * x
    v = x / z
    w = x * y / z**2
    return u, v, w

start_points = [(1, -2, 3), (-3, 1, -4), (2, 3, -1), (-4, -1, 2), (3, -3, 1), (0, 0, 0), (-2, 2, 2), (1, -1, -3), (-3, -3, 3), (2, 1, -2)]
plot_stream_lines(F, start_points)
