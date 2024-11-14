import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from fractions import Fraction as fr

angles_deg = [30, 45, 60, 90, 120, 150, 180, 270]
angles_rad = np.radians(angles_deg)
fig, ax = plt.subplots(figsize=(9, 6))
ymp = patches.Circle((0, 0), radius=1, fill=False, edgecolor='black', linewidth=2)
ax.add_patch(ymp)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.axis('equal')

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

x_points = np.cos(angles_rad)
y_points = np.sin(angles_rad)

colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'black']

for i, angle in enumerate(angles_rad):
    ax.scatter(x_points[i], y_points[i], color=colors[i], marker='X', s=100)
    ax.annotate(f'{angles_deg[i]}°',
                xy=(x_points[i], y_points[i]), xycoords='data',
                xytext=(10, 10), textcoords='offset points', fontsize=12,
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))
plt.show()

X = np.linspace(-3 * np.pi, 3 * np.pi, 512, endpoint=True)
C, S = np.cos(X), np.sin(X)

fig, ax = plt.subplots(figsize=(9, 6))
ax.plot(X, C, label='cos(θ)', color='blue', linestyle='-', linewidth=2)
ax.plot(X, S, label='sin(θ)', color='red', linestyle='--', linewidth=2)
ax.set_title('Sine and Cosine Functions')
ax.legend(loc='upper left')

tick_labels = [r'$-\mathbf{3\pi}$', r'$-\mathbf{2\pi}$', r'$-\mathbf{\pi}$', r'$\mathbf{0}$', r'$\mathbf{\pi}$', r'$2\pi$', r'$3\pi$']
ax.set_xticks([-3*np.pi, -2*np.pi, -np.pi, 0, np.pi, 2*np.pi, 3*np.pi])
ax.set_xticklabels(tick_labels)

ax.grid(True)
plt.show()
