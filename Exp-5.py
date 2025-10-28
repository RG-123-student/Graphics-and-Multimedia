import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection

def draw(ax, v, e, c):
    ax.add_collection3d(Line3DCollection([(v[i], v[j]) for i, j in e], colors=c))

def trans(tx, ty, tz):
    return np.array([[1, 0, 0, tx],
                     [0, 1, 0, ty],
                     [0, 0, 1, tz],
                     [0, 0, 0, 1]])

def scale(sx, sy, sz):
    return np.array([[sx, 0, 0, 0],
                     [0, sy, 0, 0],
                     [0, 0, sz, 0],
                     [0, 0, 0, 1]])

def rotz(a):
    r = np.radians(a)
    return np.array([[np.cos(r), -np.sin(r), 0, 0],
                     [np.sin(r),  np.cos(r), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

def apply(v, m):
    return [(m @ np.array([*p, 1]))[:3] for p in v]

v = [(0,0,0),(1,0,0),(1,1,0),(0,1,0),
     (0,0,1),(1,0,1),(1,1,1),(0,1,1)]
e = [(0,1),(1,2),(2,3),(3,0),
     (4,5),(5,6),(6,7),(7,4),
     (0,4),(1,5),(2,6),(3,7)]

M = trans(2,2,0) @ scale(1.5,1.5,1.5) @ rotz(45)
vt = apply(v, M)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
draw(ax, v, e, 'blue')
draw(ax, vt, e, 'red')
ax.set_title("3D Transformations")
plt.show()
