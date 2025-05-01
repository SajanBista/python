import math


SIZE = 20
grid = [['.' for _ in range(SIZE)] for _ in range(SIZE)]  


x1, y1 = map(int, input("first point (x1 y1): ").split())
x2, y2 = map(int, input("second point (x2 y2): ").split())


dx = x2 - x1
dy = y2 - y1
steps = max(abs(dx), abs(dy))

print("\npoints:")
for i in range(steps + 1):
    x = round(x1 + i * (dx / float(steps)))
    y = round(y1 + i * (dy / float(steps)))

   
    if 0 <= x < SIZE and 0 <= y < SIZE:
        grid[SIZE - 1 - y][x] = '#' 
    print(f"({x},{y})", end=" ")


print("\n\nGraph:")
for row in grid:
    print(" ".join(row))
