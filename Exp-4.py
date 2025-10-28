import matplotlib.pyplot as plt

L, R, B, T = 0, 1, 2, 3

def inside(p, e, win):
    x, y = p
    xmin, xmax, ymin, ymax = win
    return [x >= xmin, x <= xmax, y >= ymin, y <= ymax][e]

def intersect(p1, p2, e, win):
    xmin, xmax, ymin, ymax = win
    x1, y1 = p1; x2, y2 = p2
    if e == L: return (xmin, y1 + (y2 - y1) * (xmin - x1) / (x2 - x1))
    if e == R: return (xmax, y1 + (y2 - y1) * (xmax - x1) / (x2 - x1))
    if e == B: return (x1 + (x2 - x1) * (ymin - y1) / (y2 - y1), ymin)
    if e == T: return (x1 + (x2 - x1) * (ymax - y1) / (y2 - y1), ymax)

def clip(poly, win):
    out = poly
    for e in [L, R, B, T]:
        inp, out = out, []
        if not inp: break
        s = inp[-1]
        for p in inp:
            if inside(p, e, win):
                if not inside(s, e, win): out.append(intersect(s, p, e, win))
                out.append(p)
            elif inside(s, e, win):
                out.append(intersect(s, p, e, win))
            s = p
    return out

def draw(pts, col, lbl):
    x, y = zip(*(pts + [pts[0]]))
    plt.plot(x, y, color=col, label=lbl)

win = (100, 300, 100, 300)
poly = [(50, 150), (200, 50), (350, 150), (350, 300), (250, 350), (150, 300)]
clipped = clip(poly, win)

plt.figure(figsize=(8, 8))
draw(poly, 'blue', "Original")
draw([(win[0], win[2]), (win[1], win[2]), (win[1], win[3]), (win[0], win[3])], 'black', "Window")
draw(clipped, 'red', "Clipped")
plt.legend()
plt.title("Sutherland-Hodgman Polygon Clipping")
plt.grid(True)
plt.axis("equal")
plt.show()
