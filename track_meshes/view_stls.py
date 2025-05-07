import matplotlib.pyplot as plt
from stl import mesh
import numpy as np

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
    plt.scatter(combined[:, 0], combined[:, 1], label=filename)

plt.axis('equal')
plt.legend()
plt.show()