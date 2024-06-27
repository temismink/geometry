from matplotlib import pyplot as plt
import numpy as np

def draw_star_polygon(p, d):
    angles = np.linspace(0, 2 * np.pi, p, endpoint=False)
    points = np.column_stack([np.cos(angles), np.sin(angles)])
    indices = np.arange(p) * d % p
    star_points = points[indices]
    return np.append(star_points, [star_points[0]], axis=0)

# Define the star polygons
star_polygons = [
    (60, 35),
    (6, 2),
    (8, 2),  # {9/3}
    (9, 3), # {10/4}
    (5, 2), # {10/4}
    (10, 4), # {10/4}
    (60, 35), # {60/35}
    (6, 2)
]

# Plot the star polygons
fig, axes = plt.subplots(2, 4, figsize=(15, 10))
axes = axes.flatten()

for ax, (p, d) in zip(axes, star_polygons):
    star = draw_star_polygon(p, d)
    ax.plot(star[:, 0], star[:, 1], marker='o')
    ax.set_title(f'Star Polygon {p}/{d}')
    ax.set_aspect('equal')
    ax.axis('off')

# Hide the unused subplot
axes[-1].axis('off')

plt.tight_layout()
plt.show()
