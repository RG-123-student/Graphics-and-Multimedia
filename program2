import matplotlib.pyplot as plt
import numpy as np

def bresenham_line(x1, y1, x2, y2):
    points = []
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy: err, x1 = err - dy, x1 + sx
        if e2 < dx: err, y1 = err + dx, y1 + sy
    return points

def scanline_fill(polygon):
    ymin = min(y for _, y in polygon)
    ymax = max(y for _, y in polygon)
    edges = []
    n = len(polygon)
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i+1) % n]
        if y1 == y2:
            continue
        if y1 > y2:
            x1, y1, x2, y2 = x2, y2, x1, y1
        edges.append({'x': x1, 'y_min': y1, 'y_max': y2, 'inv_slope': (x2 - x1) / (y2 - y1)})

    filled_points = []
    for y in range(ymin, ymax+1):
        x_intersections = []
        for edge in edges:
            if edge['y_min'] <= y < edge['y_max']:
                x = edge['x'] + (y - edge['y_min']) * edge['inv_slope']
                x_intersections.append(x)
        x_intersections.sort()
        for i in range(0, len(x_intersections), 2):
            x_start = int(np.ceil(x_intersections[i]))
            x_end = int(np.floor(x_intersections[i+1]))
            for x in range(x_start, x_end+1):
                filled_points.append((x, y))
    return filled_points

def flood_fill(image, x, y, fill_color, boundary_color):
    max_y, max_x = image.shape
    if x < 0 or x >= max_x or y < 0 or y >= max_y:
        return
    if image[y, x] == fill_color or image[y, x] == boundary_color:
        return

    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if 0 <= cx < max_x and 0 <= cy < max_y and image[cy, cx] != fill_color and image[cy, cx] != boundary_color:
            image[cy, cx] = fill_color
            stack.extend([(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)])

def draw_polygon_edges(polygon):
    points = []
    n = len(polygon)
    for i in range(n):
        points.extend(bresenham_line(*polygon[i], *polygon[(i+1) % n]))
    return points

def main():
    polygon = [(10, 10), (40, 15), (35, 40), (15, 35)]
    width, height = 50, 50
    image = np.zeros((height, width), dtype=int)
    edge_points = draw_polygon_edges(polygon)
    for x, y in edge_points:
        if 0 <= x < width and 0 <= y < height:
            image[y, x] = 1

    fill_points = scanline_fill(polygon)
    for x, y in fill_points:
        if 0 <= x < width and 0 <= y < height:
            image[y, x] = 2

    flood_fill(image, 20, 20, fill_color=3, boundary_color=1)

    plt.imshow(image, cmap='Accent_r')
    plt.title("Polygon Scanline Fill and Flood Fill")
    plt.show()

if __name__ == '__main__':
    main()
