__author__ = 'Roderik'
from math import *


def rotatePoint(angle, point, origin):
    sinT = sin(radians(angle))
    cosT = cos(radians(angle))
    return (origin[0] + (cosT * (point[0] - origin[0]) - sinT * (point[1] - origin[1])),
            origin[1] + (sinT * (point[0] - origin[0]) + cosT * (point[1] - origin[1])))



# 0 260
# 1 228.0 37.0
# 2 3.1538976466084208 230.96115026045985



# new
# (37, 228)
# print (rotatePoint(10, (37, 228), (0, 0)))



angle = 90
topLeft = rotatePoint(angle, (0, 228), (0, 0))
topRight = rotatePoint(angle, (37, 228), (0, 0))
bottomLeft = rotatePoint(angle, (0, 0), (0, 0))
bottomRight = rotatePoint(angle, (37, 0), (0, 0))
mostLeft = min(topLeft[0], topRight[0], bottomLeft[0], bottomRight[0])
mostRight = max(topLeft[0], topRight[0], bottomLeft[0], bottomRight[0])
mostBottom = min(topLeft[1], topRight[1], bottomLeft[1], bottomRight[1])
mostTop = max(topLeft[1], topRight[1], bottomLeft[1], bottomRight[1])
width = abs(mostRight - mostLeft)
height = abs(mostTop - mostBottom)

print (width, height)
# width = abs(max(topLeft[0], bottomLeft[0]) - min(topLeft[0], bottomLeft[0]))
# print (width)
