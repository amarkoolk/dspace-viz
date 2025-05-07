import matplotlib.pyplot as plt
from stl import mesh
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure()
ax = fig.add_subplot(projection="3d")
# ax = fig.gca(projection='3d')

# fig_polar = plt.figure("Polar coordinates")
# ax_polar = fig_polar.add_subplot(projection="3d")


# Load the STL file
filenames = ['dspace-laguna_track.stl', 'dspace-laguna_track2.stl']
for filename in filenames:
    stl_mesh = mesh.Mesh.from_file(filename)
    combined = []
    for v in stl_mesh.vectors:
        combined.append(v[0])
        combined.append(v[1])
        combined.append(v[2])
    combined = np.array(combined)
    ax.scatter(combined[::10, 0], combined[::10, 1], combined[::10, 2], label=filename)

plt.axis('equal')
plt.legend()
plt.show()