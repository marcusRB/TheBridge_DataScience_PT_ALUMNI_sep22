import math
import numpy as np

def eucl_dist(x,y):
    n = len(x)
    return sum([(abs(y[i]) - abs(x[i]))**2 for i in range(n)]) ** (1/2)

vec1 = np.array([5, 6, 7, -3])
vec2 = np.array([10, 1, 8, -6])


def eucl_dist(x,y):
    return math.sqrt(sum([(coord[0]-coord[1])**2]) for coord in zip(x,y))


def eucl_dist(x,y):
    return np.sqrt(sum((x-y)**2))