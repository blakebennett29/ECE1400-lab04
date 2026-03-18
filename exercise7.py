import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create mesh grid with at least 120 points in each axis
x = np.linspace(-3, 3, 120)
y = np.linspace(-3, 3, 120)
X, Y = np.meshgrid(x, y) #make it a 2D grid of x and y values (a 2d array of x and y coordinates)

# Calculate z = y² - x² + 2xy
Z = Y**2 - X**2 + 2*X*Y #compute the z values for each (x, y) pair using the formula provided

# Create 3D surface plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1,1,1, projection='3d')

# Plot surface with jet colormap
surf = ax.plot_surface(X, Y, Z, cmap='jet', linewidth=0, antialiased=True)

# Labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('z = y² - x² + 2xy')

# Add colorbar
fig.colorbar(surf, ax=ax, label='Z value')

# Save and show
plt.savefig('exercise7_surface_plot.png', dpi=150, bbox_inches='tight')
plt.show()

print(f"Surface plot generated with {len(x)} × {len(y)} = {len(x)*len(y)} points")
print(f"Range: x ∈ [-3, 3], y ∈ [-3, 3]")
print(f"Z range: {Z.min():.2f} to {Z.max():.2f}")
