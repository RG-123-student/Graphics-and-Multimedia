import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

v = np.array([[0,0,0],[1,0,0],[1,1,0],[0,1,0],
              [0,0,1],[1,0,1],[1,1,1],[0,1,1]])

f = [[v[j] for j in [0,1,2,3]],
     [v[j] for j in [4,5,6,7]],
     [v[j] for j in [0,1,5,4]],
     [v[j] for j in [2,3,7,6]],
     [v[j] for j in [1,2,6,5]],
     [v[j] for j in [4,7,3,0]]]

c = ['red','blue','green','yellow','cyan','orange']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.add_collection3d(Poly3DCollection(f, facecolors=c, edgecolors='black'))
ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
ax.set_title('3D Cube with Flat Shading')
ax.set_box_aspect([1,1,1])
plt.show()
