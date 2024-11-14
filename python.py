import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from fractions import Fraction as fr

# Task 1: Plot points on the unit circle for given angles
angles_deg = [30, 45, 60, 90, 120, 150, 180, 270]  # degrees
angles_rad = np.radians(angles_deg)  # convert degrees to radians

# Create the plot
fig, ax = plt.subplots(figsize=(9, 6))  # Increase figure size to make it wider

# Create the unit circle
ymp = patches.Circle((0, 0), radius=1, fill=False, edgecolor='black', linewidth=2)
ax.add_patch(ymp)

# Set axis properties
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.axis('equal')

# Set axis limits and ticks
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

# Mark points on the circle
x_points = np.cos(angles_rad)  # x = cos(θ)
y_points = np.sin(angles_rad)  # y = sin(θ)

# Assign colors for each point
colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'black']

# Annotate the points with the angle labels
for i, angle in enumerate(angles_rad):
    ax.scatter(x_points[i], y_points[i], color=colors[i], marker='X', s=100)  # Plot points
    ax.annotate(f'{angles_deg[i]}°',
                xy=(x_points[i], y_points[i]), xycoords='data',
                xytext=(10, 10), textcoords='offset points', fontsize=12,
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))

# Show the plot
plt.show()

# Task 2: Enlarging the plot and modifying graph colors, line styles

# Define X range for sine and cosine plot
X = np.linspace(-3 * np.pi, 3 * np.pi, 512, endpoint=True)
C, S = np.cos(X), np.sin(X)

# Create a new figure for the sine and cosine plot
fig, ax = plt.subplots(figsize=(9, 6))  # Make the figure wider
ax.plot(X, C, label='cos(θ)', color='blue', linestyle='-', linewidth=2)  # Blue solid line for cosine
ax.plot(X, S, label='sin(θ)', color='red', linestyle='--', linewidth=2)  # Red dashed line for sine

# Add title and legend
ax.set_title('Sine and Cosine Functions')
ax.legend(loc='upper left')

# Customize x-ticks in terms of π
tick_labels = [r'$-\mathbf{3\pi}$', r'$-\mathbf{2\pi}$', r'$-\mathbf{\pi}$', r'$\mathbf{0}$', r'$\mathbf{\pi}$', r'$2\pi$', r'$3\pi$']
ax.set_xticks([-3*np.pi, -2*np.pi, -np.pi, 0, np.pi, 2*np.pi, 3*np.pi])
ax.set_xticklabels(tick_labels)

# Add grid and show the plot
ax.grid(True)
plt.show()
