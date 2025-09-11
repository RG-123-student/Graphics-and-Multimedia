import matplotlib.pyplot as plt

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

def midpoint_circle(xc, yc, r):
    points = []
    x, y = 0, r
    d = 1 - r
    while x <= y:
        pts = [(xc + x, yc + y), (xc - x, yc + y), (xc + x, yc - y), (xc - x, yc - y),
               (xc + y, yc + x), (xc - y, yc + x), (xc + y, yc - x), (xc - y, yc - x)]
        points.extend(pts)
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1
    return points

def midpoint_ellipse(xc, yc, rx, ry):
    points = []
    x, y = 0, ry
    rx2, ry2 = rx**2, ry**2
    dx, dy = 0, 2 * rx2 * y
    d1 = ry2 - rx2 * ry + 0.25 * rx2

    while dx < dy:
        pts = [(xc + x, yc + y), (xc - x, yc + y), (xc + x, yc - y), (xc - x, yc - y)]
        points.extend(pts)
        if d1 < 0:
            x += 1
            dx += 2 * ry2
            d1 += dx + ry2
        else:
            x += 1
            y -= 1
            dx += 2 * ry2
            dy -= 2 * rx2
            d1 += dx - dy + ry2

    d2 = ry2 * (x + 0.5)**2 + rx2 * (y - 1)**2 - rx2 * ry2
    while y >= 0:
        pts = [(xc + x, yc + y), (xc - x, yc + y), (xc + x, yc - y), (xc - x, yc - y)]
        points.extend(pts)
        if d2 > 0:
            y -= 1
            dy -= 2 * rx2
            d2 += rx2 - dy
        else:
            y -= 1
            x += 1
            dx += 2 * ry2
            dy -= 2 * rx2
            d2 += dx - dy + rx2
    return points

def plot(points, color):
    xs, ys = zip(*points)
    plt.scatter(xs, ys, color=color, s=10)

def main():
    plt.figure(figsize=(8, 8))
    plt.axis('equal')
    plt.grid(True)

    plot(bresenham_line(2, 3, 20, 15), 'red')
    plot(midpoint_circle(30, 20, 10), 'blue')
    plot(midpoint_ellipse(50, 30, 15, 10), 'green')

    plt.title("Bresenham Line (red), Midpoint Circle (blue), Midpoint Ellipse (green)")
    plt.show()

if __name__ == "__main__":
    main()
