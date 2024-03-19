from math import sin
import math
a = 0
b = math.pi/2
N = 100
h = (b - a) / N
k = 1
S = 0

while k <= N:
    S += h / 2 * (sin(a + (k - 1) * h) + sin(a + k * h))

    k += 1

print(S)