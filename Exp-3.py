import numpy as np

def translate(points, tx, ty):
    T = np.array([[1, 0, tx],
                  [0, 1, ty],
                  [0, 0, 1]])
    points = np.vstack((points.T, np.ones(points.shape[0])))
    transformed = T @ points
    return transformed[:2].T

def scale(points, sx, sy):
    S = np.array([[sx, 0, 0],
                  [0, sy, 0],
                  [0, 0, 1]])
    points = np.vstack((points.T, np.ones(points.shape[0])))
    transformed = S @ points
    return transformed[:2].T

def rotate(points, angle_deg):
    angle = np.radians(angle_deg)
    R = np.array([[np.cos(angle), -np.sin(angle), 0],
                  [np.sin(angle), np.cos(angle), 0],
                  [0, 0, 1]])
    points = np.vstack((points.T, np.ones(points.shape[0])))
    transformed = R @ points
    return transformed[:2].T

triangle = np.array([[0,0], [1,0], [0.5,1]])
rectangle = np.array([[0,0], [2,0], [2,1], [0,1]])

t_triangle = translate(triangle, 2, 3)
s_rectangle = scale(rectangle, 0.5, 2)
r_triangle = rotate(triangle, 45)

print("Translated Triangle:\n", t_triangle)
print("Scaled Rectangle:\n", s_rectangle)
print("Rotated Triangle:\n", r_triangle)
