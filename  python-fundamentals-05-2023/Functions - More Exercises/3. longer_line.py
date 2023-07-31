import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Създаване на фигурата и осите на графиката
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Дефиниране на координатите на върховете на куба
x = [0, 0, 1, 1, 0, 0, 1, 1]
y = [0, 1, 1, 0, 0, 1, 1, 0]
z = [0, 0, 0, 0, 1, 1, 1, 1]

# Рисуване на куба
ax.scatter(x, y, z)
ax.plot(x[:4], y[:4], z[:4], 'k')
ax.plot(x[4:], y[4:], z[4:], 'k')
ax.plot([x[0], x[4]], [y[0], y[4]], [z[0], z[4]], 'k')
ax.plot([x[1], x[5]], [y[1], y[5]], [z[1], z[5]], 'k')
ax.plot([x[2], x[6]], [y[2], y[6]], [z[2], z[6]], 'k')
ax.plot([x[3], x[7]], [y[3], y[7]], [z[3], z[7]], 'k')

# Задаване на заглавието на графиката и мащабиране на осите
ax.set_title('3D Cube')
ax.set_xlim3d(0, 1)
ax.set_ylim3d(0, 1)
ax.set_zlim3d(0, 1)

# Показване на графиката
plt.show()