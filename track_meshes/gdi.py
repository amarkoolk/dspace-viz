from stl import mesh
import pygeodesy
import numpy as np

# Load the STL file
stl_mesh = mesh.Mesh.from_file('dspace-laguna_track.stl')

# Access mesh data (vertices, normals)
vertices = stl_mesh.vectors
normals = stl_mesh.normals

david_frame = pygeodesy.ltp.LocalCartesian(
    36.58706, # lat
    -121.75590, # lon
    0.0 # alt
)

36.58706, -121.75590, 0.0

# 36.58736160181 -121.75581850179
dspace_frame = pygeodesy.ltp.LocalCartesian(
    36.58736160181, # lat
    -121.75581850179, # lon
    754.0 # alt
)

def tolla(converter, arr):
    _x, _y, _z, lat, lon, h, *_ = converter.reverse(arr[0], arr[1], arr[2])
    return [lat, lon, h]

def toxyz(converter, arr):
    x, y, z, *_ = converter.forward(arr[0], arr[1], arr[2])
    return [x, y, z]

track = mesh.Mesh(np.zeros(vertices.shape[0], dtype=mesh.Mesh.dtype))

new_vertices = np.zeros_like(vertices)
for i, vector in enumerate(vertices):
    v0_lla = tolla(dspace_frame, vector[0])
    v1_lla = tolla(dspace_frame, vector[1])
    v2_lla = tolla(dspace_frame, vector[2])

    track.vectors[i][0] = toxyz(david_frame, v0_lla)
    track.vectors[i][1] = toxyz(david_frame, v1_lla)
    track.vectors[i][2] = toxyz(david_frame, v2_lla)

track.save(f"dspace-laguna_track2.stl")
