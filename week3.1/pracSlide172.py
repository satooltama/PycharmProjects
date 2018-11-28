import math as m

p = []

for i in range(1,4):
    pointin = input('Point {} (x,y) : '.format(i))
    x,y = pointin.split()
    pointtp = (int(x),int(y))
    p.append(pointtp)

print(p)

area = 2 / abs( p[0][0] * (p[1][1] - p[2][1]) - p[1][0] * (p[0][1]-p[2][1]) + p[2][0] * (p[0][1] - p[1][1]) )

print(area)
